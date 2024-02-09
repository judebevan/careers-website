# from sqlalchemy import create_engine, text
import mysql.connector
from mysql.connector import Error

hostname = "l4k.h.filess.io"
database = "JDgroups_frogfourth"
port = "3307"
username = "JDgroups_frogfourth"
password = "9c853f9c88ccc3531600c33e10a5733000558547"

try:
  connection = mysql.connector.connect(host=hostname,
                                       database=database,
                                       user=username,
                                       password=password,
                                       port=port)
  if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select * from jobs")
    records = cursor.fetchall()
    print(type(records))
    for record in records:
      print(record)
    cursor.close()
    # record = cursor.fetchone()
    print("You're connected to database: ", record)

except Error as e:
  print("Error while connecting to MySQL", e)
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

# db_connection_string = "mysql+pymysql://JDgroups_frogfourth:@l4k.h.filess.io/JDgroups_frogfourth?charset=utf8mb4"

# engine = create_engine(
#   db_connection_string)

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   print(result.all())
