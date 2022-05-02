# IMPORTANT! - You must be in your project directory when filling this file.
# Here you may define the columns, and their atributes, that you want. If you need more than the spaces available, just copy/paste an entry and change its numbers.
# Tuesday Jan 19, 2021 13:36:19 WETfrom icecream import ic
from icecream import ic


class Basededados:
    """ This class will handle the definition of the database configuration, and text prepping to turn it into a SQLite query. """

    def __init__(self):
        self.key0 = 'id'
        self.spec1 = 'INTEGER'
        self.spec2 = 'NOT NULL'
        self.spec3 = 'PRIMARY KEY'
        self.key1 = 'title'
        self.spec4 = 'TEXT'
        # self.spec5 =
        # self.spec6 =
        self.key2 = 'comment'
        self.spec7 = 'TEXT'
        # self.spec8 =
        # self.spec9 =
        self.key3 = 'link'
        self.spec10 = 'TEXT'
        # self.spec11 =
        # self.spec12 =
        self.key4 = 'k1'
        self.spec13 = 'TEXT'
        # self.spec14 =
        # self.spec15 =
        self.key5 = 'k2'
        self.spec16 = 'TEXT'
        # self.spec17 =
        # self.spec18 =
        self.key6 = 'k3'
        self.spec19 = 'TEXT'
        # self.spec20 =
        # self.spec21 =
        self.key7 = 'time'
        self.spec22 = 'DATETIME'
        self.spec23 = 'DEFAULT'
        self.spec24 = 'CURRENT_TIMESTAMP'
        # self.key8 =
        # self.spec25 =
        # self.spec26 =
        # self.spec27 =
        self.table_name = 'teste1'

    def column_specs(self):
        """ Defines the columns names and specifications for the sqlite database. """
        a = {}
        # Column 0
        key = self.key0
        a.setdefault(key, [])
        a[key].append(self.spec1)
        a[key].append(self.spec2)
        a[key].append(self.spec3)

        # Column 1
        key = self.key1
        a.setdefault(key, [])
        a[key].append(self.spec4)
        # a[key].append(self.spec5)
        # a[key].append(self.spec6)

        # Column 2
        key = self.key2
        a.setdefault(key, [])
        a[key].append(self.spec7)
        # a[key].append(self.spec8)
        # a[key].append(self.spec9)

        # Column 3
        key = self.key3
        a.setdefault(key, [])
        a[key].append(self.spec10)
        # a[key].append(self.spec11)
        # a[key].append(self.spec12)

        # Column 4
        key = self.key4
        a.setdefault(key, [])
        a[key].append(self.spec13)
        # a[key].append(self.spec14)
        # a[key].append(self.spec15)

        # Column 5
        key = self.key5
        a.setdefault(key, [])
        a[key].append(self.spec16)
        # a[key].append(self.spec17)
        # a[key].append(self.spec18)

        # Column 6
        key = self.key6
        a.setdefault(key, [])
        a[key].append(self.spec19)
        # a[key].append(self.spec20)
        # a[key].append(self.spec21)

        # Column 7
        key = self.key7
        a.setdefault(key, [])
        a[key].append(self.spec22)
        a[key].append(self.spec23)
        a[key].append(self.spec24)

        # Column 8
        # key = self.key8
        # a.setdefault(key, [])
        # a[key].append(self.spec25)
        # a[key].append(self.spec26)
        # a[key].append(self.spec27)

        # print(a)

    def creating_the_db(self):
        import sqlite3

        try:
            conn = sqlite3.connect(self.table_name)
            cur = conn.cursor()
            ic("Database created and Successfully Connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cur.execute(sqlite_select_Query)
            record = cur.fetchall()
            ic("SQLite Database Version is: ", record)
            conn.commit()
        except sqlite3.Error as e:
            ic("Error while connecting to db", e)
        finally:
            if(conn):
                conn.close()

    def envio_de_query(self):
        import sqlite3

        questao = 'CREATE TABLE ' + self.table_name + ' (' + self.key0 + ' ' + self.spec1 + ' ' + self.spec2 + ' ' + self.spec3 + ', ' \
            + self.key1 + ' ' + self.spec4 + ', ' + self.key2 + ' ' + self.spec7 + ', ' + self.key3 + ' ' + self.spec10 + ', ' \
            + self.key4 + ' ' + self.spec13 + ', ' + self.key5 + ' ' + self.spec16 + ', ' + self.key6 + ' ' + self.spec19 + ', ' \
            + self.key7 + ' ' + self.spec22 + ' ' + self.spec23 + ' ' + self.spec24 + ')'
        # print(questao)
        try:
            conn = sqlite3.connect(self.table_name)
            cur = conn.cursor()
            query = questao
            cur.execute(query,)
            conn.commit()
        except sqlite3.Error as e:
            print("Error while connecting to db", e)
        finally:
            if(conn):
                conn.close()


a = Basededados()
# dictionary_data = a.column_specs()
create_db = a.creating_the_db()
# emission = a.envio_de_query()
# a.creating_the_db()
