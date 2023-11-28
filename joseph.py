import random

class Pessoa:
    def __init__(self, numero, nome, telefone, endereco, cpf):
        self.numero = numero
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf

def preencher_pessoas():
    # Gera dados fictícios para preencher as pessoas
    nomes = ["Ana", "Carlos", "Maria", "João", "Paula", "Pedro", "Luis", "Fernanda", "Mariana", "Ricardo",
             "Camila", "Gabriel", "Juliana", "Felipe", "Isabela", "Lucas", "Renata", "Thiago", "Vanessa", "Eduardo"]

    telefones = ["111-1111", "222-2222", "333-3333", "444-4444", "555-5555", "666-6666", "777-7777", "888-8888", "999-9999", "000-0000",
                 "123-4567", "234-5678", "345-6789", "456-7890", "567-8901", "678-9012", "789-0123", "890-1234", "901-2345", "012-3456"]

    enderecos = ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E", "Rua F", "Rua G", "Rua H", "Rua I", "Rua J",
                 "Av. X", "Av. Y", "Av. Z", "Travessa 1", "Travessa 2", "Travessa 3", "Praça Central", "Alameda Principal", "Avenida Principal", "Estrada Principal"]

    cpfs = [f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}" for _ in range(20)]

    # Cria uma lista de objetos Pessoa com dados aleatórios
    pessoas = [Pessoa(numero, nomes[numero - 1], telefones[numero - 1], enderecos[numero - 1], cpfs[numero - 1]) for numero in range(1, 21)]

    return pessoas

def josephus_pessoas(pessoas):
    eliminadas = []

    # Enquanto houver mais de uma pessoa na lista
    while len(pessoas) > 1:
        # Escolhe aleatoriamente a pessoa a ser removida
        indice_remocao = random.randint(0, len(pessoas) - 1)
        pessoa_removida = pessoas.pop(indice_remocao)
        eliminadas.append(pessoa_removida)

    return eliminadas

# Preenche as pessoas
lista_de_pessoas = preencher_pessoas()

# Executa o algoritmo de Josephus
pessoas_eliminadas = josephus_pessoas(lista_de_pessoas)

# Exibe os dados das pessoas eliminadas
for pessoa in pessoas_eliminadas[:-1]:
    print(f"Pessoa eliminada - Numero: {pessoa.numero}, Nome: {pessoa.nome}, Telefone: {pessoa.telefone}, Endereco: {pessoa.endereco}, CPF: {pessoa.cpf}")

# Exibe a última pessoa sobrevivente
pessoa_sobrevivente = pessoas_eliminadas[-1]
print(f"\nPessoa sobrevivente - Numero: {pessoa_sobrevivente.numero}, Nome: {pessoa_sobrevivente.nome}, Telefone: {pessoa_sobrevivente.telefone}, Endereco: {pessoa_sobrevivente.endereco}, CPF: {pessoa_sobrevivente.cpf}")
