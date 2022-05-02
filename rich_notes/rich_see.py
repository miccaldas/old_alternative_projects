""" Module that prints the content of the databse."""
from loguru import logger
from mysql.connector import Error, connect
from rich import print
from rich.console import Console
from rich.panel import Panel

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/see.log", level="INFO", format=fmt)
logger.add("../logs/see.log", level="ERROR", format=fmt)

console = Console()


@logger.catch
def see():
    """Connect to db, get all the lines and present it with colr."""
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
        cur = conn.cursor()
        query = "SELECT * FROM notes"
        cur.execute(
            query,
        )
        records = cur.fetchall()

        for row in records:
            id = str(row[0])  # noqa: F841
            tit = row[1]  # noqa: F841
            k1 = row[2]  # noqa: F841
            k2 = row[3]  # noqa: F841
            k3 = row[4]  # noqa: F841
            nota = row[5]  # noqa: F841
            url = row[6]  # noqa: F841
            time = row[7]  # noqa: F841
            print(
                Panel(
                    f"[#d97c70]{tit}[/#d97c70]\n[#f9c586]#{k1}, #{k2}, #{k3}[/#f9c586]\n[#849590]{nota}[/#849590]\n",
                    title=f"[#a1c690]{id}[/#a1c690]",
                    subtitle=f"[#a1c690]{time}[/#a1c690]",
                )
            )
            print("\n")

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    see()
