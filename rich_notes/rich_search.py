""" Module to see all of the database """
import fire
from colr import color
from loguru import logger
from mysql.connector import Error, connect
from rich import print
from rich.panel import Panel

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/search.log", level="INFO", format=fmt)
logger.add("../logs/search.log", level="ERROR", format=fmt)


def search():
    try:
        busca = input(color(" What are you searching for? ", fore="#40afb8"))
        logger.info(busca)
        conn = connect(host="localhost", user="mic", password="xxxx", database="notes")
        cur = conn.cursor()
        query = " SELECT ntid, title, k1, k2, k3, note, url, time FROM notes WHERE MATCH(title, k1, k2, k3, note, url) AGAINST ('" + busca + "' ) ORDER BY time"
        logger.info(query)
        cur.execute(query)
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


if __name__ == "__main__":
    fire.Fire(search)
