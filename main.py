import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DAYA;'
    'DATABASE=QRAccessControl;'
    'UID=sa;'
    'PWD=P@ssw0rd;'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sys.tables")
print("Tablas:", [row[0] for row in cursor.fetchall()])
