from loguru import logger
from prompt_toolkit.shortcuts import radiolist_dialog
from bkmk_class import Add

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def main():
    """
    Main function of the app. Where all functionalities concentrate.

    Inside the function we build the radio button questionnaire. Outside the function,
    and necessarily so, we declare the instantiation of the imported class.
    Finally we connect each radio button option to a specific method, mediated by the
    instance

    Args:
        main.result: str, Returns the key of the dictionary value that was chosen by the
                          user.
        sum: class, Variable instantiation of the Add class
        sum.add_bkmk: Instantiated class method
        sum.delete:  Instantiated class method
        sum.see:  Instantiated class method
        sum.search:  Instantiated class method
        sum.update:  Instantiated class method

    Returns:
        main.result: dict.key, User choice
        sum.see: dict, print all the database
        sum.search: dict, search results
    """
    main.result = radiolist_dialog(
        title="Main",
        text="What Do You Want To Do?",
        values=[
            ("add", "Add a Bookmark"),
            ("delete", "Delete a Bookmark"),
            ("see", "See All Bookmarks"),
            ("search", "Search the Bookmarks"),
            ("update", "Update a Bookmark"),
        ],
    ).run()


main()


sum = Add()
if main.result == "add":
    sum.add_bkmk()
if main.result == "delete":
    sum.delete()
if main.result == "see":
    sum.see()
if main.result == "search":
    sum.search()
if main.result == "update":
    sum.update()
