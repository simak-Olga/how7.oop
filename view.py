
class Console_View(View):
    """Класс описывает взаимодействие с пользователем'''

    def get_variant(self, title):
        
        check_input = False
        while not check_input:
            try:
                menu = int(input(title))
                Logger.menu_logger(menu)  # записали в лог
                check_input = True
            except:
                print('Некорректный ввод, введите число')
                Logger.error_logger('Некорректный ввод пункта меню')

        return menu


    def get_value(self, title):
      """Метод для расчёта float или complex.
        Возвращает введенное число в формате float или complex"""

        check_input = False
        while not check_input:
            data = input(title)
            Logger.input_logger(data)
            try:
                data = float(data)
                Logger.input_logger(f'{data} преобразовано во float')
                check_input = True
            except:    
                try:
                    data = complex(data)
                    Logger.input_logger(f'{data} преобразовано в complex')
                    check_input = True
                except:
                    Logger.error_logger('Некорректный ввод числа')
                    print('Некорректный ввод числа')

        return data


    def view_data(self, data, title):
        """Метод выдает пользователю результат вычислений или сообщение об ошибке"""

        print('\nПолучен результат:')
        print(f'{title} = {data}')
        Logger.res_logger(f'{title} = {data}')


    def view_logger(self, fl):
        """Метод выдает пользователю в консоль для просмотра записи лог-файла"""

        Logger.view_log_logger(fl)
        with open(fl, 'r', encoding="utf8") as file:
            log_txt = file.read()
        print(log_txt)