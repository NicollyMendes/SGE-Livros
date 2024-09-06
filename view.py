import sqlite3

#Conectar ao bando de dados
#Função criada para conexao ao banco 
def connect():
    conexao = sqlite3.connect('dados.db')
    return conexao

#Função para inserir um novo livro na tabela Livros
def insert_book(titulo, autor, editora, ano_de_publicacao, isbn):
    conexao = connect()
    conexao.execute("INSERT INTO Livros(titulo, autor, editora, ano_de_publicacao, isbn)\
                     VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_de_publicacao, isbn))
    conexao.commit()
    conexao.close()

#Funcao para inserir usuarios
def insert_user(nome, sobrenome, endereco, email, num_telefone):
    conexao = connect()
    conexao.execute("INSERT INTO Usuarios(nome, sobrenome, endereco, email, num_telefone)\
                     VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, num_telefone))
    conexao.commit()
    conexao.close()

# Função para exibir os usuarios
def get_users():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT * FROM Usuarios") 
    users = c.fetchall()
    conexao.close()
    return users 
# Funcao para exibir os livros
def exibir_livros():
    conexao = connect()
    Livros = conexao.execute("SELECT * FROM Livros").fetchall()
    conexao.close()

    return Livros



# Função para realizar empréstimos
def insert_loan(id_usuario, id_livro, data_emprestimo, data_devolucao):
    conexao = connect()
    conexao.execute("INSERT INTO Emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                    VALUES(?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conexao.commit()
    conexao.close()

#Funcao para exibir todos os livros emprestados no momento

def get_books_on_loan():
    conexao = connect()
    resultado = conexao.execute("SELECT Emprestimos.id, Livros.titulo, Usuarios.nome, Usuarios.sobrenome, Emprestimos.data_emprestimo,Emprestimos.data_devolucao\
                                FROM Livros\
                                INNER JOIN Emprestimos ON Livros.id = Emprestimos.id_livro\
                                INNER JOIN Usuarios ON Usuarios.id = Emprestimos.id_usuario\
                                WHERE Emprestimos.data_devolucao IS NULL").fetchall() #Juntando os campos id(Livros) com id_livro(Emprestimos), e tambem id(Usuarios) 
#com id_usuario(Emprestimos), onde se a data de devolucao do livro estiver vazia significa que ele ainda nao foi devolvido
    conexao.close()
    return resultado 



#Função para atualizar a data de devolucao do emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conexao = connect()
    conexao.execute("UPDATE Emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conexao.commit()
    conexao.close()



