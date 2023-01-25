class App:
    """ Класс App(presenter)- запуск и верхнее меню приложения.
    При инициализации принимает презентер - компоненту управления связью между интерфейсом пользователя
    и моделью расчета, и тип пользовательского интерфейса.
    """

    def __init__(self, presenter, view):
        self.__presenter = presenter
        self.__view = view

    def start(self):
        """ метод запуска приложения, где определены связи между интерфесом и моделью расчета.
       Ниже указаны варианты меню"""

        while True:
            menu = self.__view.get_variant("""
                    Выберите пункт меню:
                        1 - операции с числами
                        2 - посмотреть лог файл
                        3 - выход из программы
                    """)
            if menu == 1:
                self.__presenter.button_click()
            elif menu == 2:
                self.__view.view_logger("log.txt")
            elif menu == 3:
                break
            else:
                print('Выберите действительный пункт меню')