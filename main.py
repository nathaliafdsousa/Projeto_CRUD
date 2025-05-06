#
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crud import CRUD
from relacoes import Livro

# Carrega variáveis do ficheiro .env
load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# Conexão com SQL Server 
url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

# Instancia a classe CRUD
livro_crud = CRUD(session)

try:
    # Livro válido
    try:
        livro_crud.create("9788521630814", "Introdução à Computação Usando Python", "PERKOVIC, L.", 2016, "Programação")
        print("Livro Introdução à Computação Usando Python criado com sucesso.")
    except Exception as e:
        print("Erro ao criar livro Introdução à Computação Usando Python:", e)

    # Livro com ano inválido (-500)
    try:
        livro_crud.create("9780140439199", "A Arte da Guerra", "Sun Tzu", -500, "Não ficção")
    except Exception as e:
        print("Erro ao criar livro A Arte da Guerra (ano inválido):", e)

    # Livro válido
    try:
        livro_crud.create("9788474261448", "Feliz Ano Velho", "Marcelo Rubens Paiva", 1982, "Auto Biografia")
        print("Livro Feliz Ano Velho criado com sucesso.")
    except Exception as e:
        print("Erro ao criar livro Feliz Ano Velho:", e)

    # Livro válido
    try:
        livro_crud.create("9780192823786", "As aventuras de Sherlock Holmes", "Arthur Conan Doyle", 1892, "ficção policial")
        print("Livro As Aventuras de Sherlock Holmes criado com sucesso.")
    except Exception as e:
        print("Erro ao criar livro As Aventuras de Sherlock Holmes:", e)

    # Livro com ano inválido (0)
    try:
        livro_crud.create("9786555876475", "A Natureza da Mordida", "Carla Madeira", 0, "Romance")
    except Exception as e:
        print("Erro ao criar livro A Natureza da Mordida (ano inválido):", e)

    # Leitura de livro existente
    livro = livro_crud.read("9788474261448")
    if livro:
        print("Livro encontrado:", livro.titulo)
    else:
        print("Livro não encontrado.")
    
    livro = livro.crud.read("9788474261448")
    if livro:
        print("Livro encontrado:, livro.titulo")
    else:
        print("Livro não encontrado")
    # Atualização de livro existente
    livro_crud.update("9788521630814", titulo="Introdução à Computação Usando Python - Atualizado", ano_publicacao=2021)

    # Exclusão do livro
    livro_crud.delete("9788521630814")

except Exception as e:
    print("Erro geral:", e)

finally:
    session.close()


