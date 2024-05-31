from DatabaseConnection import DatabaseConnection
from Managers.LoginManager import LoginManager
from Managers.TableManager import TableManager
from OptionSelection import OptionSelection
from Pages.Page import Page

# List all tables including their status

db = DatabaseConnection()
table_manager = TableManager(db)


class TablePage(Page):
    @staticmethod
    def display(login_manager: LoginManager) -> bool:
        table_manager.readItemsFromDB()
        tables = table_manager.getTables()
        print("| id | status |")
        for table in tables:
            print("| " + str(table.getId()) + " | " + table.getStatus() + " |")

        while True:
            value = input("Press 'q' to return: ")
            if value == "q":
                break
        return True
