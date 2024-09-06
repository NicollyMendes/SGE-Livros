import sqlite3

#Conectar ao bando de dados/ ou criar um novo banco de dados  
conexao = sqlite3.connect('dados.db')
#Criar tabela de Livros
conexao.execute('CREATE TABLE Livros(\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_de_publicacao INTEGER,\
                isbn TEXT)') 
#Criar tabela de usuarios
conexao.execute('CREATE TABLE Usuarios(\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                num_telefone TEXT)')
#Criar tabela de empréstimos
conexao.execute('CREATE TABLE Emprestimos(\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES Livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES Usuarios(id))')