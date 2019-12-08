from MatrixCreator import MatrixCreator
from BruteForcer import BruteForcer
from NewBranchAndBounder import NewBranchAndBounder
from DynamicProgramming import DynamicProgrammer
class MainMenu:
    _opening = " 1. Wczytaj dane z pliku \n 2. Wyświetl wczytane dane \n 3. Uruchom przegląd zupełny" \
               "\n 4. Uruchom metodę podziału i ograniczeń \n 5. Uruchom programowanie dynamiczne\n" \
               " 6. Wyjdź z programu"
    _data = None
    _matrix = []
    _creator = None
    @classmethod
    def interact(cls):
        x = None
        while True:
            print(cls._opening)
            x = input('Podaj liczbę 1-6 z punktów podanych wyżej ')
            try:
                x = int(x)
                if x == 1:
                    z = cls.load_data()
                    while z == 'again':
                        z = cls.load_data()
                elif x == 2:
                    cls.show_data()
                elif x == 3:
                    cls.run_brute()
                elif x == 4:
                    cls.run_branch()
                elif x == 5:
                    cls.run_dynamic()
                elif x == 6:
                    return
                else:
                    x = input('Podałeś zły numer! Spróbuj jeszcze raz ')
            except:
                print('Podałeś złe dane, spróbuj jeszcze raz! ')

    @classmethod
    def load_data(cls):
        file_path = input('Podaj ścieżkę pliku do wczytania ' )
        load_type = input(' 1. Wczytaj format danych z internetu\n 2. Wczytaj format prosty ')
        try:
            load_type = int(load_type)
            print('\n')
            if load_type != 1 and load_type != 2:
                print('Wybrano złą opcję')
                return
        except TypeError:
            return
        cls._creator = MatrixCreator()
        if load_type == 1:
            result = cls._creator.create_matrix(file_path)
        if load_type == 2:
            result = cls._creator.create_matrix_new(file_path)
        if isinstance(result, list):
            cls._matrix = result
        else:
            print('Podano złą ścieżkę lub zły format pliku, co robić?')
            select = input(' 1. Przejdź do menu głównego \n 2. Podaj ścieżkę jeszcze raz ')
            try:
                select = int(select)
                if select == 1:
                    return
                if select == 2:
                    return 'again'
                else:
                    print('Wybrano złą opcję...')
                    return
            except TypeError:
                print('Wybrano złą opcję...')
                return



    @classmethod
    def show_data(cls):
        if cls._creator is not None:
            cls._creator.pretty_print_matrix(cls._matrix)
        else:
            print('Najpierw wczytaj dane!')


    @classmethod
    def run_brute(cls):
        n = len(cls._matrix)
        a = list(range(len(cls._matrix)))
        x = BruteForcer()
        x.permute(a, 1, n - 1)
        route = x.get_best_route(x.all_routes, cls._matrix)
        print(route)


    @classmethod
    def run_branch(cls):
        bab = NewBranchAndBounder(cls._matrix)
        x = bab.get_best_route()
        print([x.route, x.cost])
        # algorytm modyfikuje tablice wiec przywroceine starej tablicy
        cls._matrix = bab.og_matrix


    @classmethod
    def run_dynamic(cls):
        dp = DynamicProgrammer(cls._matrix)
        cost = dp.get_best_route(1, 0)
        print(cost)


MainMenu.interact()