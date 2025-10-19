import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="Luderia",
            user="postgres",
            password=os.getenv("PASSWORD"),
            port="5432") # Cria nova sessão de base de dados e retorna uma instancia de conexão
        
        print("Connection successful!")
        
        return conn
    
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")


conn = connect_db()
cur = conn.cursor() # permite interagir com a base de dados

#inicia_dados(os.getenv('PATH_DADOS_BASE'))

#cur.execute("SELECT * FROM cliente")
#print(cur.fetchmany())

'''
cur.execute("DROP TABLE test")
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

cur.execute("SELECT * FROM cliente")
print(cur.fetchmany())
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
'''

cur.close()
conn.close()