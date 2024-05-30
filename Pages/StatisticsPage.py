from DatabaseConnection import DatabaseConnection
from Managers.LoginManager import LoginManager
from Managers.MenuManager import MenuManager
from Pages.Page import Page

db = DatabaseConnection()
menu_manager = MenuManager(db)


class StatisticsPage(Page):
    def display(login_manager: LoginManager):
        item_counts = {}
        orders = db.getTableData("orders")
        menu_manager.readItemsFromDB()
        menu = menu_manager.getAllItems()
        for order in orders:
            for item_id in order["menu_items"]:
                item_counts[item_id] = item_counts.get(item_id, 0) + 1
        # order["menu_items"][index] = next((itm for itm in menu if itm.getId() == item_id), None)
        print("Menu Item Statistics")
        for id, count in item_counts.items():
            item = menu_manager.getItem(id)
            if item:
                print(f"{item.getName()}, ${item.getPrice()} - Ordered {count} times.")
        while True:
            user_input = input("Press (q) to return: ")
            if user_input == "q":
                break
