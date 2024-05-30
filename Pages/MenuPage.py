# Print menu items
from DatabaseConnection import DatabaseConnection
from MainClasses.MenuItem import MenuItem
from Managers.LoginManager import LoginManager
from Pages.Page import Page

db = DatabaseConnection()


class MenuPage(Page):
    @staticmethod
    def display(login_manager: LoginManager) -> bool:
        menu_dict = db.getTableData("menu")
        menu_items = [
            MenuItem(item["id"], item["name"], item["price"]) for item in menu_dict
        ]

        MenuPage.printMenu(menu_items)
        while True:
            user_input = input("Enter q to exit: ")
            if user_input == "q":
                return True

    @staticmethod
    def printMenu(menu_items):
        print("------------Menu------------")

        # Get the maximum width of each column
        max_id_width = max(len(str(item.getId())) for item in menu_items)
        max_name_width = max(len(item.getName()) for item in menu_items)
        max_price_width = max(len(str(item.getPrice())) for item in menu_items)

        # Print the table header
        header = f"| {'ID':<{max_id_width}} | {'Name':<{max_name_width}} | {'Price':<{max_price_width}} |"
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # Print each menu item
        for item in menu_items:
            id_str = str(item.getId()).ljust(max_id_width)
            name_str = item.getName().ljust(max_name_width)
            price_str = str(item.getPrice()).ljust(max_price_width)
            print(f"| {id_str} | {name_str} | {price_str} |")

        # Print the bottom border
        print("-" * len(header))
