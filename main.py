import mysql.connector
import xlrd
conn = mysql.connector.connect(user='admin', password='admin', host='65.52.178.181', port=3306, database='tanner',
                               auth_plugin='mysql_native_password')
cur = conn.cursor()

loc = "C:\\Users\\pc\\PycharmProjects\\test.xlsx"

list = list()

file = xlrd.open_workbook(loc)

sheet = file.sheet_by_name('Sheet1')
sheet.cell_value(0, 0)

print(sheet._dimnrows)
rows = sheet._dimnrows


for i in range(1, rows):
    list.append(tuple(sheet.row_values(i)))

print(list)
q = "insert into bucket(id, panel_id, title)values (%s,%s,%s)"

cur.executemany(q, list)
conn.commit()
conn.close()
