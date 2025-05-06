from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Livro(Base):
    __tablename__ = 'livros'

    isbn = Column(String, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
