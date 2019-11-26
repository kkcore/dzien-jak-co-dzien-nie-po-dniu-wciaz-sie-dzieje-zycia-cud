'''Klasa zawierająca funkcję tworząca macierz z pliku podanego jako argument'''
import random

class MatrixCreator:

    def create_matrix(self, file_path = 'data/br17.atsp'):
        try:
            with open(file_path, 'r') as file_handle:
                # Ominięcie pierwszych 7 linii oraz ostatniej (EOF) z pliku z opisami
                lines_list = file_handle.readlines()[7:-1]
                numbers = []
                for line in lines_list:
                    numbers += line.split()
                matrix = []
                matrix_row = []
                # Wyciągnięcie separatora, który we wszystkich plikach wejściowych jest na początku macierzy
                separator = numbers[0]
                for number in numbers[1:]:
                    if number == separator:
                        matrix.append(matrix_row)
                        matrix_row = []
                        continue
                    matrix_row.append(int(number))
                self.set_loops_to_infinity(matrix)
        except:
            return None
        return matrix

    '''Funkcja drukująca na obrazie macierz w czytelny sposób (wiersz po wierszu)'''
    def pretty_print_matrix(self, matrix):
        if len(matrix) > 0:
            for row in matrix:
                print(row)
        else:
            print(matrix)
    '''Ustawia pętle w grafie na nieskończoność (string "X")'''
    def set_loops_to_infinity(self, matrix):
        for i in range(len(matrix)):
            matrix[i][i] = 'X'

    # Do generowania losowych macierzy bez użycia pliku
    def generate_matrix(self, size):
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(random.randrange(0,50))
        self.set_loops_to_infinity(matrix)
        return matrix


# Do testowania wydruków funkcji, gdy używa się moduły MatrixCreator jako skrypt
# matrix_creator = MatrixCreator()
# matrix = matrix_creator.create_matrix('data/users.atsp')
# matrix = matrix_creator.generate_matrix(5)
# matrix_creator.pretty_print_matrix(matrix)
