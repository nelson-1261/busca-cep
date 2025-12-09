import requests
import mysql.connector 

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    endereco = requests.get(url).json()

    inserir_endereco(endereco)

def inserir_endereco(endereco):
    conexao_bd = mysql.connector.connect(host="localhost", database="cep", user="root", password='xxxx')
    cursor=conexao_bd.cursor()

    complemento = getattr(endereco, 'complemento', '')

    query= (f"insert into cep (cep, logradouro, numero, complemento, bairro, localidade, uf) "
           f"values ({endereco["cep"]}, '{endereco["logradouro"]}', '{endereco["unidade"]}', "
           f"'{endereco["complemento"]}', '{endereco["bairro"]}', '{endereco["localidade"]}', " 
           f"'{endereco["uf"]}')")
    
    cursor.execute(query)
    conexao_bd.commit()

    print("CEP:", endereco["cep"])
    print("Logradouro:", endereco["logradouro"])
    print("Complemento:", endereco["complemento"])
    print("Número:", endereco["unidade"])
    print("Bairro:", endereco["bairro"])
    print("Localidade:", endereco["localidade"])
    print("UF:", endereco["uf"])

    cursor.close()
    conexao_bd.close()

cep = input("Digite o CEP:")
endereco = buscar_cep(cep)