from sqlalchemy.exc import IntegrityError

from relacoes import Livro

class CRUD:
    def __init__(self, session):
        self.session = session

    def create(self, isbn, titulo, autor, ano_publicacao, genero):
        try:
            novo_livro = Livro(
                isbn=isbn,
                titulo=titulo,
                autor=autor,
                ano_publicacao=ano_publicacao,
                genero=genero
            )
            self.session.add(novo_livro)
            self.session.commit()
            print(f"Livro '{titulo}' criado com sucesso.")
        except IntegrityError as e:
            self.session.rollback()
            print(f"Erro de integridade ao criar o livro '{titulo}':", e)
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao criar o livro '{titulo}':", e)

    def read(self, isbn):
        return self.session.query(Livro).filter_by(isbn=isbn).first()

    def update(self, isbn, **kwargs):
        livro = self.read(isbn)
        if livro:
            for key, value in kwargs.items():
                setattr(livro, key, value)
            self.session.commit()
            print(f"Livro '{isbn}' atualizado com sucesso.")
        else:
            print(f"Livro '{isbn}' não encontrado para atualização.")

    def delete(self, isbn):
        livro = self.read(isbn)
        if livro:
            self.session.delete(livro)
            self.session.commit()
            print(f"Livro '{isbn}' excluído com sucesso.")
        else:
            print(f"Livro '{isbn}' não encontrado para exclusão.")


