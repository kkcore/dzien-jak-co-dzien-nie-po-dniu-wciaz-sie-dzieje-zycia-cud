import logging
import random
from MatrixCreator import MatrixCreator
from BruteForcer import BruteForcer
from NewBranchAndBounder import NewBranchAndBounder
from BranchAndBounder import BranchAndBounder

logging.basicConfig(filename='logs',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

# matrix = [['X',20,30,10,11],[15,'X',16,4,2],[3,5,'X',2,4],[19,6,18,'X',3],[16,4,7,16,'X']]
matrix_creator = MatrixCreator()
matrix = matrix_creator.generate_matrix(5)
matrix = [['X', 4, 2, 9, 9],[3, 'X', 1, 3, 3],[2, 8, 'X', 1, 3],[0, 7, 0, 'X', 8],[2, 2, 2, 5, 'X']]
#newBranchAndBound test
nbab = NewBranchAndBounder(matrix)
matrix_cp = nbab.copy_matrix(matrix)
for i in matrix:
    print(i)
print('\n')
node = nbab.get_best_route()
print([node.route, node.cost])

matrix = matrix_cp
# BruteForcer test
n = len(matrix)
a = list(range(len(matrix)))
x = BruteForcer()
x.permute(a, 1, n-1)

route = x.get_best_route(x.all_routes, matrix)
print(route)
