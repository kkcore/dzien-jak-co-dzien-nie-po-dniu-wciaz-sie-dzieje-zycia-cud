import logging
import random
from MatrixCreator import MatrixCreator
from BruteForcer import BruteForcer
from BranchAndBounder import BranchAndBounder

logging.basicConfig(filename='logs',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

matrix = [['X',20,30,10,11],[15,'X',16,4,2],[3,5,'X',2,4],[19,6,18,'X',3],[16,4,7,16,'X']]
matrix_creator = MatrixCreator()
matrix = matrix_creator.generate_matrix(5)
matrix = [['X', 18, 15, 6, 45],[13, 'X', 39, 45, 43],[37, 34, 'X', 30, 18],[20, 46, 26, 'X', 44],[27, 36, 14, 10, 'X']]
for i in matrix:
    print(i)
bab = BranchAndBounder(matrix)
x = bab.get_best_route()
print(x)
n = len(matrix)
a = list(range(len(matrix)))
x = BruteForcer()
x.permute(a, 1, n-1)
route = x.get_best_route(x.all_routes, matrix)
print(route)
