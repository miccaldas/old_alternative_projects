"""Module Docstring"""
from loguru import logger
from pysqlcipher3 import dbapi2 as sqlcipher

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)

db = sqlcipher.connect("test.db")


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def function():
    """
    One Liner

    Args:
        name: description

    Returns:
        name, type, semantics

    Raises:
        Name: Error Message
    """
    db.execute('pragma key="testing"')
    db.execute("select * from people;").fetchall()


function()
