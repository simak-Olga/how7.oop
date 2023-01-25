class Calculator:
    def __init__(self, parent, x, y):
        self.button_font = ('Verdana', 15)
        self.entry_font = ('Verdana', 20)
        self.parent = parent

        self.button_width = 4
        self.button_height = 1
        self.container = Frame(self.parent)
        self.container.grid(row=x, column=y)

        self.string = ''

        def button_eq(self, char_, x_, y_):
        self.b = Button(
            self.container, text= char_, width=self.button_width,
            height=self.button_height, font=self.entry_font)
        self.b.grid(row= x_, column= y_, sticky='we', columnspan=2)
