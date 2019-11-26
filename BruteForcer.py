from MatrixCreator import MatrixCreator
from timeit import default_timer as timer

'''Klasa zawierająca metody używane podczas przeglądu zupełnego'''
class BruteForcer:
    def __init__(self):
        self.all_routes = []

    def permute(self, nodes, start_node, end_node):
        if start_node == end_node:
            x = nodes[:]
            x.append(x[0])
            return x
        else:
            for i in range(start_node, end_node+1):
                nodes[start_node], nodes[i] = nodes[i], nodes[start_node]
                result = self.permute(nodes, start_node + 1, end_node)
                if result is not None:
                    self.all_routes.append(result)
                nodes[start_node], nodes[i] = nodes[i], nodes[start_node]

    def get_best_route(self, all_routes, matrix):
        routes_values = []
        best_sum = float('inf')
        for route in all_routes:
            i = 1
            sum = 0
            while i < len(route):
                sum += matrix[route[i-1]][route[i]]
                i+=1
            if sum < best_sum:
                best_sum, best_route = sum, route
        best_route.pop(-1)
        return [best_route, best_sum]



