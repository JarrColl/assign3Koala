from DatabaseConnection import DatabaseConnection
from Managers.TableManager import TableManager
from OptionSelection import OptionSelection
from Pages.Page import Page
# List all tables including their status

db = DatabaseConnection()
table_manager = TableManager(db)
class TablePage(Page):
    def display(login_manager):
        table_manager.readItemsFromDB()
        tables = table_manager.getTables()
        table_numbers = [table.getId() for table in tables]
        OptionSelection.show(table_numbers, "Pick a table number:")
