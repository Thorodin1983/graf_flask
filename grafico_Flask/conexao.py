# conexao.py
import pyodbc

def create_connection():
    try:
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                              'Server=<servidor>;'
                              'Database=<db>;'
                              'UID=<user>;'
                              'PWD=<psw>;')
        print("Conexão bem-sucedida!")
        return conn
    except Exception as e:
        print("Erro ao conectar:", e)
        return None
