"""A rethink of my password app. Added hashes to the mix"""
import random
from loguru import logger
import hashlib
import sqlite3

fmt = "{time} - {name} - {level} - {message}"
logger.add("info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch
def info():
    """All information but the password"""

    info.service = input("What is the service? ")
    info.username = input("What is the email/username? ")
    info.string = input("Choose a random, long, string ")
    info.length = int(input("How long do you want your password to be? "))
    info.creation = input("Do you want to write your own password? [y/n] ")

    if info.creation == "y":
        info.user_pwd = input("What password do you want? ")
    else:
        info.user_pwd = 0


if __name__ == "__main__":
    info()


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def hash_string():
    """Where all the hashing operations are done"""

    string_bt = info.string.encode()
    service_bt = info.service.encode()
    concat = b"".join([string_bt, service_bt])
    h = hashlib.sha256()
    h.update(concat)
    hash_string.hex = h.hexdigest()


if __name__ == "__main__":
    hash_string()


@logger.catch
def complex():
    complex.passwd = " "
    hex = str(hash_string.hex)
    hex_list = [char for char in hex]
    alpha = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "A",
        "a",
        "B",
        "b",
        "C",
        "c",
        "D",
        "d",
        "E",
        "e",
        "F",
        "f",
        "G",
        "g",
        "H",
        "h",
        "I",
        "i",
        "J",
        "j",
        "K",
        "k",
        "L",
        "l",
        "M",
        "m",
        "N",
        "n",
        "O",
        "o",
        "P",
        "p",
        "Q",
        "q",
        "R",
        "r",
        "S",
        "s",
        "T",
        "t",
        "U",
        "u",
        "V",
        "v",
        "W",
        "w",
        "X",
        "x",
        "Y",
        "y",
        "Z",
        "z",
        "|",
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "/",
        "(",
        ")",
        "=",
        "«",
        "^",
        "<",
        ">",
        "[",
        "}",
        "+",
        "*",
        "ç",
        "`",
        "~",
        "_",
        "-",
        ".",
        ";",
        "|",
    ]

    add = random.sample(alpha, info.length)
    for i in add:
        hex_list.append(i)
    cull = hex_list[::4]
    pwd = ""
    complex.passwd = pwd.join(cull)
    print(complex.passwd)


if __name__ == "__main__":
    complex()


@logger.catch
def updt_database():
    """Updates the database"""

    try:
        conn = sqlite3.connect("new_pwd.db")
        cur = conn.cursor()
        if info.user_pwd != 0:
            complex.passwd = info.user_pwd
        answers = [info.service, info.username, info.string, complex.passwd]
        query = """INSERT INTO new_pwd (service, username, string, password) VALUES (?, ?, ?, ?)"""
        cur.execute(query, answers)
        conn.commit()
    except sqlite3.Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    updt_database()
