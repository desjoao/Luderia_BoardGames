import psycopg2 as pg2

def conecta():
    try:
        conn = psycopg2.connect(
                host = 'localhost',
                database = 'Luderia',
                user = 'usuario',
                password = 'senha'
                )
        print('conexão estabelecida.')
    except psycopg2.Error as e:
        print('Erro ao conectar com o PostgreSQL')

