# Thomas' ***VERSITILE MENU SYSTEM***
import json


class Menu:
    def __init__(self, path):
        with open(path, "r") as f:
            dat = json.load(f)

        self.question = dat["question"]
        self.me = dat["me"]
        self.can_return = dat["canreturn"]
        self.return_to = dat["returnto"]
        self.options = dat["options"]

        to_return_int = []
        to_return = []
        for i, _ in enumerate(self.options):
            to_return_int.append(i + 1)
        for x in to_return_int:
            to_return.append(str(x))
        self.accepted = to_return

    def display(self):
        print("=" * 20)
        while True:

            print(self.question)
            for i, x in enumerate(self.options):
                print(i + 1, ": ", x["text"])

            if self.can_return:
                print("b :  Back")

            a = input(": ")

            if a in self.accepted:
                break

            if a == "b" and self.can_return:
                break

            print("That answer was invalid. Please try again.")

        if a == "b":
            return start_menu(self.return_to)

        continue_on = True

        if self.options[int(a) - 1]["askyesno"]:
            while True:
                answer = input("Are you sure you want to do this?\n(y/n): ")
                if answer == "y" or answer == "n":
                    break
                print("Please answer with y or n.")

            if answer == "n":
                continue_on = False

        if continue_on:
            command = self.options[int(a) - 1]["command"]
            if command["type"] == "return":
                return command["value"]
            if command["type"] == "menu":
                return start_menu(command["value"])
        else:
            return start_menu(self.me)


def start_menu(menu_name):
    menu_obj = Menu("menus/" + menu_name + ".json")
    return menu_obj.display()
