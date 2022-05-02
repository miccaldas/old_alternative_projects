from mysql.connector import connect, Error
from colr import color


class Bookmark:
    def __init__(self, title, comment, link, k1, k2, k3):
        self.title = title
        self.comment = comment
        self.link = link
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3

    def add(self):
        answers = [self.title, self.comment, self.link, self.k1, self.k2, self.k3]
        try:
            conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="bkmks")
            cur = conn.cursor()
            query = "INSERT INTO bkmks (title, comment, link, k1, k2, k3) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(query, answers)
            conn.commit()

        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if(conn):
                conn.close()

    def see(self):
        try:
            conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="bkmks")
            cur = conn.cursor()
            query = """ SELECT * FROM bkmks """
            cur.execute(query)
            records = cur.fetchall()
            for row in records:
                print(color(' [*] ID » ', fore='#85a585'), color(str(row[0]), fore='#fdf3d3'))   # 1
                print(color(' [*] TITLE » ', fore='#85a585'), color(str(row[1]), fore='#fdf3d3'))
                print(color(' [*] COMMENT » ', fore='#85a585'), color(str(row[2]), fore='#fdf3d3'))
                print(color(' [*] LINK ? ', fore='#85a585'), color(str(row[3]), fore='#f29b85'))
                print(color(' [*] KEYWORD 1 » ', fore='#85a585'), color(str(row[4]), fore='#fdf3d3'))
                print(color(' [*] KEYWORD 2 » ', fore='#85a585'), color(str(row[5]), fore='#fdf3d3'))
                print(color(' [*] KEYWORD 3 » ', fore='#85a585'), color(str(row[6]), fore='#fdf3d3'))
                print(color(' [*] TIME » ', fore='#85a585'), color(str(row[7]), fore='#fdf3d3'))
            print('\n')
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if(conn):
                conn.close()


new_bkmk = Bookmark('Python Objects and Classes',
                    'In this tutorial, you will learn about the core functionality of Python objects and classes.',
                    'https://www.programiz.com/python-programming/class',
                    'python',
                    'classes',
                    'oop')

# new_bkmk.add()
new_bkmk.see()
