Cоздаем интерфейс

view = Console_View() cвязь интерфейса и модели расчета
presenter = Presenter(view)
создаем экземпляр приложения для запуска меню
app = App(presenter, view)
запускаем приложение с заданными параметрами
app.start()
"""

from App import App
from Console_View import Console_View
from MVP.Presenter import Presenter

view = Console_View()
presenter = Presenter(view)
app = App(presenter, view)
app.start()
