from utils import Utils
from cryptography.fernet import Fernet

def encripta(valores:dict, caminho: str):
    try:
        chave = Fernet.generate_key()
        f = Fernet(chave)
        valores = list(valores.values())
        user = f.encrypt(valores[0].encode())
        password = f.encrypt(valores[1].encode())

        arq = open(caminho, "w")
        arq.write(f'Chave: ' + str(chave) + '\nUser: ' + str(user) + '\nPassword: ' + str(password))
        return True
    except Exception as e:
        msg = 'Erro ao criptografar dados.'
        print(msg)
        return False
