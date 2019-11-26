from MatrixCreator import MatrixCreator
from BruteForcer import BruteForcer
from BranchAndBounder import BranchAndBounder

class MainMenu:
    _opening = " 1. Wczytaj dane z pliku \n 2. Wyświetl wczytane dane \n 3. Uruchom przegląd zupełny" \
               "\n 4. Uruchom metodę podziału i ograniczeń \n 5. Uruchom programownanie dynamiczne\n" \
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
                    print('Jeszcze nie zaprogramowano tej funkcji ')
                elif x == 6:
                    return
                else:
                    x = input('Podałeś zły numer! Spróbuj jeszcze raz ')
            except:
                print('Podałeś złe dane, spróbuj jeszcze raz! ')

    @classmethod
    def load_data(cls):
        file_path = input('Podaj ścieżkę pliku do wczytania ' )
        cls._creator = MatrixCreator()
        result = cls._creator.create_matrix(file_path)
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
        bab = BranchAndBounder(cls._matrix)
        x = bab.get_best_route()
        print(x)

MainMenu.interact()