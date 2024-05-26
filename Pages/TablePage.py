from DatabaseConnection import DatabaseConnection
from OptionSelection import OptionSelection
from Pages.Page import Page
# List all tables including their status

db = DatabaseConnection()
class TablePage(Page):
    def display(login_manager):
        tables = db.getTableData("tables")
        table_names = [table["id"] for table in tables]
        OptionSelection.show(table_names, "Pick a table number:")
