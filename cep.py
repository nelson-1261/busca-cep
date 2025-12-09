import requests 

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    return requests.get(url).json()   

cep = input("Digite o CEP:")
endereco = buscar_cep(cep)

print("CEP:", endereco["cep"])
print("Logradouro:", endereco["logradouro"])
print("Complemento:", endereco["complemento"])
print("Bairro:", endereco["bairro"])
print("Localidade:", endereco["localidade"])
print("UF:", endereco["uf"])



