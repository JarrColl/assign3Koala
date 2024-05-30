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
        table_numbers = [
            "| " + str(table.getId()) + " | " + table.getStatus() + " |"
            for table in tables
        ]
        OptionSelection.show(table_numbers, "Pick a table number:")
        return True
