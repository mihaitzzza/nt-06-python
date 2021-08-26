import tkinter
from handlers.database import create_pizza


class CreatePizzaModal:
    def __init__(self, parent_frame):
        self._parent_frame = parent_frame

        self._top_level = tkinter.Toplevel(parent_frame)
        self._top_level.transient(parent_frame)
        self._top_level.geometry('500x600')

        self._label = tkinter.Label(self._top_level, text='Add new pizza form')
        self._label.pack(side=tkinter.TOP)

        self._name = tkinter.Label(self._top_level, text='Name')
        self._name.pack(side=tkinter.TOP)

        self._name_entry = tkinter.Entry(self._top_level)
        self._name_entry.pack(side=tkinter.TOP)

        self._btn = tkinter.Button(self._top_level, text='Add', command=self._create_pizza)
        self._btn.pack(side=tkinter.BOTTOM)

    def _create_pizza(self):
        pizza_name = self._name_entry.get()
        error = create_pizza(pizza_name)

        if error is None:
            self._top_level.destroy()
            self._parent_frame.add_new_pizza(pizza_name)
        else:
            # solve the error if anything happens :)
            pass
