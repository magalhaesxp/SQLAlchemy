import pymongo as pyM

# Conectar ao banco de dados do MongoDB no Atlas
# Substitua "SEU_CONNECTION_STRING" pela sua string de conexão do MongoDB
client = pyM.MongoClient(
    "mongodb+srv://magalhaesxp:040482@cluster1.lax0fhp.mongodb.net/?retryWrites=true&w=majority")

# Criar um banco de dados chamado "banco_dados_nosql"
db = client.banco_dados_nosql

# Definir uma coleção chamada "bank" para armazenar os documentos dos clientes
collection = db.bank

# Inserir documentos com a estrutura mencionada (dados de exemplo)
documento1 = {
    "cliente": {
        "id": 1,
        "nome": "João",
        "endereco": "Rua A"
    },
    "contas": [
        {
            "numero": "12345",
            "saldo": 1000
        },
        {
            "numero": "67890",
            "saldo": 2000
        }
    ]
}

documento2 = {
    "cliente": {
        "id": 2,
        "nome": "Maria",
        "endereco": "Rua B"
    },
    "contas": [
        {
            "numero": "54321",
            "saldo": 1500
        }
    ]
}

# Inserir os documentos na coleção
collection.insert_many([documento1, documento2])

# Instruções de recuperação de informações com base nos pares de chave e valor

# Recuperar todos os documentos da coleção "bank"
todos_documentos = collection.find()
print("Todos os documentos:")
for documento in todos_documentos:
    print(documento)

# Recuperar documentos com base no nome do cliente (chave: "cliente.nome")
nome_cliente = "João"
documentos_cliente = collection.find({"cliente.nome": nome_cliente})
print("\nDocumentos do cliente com nome =", nome_cliente)
for documento in documentos_cliente:
    print(documento)

# Recuperar documentos com base no número da conta (chave: "contas.numero")
numero_conta = "12345"
documentos_conta = collection.find({"contas.numero": numero_conta})
print("\nDocumentos com o número de conta =", numero_conta)
for documento in documentos_conta:
    print(documento)

# Fechar a conexão com o banco de dados
client.close()
