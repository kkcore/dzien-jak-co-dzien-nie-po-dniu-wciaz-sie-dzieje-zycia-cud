import logging
import random
from MatrixCreator import MatrixCreator
from BruteForcer import BruteForcer
from NewBranchAndBounder import NewBranchAndBounder
from DynamicProgramming import DynamicProgrammer


logging.basicConfig(filename='banb.txt',
                    filemode='a',
                    format='%(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)



# test efektywności metody B&B
# from timeit import default_timer as timer
#
# N = 15
# nbab_sum = 0
# matrix_creator = MatrixCreator()
# while nbab_sum < 200:
#     nbab_sum = 0
#     for i in range(10):
#         matrix = matrix_creator.generate_matrix(N)
#         nbabs = timer()
#         nbab = NewBranchAndBounder(matrix)
#         node = nbab.get_best_route()
#         nbabe = timer()
#         nbab_sum += nbabe - nbabs
#     logging.info(f"{str(N)}, {str(nbab_sum / 10)}")
#     N += 1


#Tests 1
# from timeit import default_timer as timer
#
# matrix_creator = MatrixCreator()
# N = [3, 5, 7, 9, 11, 13, 15]
# N = [13, 15]
# for i in N:
#     nbab_sum = 0
#     dyn_sum = 0
#     brute_sum = 0
#     for j in range(100):
#         matrix = matrix_creator.generate_matrix(i)
#         # brute
#         brutes = timer()
#         n = len(matrix)
#         a = list(range(len(matrix)))
#         x = BruteForcer()
#         x.permute(a, 1, n - 1)
#         route = x.get_best_route(x.all_routes, matrix)
#         brutee = timer()
#         brute_sum += brutee - brutes
#         if j == 9:
#             logging.info(f"'brute', {str(i)}, {str(brute_sum/10)}")
#
#         # dynammic
#         dynamics = timer()
#         dp = DynamicProgrammer(matrix)
#         route = dp.get_best_route(1, 0)
#         dynamice = timer()
#         dyn_sum += dynamice - dynamics
#         if j == 9:
#              logging.info(f"'dynammic', {str(i)}, {str(dyn_sum / 10)}")
#
#         # newBranchAndBound test
#         nbabs = timer()
#         nbab = NewBranchAndBounder(matrix)
#         node = nbab.get_best_route()
#         nbabe = timer()
#         nbab_sum += nbabe - nbabs
#         if j == 9:
#             logging.info(f"'branchbound', {str(i)}, {str(nbab_sum/10)}")


#
matrix_creator = MatrixCreator()
matrix = matrix_creator.generate_matrix(17)
# #matrix = [['X',20,30,10,11],[15,'X',16,4,2],[3,5,'X',2,4],[19,6,18,'X',3],[16,4,7,16,'X']]
# #matrix = [['X', 4, 1, 5],[8, 'X', 3, 8],[5, 6, 'X', 8],[3, 7, 6, 'X']]
# #matrix = [['X', 2, 1, 8, 1],[2, 'X', 3, 1, 8],[2, 7, 'X', 2, 5],[5, 6, 1, 'X', 2],[4, 3, 1, 2, 'X']]
# #matrix = [['X', 0, 8, 8, 4],[2, 'X', 7, 7, 9],[8, 6, 'X', 5, 3],[7, 0, 1, 'X', 3],[1, 3, 5, 1, 'X']]
#matrix = [['X', 3, 5, 48, 48, 8, 8, 5, 5, 3, 3, 0, 3, 5, 8, 8, 5], [3, 'X', 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 0, 3, 8, 8, 5], [5, 3, 'X', 72, 72, 48, 48, 24, 24, 3, 3, 5, 3, 0, 48, 48, 24], [48, 48, 74, 'X', 0, 6, 6, 12, 12, 48, 48, 48, 48, 74, 6, 6, 12], [48, 48, 74, 0, 'X', 6, 6, 12, 12, 48, 48, 48, 48, 74, 6, 6, 12], [8, 8, 50, 6, 6, 'X', 0, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8], [8, 8, 50, 6, 6, 0, 'X', 8, 8, 8, 8, 8, 8, 50, 0, 0, 8], [5, 5, 26, 12, 12, 8, 8, 'X', 0, 5, 5, 5, 5, 26, 8, 8, 0], [5, 5, 26, 12, 12, 8, 8, 0, 'X', 5, 5, 5, 5, 26, 8, 8, 0], [3, 0, 3, 48, 48, 8, 8, 5, 5, 'X', 0, 3, 0, 3, 8, 8, 5], [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 'X', 3, 0, 3, 8, 8, 5], [0, 3, 5, 48, 48, 8, 8, 5, 5, 3, 3, 'X', 3, 5, 8, 8, 5], [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 'X', 3, 8, 8, 5], [5, 3, 0, 72, 72, 48, 48, 24, 24, 3, 3, 5, 3, 'X', 48, 48, 24], [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 'X', 0, 8], [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 0, 'X', 8], [5, 5, 26, 12, 12, 8, 8, 0, 0, 5, 5, 5, 5, 26, 8, 8, 'X']]
#
# #newBranchAndBound test
# nbab = NewBranchAndBounder(matrix)
# matrix_cp = nbab.copy_matrix(matrix)
# for i in matrix:
#     print(i)
# print('\n')
# node = nbab.get_best_route()
# print([node.route, node.cost])
#
# matrix = matrix_cp
# # BruteForcer test
# # print(matrix)
n = len(matrix)
a = list(range(len(matrix)))
x = BruteForcer()
x.permute(a, 1, n-1)
#
# route = x.get_best_route(x.all_routes, matrix)
# print(route)
# print(matrix)
# dp = DynamicProgrammer(matrix)
# route = dp.get_best_route(1, 0)
# print(route)
