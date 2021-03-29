import os

class UIMenu:
    def __init__(self):
        self.draw_menu()

    def draw_menu(self):
        print("🚀 xlsx to JSON converter")
        file = input("Ingrese el archivo: ")
        full_path = os.path.abspath(file)
        print(full_path)
