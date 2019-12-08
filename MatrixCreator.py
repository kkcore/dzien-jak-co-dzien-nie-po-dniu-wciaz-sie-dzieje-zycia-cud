'''Klasa zawierająca funkcję tworząca macierz z pliku podanego jako argument'''
import random

class MatrixCreator:

    def create_matrix(self, file_path = 'data/br17.atsp'):
        try:
            with open(file_path, 'r') as file_handle:
                # Odczytanie wymiaru macierzy
                all_lines = file_handle.readlines()
                dim_line = all_lines[3]
                N = [int(s) for s in dim_line.split() if s.isdigit()]
                N = N[0]
                # Ominięcie pierwszych 7 linii oraz ostatniej (EOF) z pliku z opisami
                lines_list = all_lines[7:-1]
                numbers = []
                for line in lines_list:
                    numbers += line.split()
                matrix = []
                matrix_row = []
                # Wyciągnięcie separatora, który we wszystkich plikach wejściowych jest na początku macierzy
                i = 1
                for number in numbers:
                    number = float(number)
                    matrix_row.append(int(number))
                    if i == N:
                        matrix.append(matrix_row)
                        matrix_row = []
                        i = 1
                        continue
                    i += 1
                self.set_loops_to_infinity(matrix)
                print(matrix)
        except:
            return None
        return matrix

    def create_matrix_new(self, file_path):
        try:
            matrix = []
            with open(file_path, 'r') as file_handle:
                lines = file_handle.read().splitlines()
                counter = int(lines[0])
                lines = lines[1:]
                for i in range(counter):
                    converted = [int(s) for s in lines[i].split() if s.isdigit()]
                    matrix.append(converted)
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
# matrix = matrix_creator.create_matrix('data/br17.atsp')
# matrix_creator.pretty_print_matrix(matrix)
# matrix = matrix_creator.generate_matrix(5)
