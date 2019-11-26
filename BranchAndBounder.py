from MatrixCreator import MatrixCreator
from timeit import default_timer as timer

class BranchAndBounder:
    def __init__(self, matrix = []):
        self.cost = 0
        self.matrix = matrix

    def reduce_row(self, matrix=None):
        if matrix == None:
            matrix = self.matrix
        # value to suma wszystkich najmniejszych elementów w każdym wierszu
        value = 0
        for row in matrix:
            filtered_row = list(filter(lambda x: (x != 'X'), row))
            if len(filtered_row) > 0:
                mini = min(filtered_row)
                value += mini
                for i in range(len(row)):
                    if row[i] != 'X':
                        row[i] -= mini
                # row[row.index(mini)] = 0
        return value

    def reduce_column(self, matrix=None):
        if matrix == None:
            matrix = self.matrix
        # value to suma wszystkich najmniejszych elementów w każdym wierszu
        value = 0
        # Liczba wierszy  (len(matrix)) to liczba kolumn, ponieważ macierz jest kwadratowa
        for i in range(len(matrix)):
            # Sprawdzam który element w kolumnie jest najmniejszy
            column = self.get_column(i,matrix)
            filtered_col = list(filter(lambda x: (x != 'X'), column))
            if len(filtered_col) > 0:
                mini = min(filtered_col)
                value += mini
                # Jeżeli sprawdzam kolumny po kolei, to wiem że zawsze będe podmieniał za element i-ty w wierszu
                for j in column:
                    if matrix[column.index(j)][i] != 'X':
                        matrix[column.index(j)][i] -= mini
        return value

    def get_column(self, colnum, matrix = None):
        if matrix == None:
            matrix = self.matrix
        return [row[colnum] for row in matrix]

    '''Obliczanie dolnej granicy, która składa się na koszt drogi wierzchołka'''
    def get_lower_bound(self, matrix_cp=None):
        if matrix_cp == None:
            matrix_cp = self.matrix
        row_value = self.reduce_row(matrix_cp)
        column_value = self.reduce_column(matrix_cp)
        return row_value + column_value

    '''Przy dodawaniu ścieżki do wyszukania optymalnej ścieżki (od-do) ograniczam macierz przez ustawienie 
        wszystkich ścieżek wychodzących do from_edge i wchodzących do to_edge na nieskończoność '''
    def prep_matrix(self, route):
        matrix_cp = []
        for i in self.matrix:
            matrix_cp.append(i[:])
        # Ustawienie dla wszystkich ścieżek wychodzących z wszystkich wierzchołków oprócz ostatniego (bo z ostatniego już nic nie wychodzi) na 'X'
        for rownum in route[:-1]:
            for i in range(len(matrix_cp[rownum])):
                matrix_cp[rownum][i] = 'X'
        # Ustawienie dla wszystkich ścieżek wchodzących z wszystkich wierzchołków oprócz pierwszego (bo do pierwszego nic nie wchodzi) na 'X'
        for colnum in route[1:]:
            for i in range(len(matrix_cp)):
                matrix_cp[i][colnum] = 'X'
        # Ustawienie ścieżek powrotnych na nieskończoność
        i = len(route) - 1
        j = len(route) - 2
        # for i in range(len(route) - 1):
        #     matrix_cp[route[i+1]][route[i]] = 'X'
        while i >= 0:
            while j >= 0:
                matrix_cp[route[i]][route[j]] = 'X'
                j -= 1
            i -= 1
            j = i - 1

        return matrix_cp

    def get_best_route(self):
        live_nodes = []
        route_to_extend = [[0]]
        # Create start paths
        while self.get_longest_route_size(live_nodes) != len(self.matrix):
            matrix_cp = []
            for i in self.matrix:
                matrix_cp.append(i)
            self.matrix = self.prep_matrix(route_to_extend[0])
            # Usunięcie ścieżki, która rozszerzana, żeby uniknąć rozwijania w kółko tego samego noda.
            if len(live_nodes) > 0:
                live_nodes.remove(route_to_extend)
            if route_to_extend == [[0]]:
                from_lower_bound = self.get_lower_bound(self.matrix)
            else:
                from_lower_bound = route_to_extend[1]
            routes = self.get_routes_to_check(route_to_extend[0])
            for i in routes:
                route_cost = self.matrix[i[-2]][i[-1]]
                matrix_to_calc = self.prep_matrix(i)
                to_lower_bound = self.get_lower_bound(matrix_to_calc)
                # if route_cost == 'X':
                #     route_cost = 0
                cost = from_lower_bound + route_cost + to_lower_bound
                live_nodes.append([i, cost])
            route_to_extend = sorted(live_nodes, key=lambda x: x[1])[0]
        return route_to_extend

# Zwraca długość najdłuższej ścieżki
    def get_longest_route_size(self, path_list):
        if len(path_list) == 0:
            return 0
        else:
            x = sorted(path_list, key=lambda y: len(y[0]), reverse=True)
            return len(x[0][0])

    def get_routes_to_check(self, path_to_expand):
        routes = []
        matrix_length = range(len(self.matrix))
        for i in matrix_length:
            if i not in path_to_expand:
                path_to_expand.append(i)
                routes.append(path_to_expand[:])
                path_to_expand.remove(i)
        return routes


