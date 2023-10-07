import pyodbc

SERVER = """MINHLIEN\SQLEXPRESS"""

connectionString = f"""DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER}"""
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()
cursor.execute("""SELECT @@version""")
conn.close()
db_version = cursor.fetchone()
print("Bạn đang dùng hệ quản trị CSDL SQL server phiên bản ", db_version)