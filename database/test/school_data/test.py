import mysql.connector

Test_Db = mysql.connector.Connect(
    host = "localhost",
    user = "Vasu",
    auth_plugin = "mysql_native_password",
    passwd = "V@$u47WithSQLPython"
)
