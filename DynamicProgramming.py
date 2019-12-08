class DynamicProgrammer:

    def __init__(self, matrix):
        self.matrix = matrix
        self.visited_all = (1 << len(self.matrix)) - 1

    # mask - zbiór miast, jeżeli 1 to miasto odwiedzone, jeżeli 0 to nieodwiedzone
    # pos - rozpatrywany wierzchołek
    # BRAK zapisywania poprzednich wyników!
    def get_best_route(self, mask, pos):
        if mask == self.visited_all:
            return self.matrix[pos][0]
        res = float('inf')
        for node in range(len(self.matrix)):
            if (mask & (1 << node)) == 0:
                new_res = self.matrix[pos][node] + self.get_best_route(mask | (1 << node), node)
                res = min(res, new_res)
        return res

# matrix = [['X', 4, 1, 5],[8, 'X', 3, 8],[5, 6, 'X', 8],[3, 7, 6, 'X']]
# dp = DynamicProgrammer(matrix)
# dp.get_best_route(1,0)