import tkinter
from gui.modals import CreatePizzaModal
from handlers.database import get_pizza_list


class PizzaListFrame(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._label = None
        self._add_button = None
        self._pizza_list = get_pizza_list()

    def _open_new_pizza_form(self):
        self._create_pizza_modal = CreatePizzaModal(self)

    def draw(self):
        self._label = tkinter.Label(self)
        if len(self._pizza_list) == 0:
            self._label.config(text='No pizza available.')
        else:
            self._label.config(text=f'You have a total of {len(self._pizza_list)} pizza.')
        self._label.pack(side=tkinter.TOP)

        for pizza in self._pizza_list:
            label = tkinter.Label(self, text=pizza.name)
            label.pack(side=tkinter.TOP)

        self._add_button = tkinter.Button(self, text='Add new pizza', command=self._open_new_pizza_form)
        self._add_button.pack(side=tkinter.TOP)

    def add_new_pizza(self, name):
        self._add_button.pack_forget()

        label = tkinter.Label(self, text=name)
        label.pack(side=tkinter.TOP)

        self._add_button.pack(side=tkinter.TOP)
