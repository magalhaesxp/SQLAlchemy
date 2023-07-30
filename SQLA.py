from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Criar o engine e a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///banco_de_dados.db')
Base = declarative_base()

# Definir a classe Cliente
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)

    def __repr__(self):
        return f"Cliente(id={self.id}, nome='{self.nome}', endereco='{self.endereco}')"

# Definir a classe Conta
class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente", back_populates="contas")

    def __repr__(self):
        return f"Conta(id={self.id}, numero='{self.numero}', saldo={self.saldo}, cliente_id={self.cliente_id})"

# Adicionar o atributo de relacionamento na classe Cliente
Cliente.contas = relationship("Conta", order_by=Conta.id, back_populates="cliente")

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserir dados mínimos para manipulação das informações
cliente1 = Cliente(nome='João', endereco='Rua A')
cliente2 = Cliente(nome='Maria', endereco='Rua B')
cliente3 = Cliente(nome='Fernanda', endereco='Rua C')

conta1 = Conta(numero='12345', saldo=1000, cliente=cliente1)
conta2 = Conta(numero='67890', saldo=2000, cliente=cliente2)
conta3 = Conta(numero='54321', saldo=3000, cliente=cliente3)

session.add_all([cliente1, cliente2, cliente3,  conta1, conta2, conta3])
session.commit()

# Métodos de recuperação de dados
# Recuperar todos os clientes
clientes = session.query(Cliente).all()
print("Clientes:")
for cliente in clientes:
    print(cliente)

# Recuperar todas as contas
contas = session.query(Conta).all()
print("\nContas:")
for conta in contas:
    print(conta)

# Recuperar as contas de um cliente específico
cliente_id = 1
contas_cliente = session.query(Conta).filter_by(cliente_id=cliente_id).all()
print("\nContas do Cliente com ID =", cliente_id)
for conta in contas_cliente:
    print(conta)

# Fechar a sessão
session.close()
