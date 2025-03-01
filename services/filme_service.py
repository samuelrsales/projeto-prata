import sqlite3

class Filme:
    def __init__(self, id=None, titulo=None, genero=None, ano=None, avaliacao=None, assistido=False):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.avaliacao = avaliacao
        self.assistido = assistido

    def conectar(self):
        return sqlite3.connect("database/banco_dados.db")

    def adicionar(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO filmes (titulo, genero, ano, avaliacao, assistido) VALUES (?, ?, ?, ?, ?)", 
            (self.titulo, self.genero, self.ano, self.avaliacao if self.avaliacao else None, 0))
        conexao.commit()
        conexao.close()

    def listar_filmes(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM filmes")
        filmes = cursor.fetchall()
        conexao.close()
        return [Filme(*f) for f in filmes]

    def buscar_filme(self, titulo):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM filmes WHERE titulo LIKE '%{titulo}%'")
        filmes = cursor.fetchall()
        conexao.close()
        return [Filme(*f) for f in filmes]

    def atualizar(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE filmes SET titulo='{self.titulo}', genero='{self.genero}', ano='{self.ano}' WHERE id={self.id}")
        conexao.commit()
        conexao.close()

    def excluir(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM filmes WHERE id={self.id}")
        conexao.commit()
        conexao.close()

    def marcar_como_assistido(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE filmes SET assistido=1 WHERE id={self.id}")
        conexao.commit()
        conexao.close()

    def avaliar(self, nota):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE filmes SET avaliacao={nota} WHERE id={self.id}")
        conexao.commit()
        conexao.close()
