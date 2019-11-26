'''Klasa LiveNode służąca do przechowywania informacji o nodach'''
class LiveNode:
    def __init__(self, route, cost, matrix):
        self.route = route
        self.cost = cost
        self.matrix = matrix


class NodeHelper:
    @staticmethod
    def get_routes(live_nodes):
        routes = [node.route for node in live_nodes]
        return routes
    @staticmethod
    def sort_by_cost(live_nodes):
        live_nodes.sort(key=lambda x: x.cost)

    @staticmethod
    def get_biggest_cost(live_nodes):
        NodeHelper.sort_by_cost(live_nodes)
        return live_nodes[0]


class NewBranchAndBounder:
    def __init__(self, matrix = []):
        self.matrix = matrix
        self.og_matrix = self.copy_matrix(matrix)

    def reduce_row(self, matrix, use_self=False):
        if use_self:
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

    def reduce_column(self, matrix,  use_self=False):
        if use_self:
            matrix = self.matrix
        # value to suma wszystkich najmniejszych elementów w każdym wierszu
        value = 0
        # Liczba wierszy  (len(matrix)) to liczba kolumn, ponieważ macierz jest kwadratowa
        for i in range(len(matrix)):
            # Sprawdzam który element w kolumnie jest najmniejszy i filtruje ją z 'X'
            column = self.get_column(i,matrix)
            filtered_col = list(filter(lambda x: (x != 'X'), column))
            if len(filtered_col) > 0:
                mini = min(filtered_col)
                value += mini
                # Jeżeli sprawdzam kolumny po kolei, to wiem że zawsze będe podmieniał za element i-ty w wierszu
                for j in range(len(matrix)):
                    if matrix[j][i] != 'X':
                        matrix[j][i] -= mini
        return value

    def get_column(self, colnum, matrix, use_self=False):
        if use_self:
            matrix = self.matrix
        return [row[colnum] for row in matrix]

    '''Obliczanie dolnej granicy, która składa się na koszt drogi wierzchołka'''
    def get_lower_bound(self, matrix, use_self = False):
        if use_self:
            matrix = self.matrix
        row_value = self.reduce_row(matrix)
        column_value = self.reduce_column(matrix)
        return row_value + column_value

    '''Przy dodawaniu ścieżki do wyszukania optymalnej ścieżki (od-do) ograniczam macierz przez ustawienie 
        wszystkich ścieżek wychodzących do from_edge i wchodzących do to_edge na nieskończoność
        Funkcja nie robi nic kiedy ścieżka route posiada tylko jeden element'''
    def prep_matrix(self, route, matrix, use_self=False):
        if use_self:
            matrix = self.matrix
        # Ustawienie dla wszystkich ścieżek wychodzących z wszystkich wierzchołków oprócz ostatniego (bo z ostatniego już nic nie wychodzi) na 'X'
        for rownum in route[:-1]:
            for i in range(len(matrix[rownum])):
                matrix[rownum][i] = 'X'
        # Ustawienie dla wszystkich ścieżek wchodzących z wszystkich wierzchołków oprócz pierwszego (bo do pierwszego nic nie wchodzi) na 'X'
        for colnum in route[1:]:
            for i in range(len(matrix)):
                matrix[i][colnum] = 'X'
        # Ustawienie ścieżek powrotnych na nieskończoność
        i = len(route) - 1
        j = len(route) - 2
        while i >= 0:
            while j >= 0:
                matrix[route[i]][route[j]] = 'X'
                j -= 1
            i -= 1
            j = i - 1

    '''Funkcja służąca do kopiowania macierzy, ponieważ powyższe funkcje modyfikują macierz, a nie zawsze te zachowanie jest potrzebne'''
    def copy_matrix(self, matrix):
        x = []
        for i in matrix:
            x.append(i[:])
        return x


    ''' Zwraca długość najdłuższej ścieżki '''
    def get_longest_route_size(self, path_list):
        if len(path_list) == 0:
            return 0
        else:
            x = sorted(path_list, key=lambda y: len(y), reverse=True)
            return len(x[0])

    def get_routes_to_check(self, path_to_expand):
        routes = []
        matrix_length = range(len(self.matrix))
        for i in matrix_length:
            if i not in path_to_expand:
                path_to_expand.append(i)
                routes.append(path_to_expand[:])
                path_to_expand.remove(i)
        return routes


    def get_best_route(self):
        live_nodes = []
        cost = self.get_lower_bound(self.matrix)
        # Stworzenie pierwszego noda, który będzie rozwijany, zawsze to będzie zero
        node = LiveNode([0], cost, self.copy_matrix(self.matrix))
        live_nodes.append(node)
        last_best_node = LiveNode(['x'],float('inf'),[])
        # Główna pętla iterująca po kolejnych nodahc
        while True:
            routes = self.get_routes_to_check(node.route)
            for i in routes:
                route_cost = self.matrix[i[-2]][i[-1]]
                future_matrix = self.copy_matrix(node.matrix)
                self.prep_matrix(i, future_matrix)
                to_lower_bound = self.get_lower_bound(future_matrix)
                from_lower_bound = node.cost
                cost = from_lower_bound + route_cost + to_lower_bound
                newlv = LiveNode(i, cost, self.copy_matrix(future_matrix))
                live_nodes.append(newlv)
            live_nodes.remove(node)
            node = NodeHelper.get_biggest_cost(live_nodes)
            if node.cost > last_best_node.cost and len(last_best_node.route) == len(self.matrix):
                node = last_best_node
                break
            last_best_node = LiveNode(node.route, node.cost, self.copy_matrix(node.matrix))
        return node


# get_longest_route_size test
# lv1=LiveNode([0,1,2,3],21,[])
# lv2=LiveNode([0],12,[[3,4,5],[2,3,3],[7,4,5]])
# lv3=LiveNode([0,1,2],13213212,[[1,2],[2,3]])
# live_nodes = [lv1,lv2,lv3]
# routes = NodeHelper.get_routes(live_nodes)
# routelen = nbab.get_longest_route_size(routes)
# print(routelen)
