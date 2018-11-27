from include.menu_button import MenuButton


class Menu:
    def __init__(self, id_):
        """
        Initialises the Menu class

        params:
            id: the id for the menu, so i can find it
        """
        self.buttons = []

    def add_button(self, button: MenuButton):
        assert isinstance(
            button, MenuButton
        ), "cannot add a non MenuButton object to the buttons of the menu"
