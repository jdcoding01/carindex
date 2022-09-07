import sqlite3
from sqlite3 import Error
import os.path
from datetime import date
import json
import locale

class DatabaseManager:
    def __init__(self, module):
        self.module = module

    def init(self):

        # Verify if database exists for specified module
        if os.path.exists("../databases/{}/{}_database.db".format(self.module, self.module)) is True:
            pass
        else:
            print(os.path.exists(
                "../databases/{}/{}_database.db".format(self.module, self.module)))
            # create a database connection
            conn = self.create_connection()

            # create tables
            if conn is not None:
                # create table
                with open('../databases/{}/{}.sql'.format(self.module, self.module), 'r') as table_config:
                    sql = table_config.read()
                    self.create_table(conn, sql)
                    table_config.close()

            else:
                print("Error! cannot create the database connection.")

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(
                "./databases/{}/{}_database.db".format(self.module, self.module))
        except Error as e:
            conn = sqlite3.connect(
                "../databases/{}/{}_database.db".format(self.module, self.module))
            return conn
        return conn

    def create_table(self, create_table_sql):
        conn = self.create_connection()
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    # Inserts item data into database through the record_availability parent method
    def insert_data(self, uid, marca, modelo, year, available_timestamp, precio):
        conn = self.create_connection()

        sql = """ INSERT INTO {}_preferences(uid, marca, modelo, year, available_timestamp, precio)
              VALUES(?,?,?,?,?,?) """.format(
            self.module
        )
        cur = conn.cursor()
        data_to_insert = (uid, marca, modelo, year, available_timestamp, precio)
        cur.execute(sql, data_to_insert)
        conn.commit()

        return cur.lastrowid

    def select_all_items(self):
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM {}_preferences".format(self.module))

        rows = cur.fetchall()

        return rows


    def count_make(self):
        conn = self.create_connection()
        cur = conn.cursor()

        cur.execute(
            """SELECT marca, COUNT(*) FROM {}_preferences GROUP BY marca HAVING count(*) > 1 """.format(self.module))

        rows = cur.fetchall()

        return rows

    def count_price(self, marca):
        conn = self.create_connection()
        cur = conn.cursor()


        cur.execute(
            """SELECT precio FROM {}_preferences WHERE marca = '{}'""".format(self.module, marca))

        rows = cur.fetchall()

        return rows

    def update_item(self, item_id):
        conn = self.create_connection()

        sql = ''' UPDATE {}_preferences
              SET unavailable_timestamp = ?
              WHERE url = ? AND unavailable_timestamp = ?'''.format(self.module)
        cur = conn.cursor()
        try:
            args = (date.today(), item_id, "null")
            cur.execute(sql, args)
            conn.commit()
        except sqlite3.ProgrammingError as e:
            print("[DatabaseManager]: update_item failed: {}".format(e))

    def add_column(self, name, type):
        conn = self.create_connection()

        sql = """ ALTER TABLE {}_preferences ADD COLUMN {} {}""".format(
            self.module, name, type
        )
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        return cur.lastrowid



months = [
    "",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dic"
]

# labels = DatabaseManager("encuentra24").count_make()
# marcas = []


# labels.sort(key = lambda labels: labels[1], reverse= True)

# for item in labels:
#     marcas.append(item[0])

# print(labels)





# precios = DatabaseManager("encuentra24").count_price("BMW")
# ds = []
# for item in precios:
#     item = item[0]


#     locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
#     n = locale.atoi(item.split("B/.")[1])
#     ds.append(n)


# from statistics import mean 

# inp_lst = ds
# list_avg = mean(inp_lst) 

# numbers = "{:,}".format(int(str(round(list_avg,3)).split(".")[0]))
# print("B/.{}".format(numbers))

# index = 0
# labels = []

# dt = DatabaseManager("supercasas").select_all_items()
# for item in dt:
#     try:
#         labels.append("{} {} - {} {}".format(months[int(dt[index][2].split('-')[1])], str(dt[index][2]).split(
#             '-')[2], months[int(dt[index + 1][2].split('-')[1])], str(dt[index + 1][2]).split('-')[2]))
#         index += 2
#     except IndexError:
#         pass


# data = {
#     "labels": labels,
#     "datasets": sectoresdata_parsed
# }

# with open("../sites/{}/analytics.json".format("supercasas"), "w+") as config:
#     config.write(json.dumps(data))
#     config.close()
