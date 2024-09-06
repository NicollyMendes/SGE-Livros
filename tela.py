#CRIACAO DA INTERFACE GRÁFICA
from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from  tkinter import messagebox
from datetime import date
from datetime import datetime

# importando as funções da view
from view import *

hoje = date.today()

# CORES
co0 = "#2e2d2b" #Preta
co1 = "#feffff" #Branca
co2 = "#4fa882" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra
co5 = "#e06636" # - profit
co6 = "#E9A178"
co7 = "#3fbfb9" #Verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = "#6e8faf"
co11 = "#f2f4f2"

#Criando janela  ------
janela = Tk()
janela.title('')
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

#Frames ------
frameCima = Frame(janela, width=770, height=50, background=co6, relief='flat')
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsq = Frame(janela, width=150, height=265, background=co4, relief='solid')
frameEsq.grid(row=1, column=0, sticky=NSEW)

frameDir = Frame(janela, width=600, height=265, background=co1, relief='raised')
frameDir.grid(row=1, column=1, sticky=NSEW)

#Logo ----------
#abrindo a imagem
app_img = Image.open('livrosicon.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6,fg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW,font=('Verdana 15 bold'),bg=co6, fg=co1)
app_.place(x=50, y=7)

app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
app_linha.place(x=0, y=47)


# novo usuario
def novo_usuario():
    global img_salvar


    #funcao para salvar as informações preenchidas pelos usuarios
    def add():
        p_nome = e_p_nome.get()
        sobrenome = e_sobrenome.get()
        endereco = e_endereco.get()
        email = e_email.get()
        telefone = e_telefone.get()

        lista = [p_nome, sobrenome, endereco, email, telefone]

        #verificando se há algum campo nao preenchido
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
            
            
        # inserindo os dados no banco de dados
        insert_user(p_nome, sobrenome, endereco, email, telefone)
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso.')
        # limpando os campos de entrada
        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)


    app_ = Label(frameDir, text='Inserir um novo usuário', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    #criando o formulário
    #primeiro nome
    l_p_nome = Label(frameDir, text='Primeiro Nome*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_p_nome = Entry(frameDir, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #sobrenome
    l_sobrenome = Label(frameDir, text='Sobrenome*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_sobrenome = Entry(frameDir, width=25, justify='left', relief='solid')
    e_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #endereço de usuario
    l_endereco = Label(frameDir, text='Endereço do usuário*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_endereco = Entry(frameDir, width=25, justify='left', relief='solid')
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    #enderço de email
    l_email = Label(frameDir, text='Endereço de e-mail*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_email = Entry(frameDir, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    #numero de telefone
    l_telefone = Label(frameDir, text='Número de telefone*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_telefone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    e_telefone = Entry(frameDir, width=25, justify='left', relief='solid')
    e_telefone.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    #botao salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir,command=add, image=img_salvar, compound=LEFT,width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                 font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Ver usuarios
def ver_usuarios():

    app_ = Label(frameDir, text='Ver usuários', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_users()

    #criando a treeview com barra de rolagem dupla
    list_header = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']
    
    global tree 
    
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    #verical scrollbar
    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)

    #horizonal scrollbar
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #ajuste da largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

# Novo livro
def novo_livro():
    global img_salvar
    #Função para salvar os livros inseridos pelos usuarios ou pelo admin
    def add():
        titulo = e_titulo.get()
        autor = e_autor.get()
        editora = e_editora.get()
        ano_publicacao = e_ano_publicacao.get()
        isbn = e_isbn.get()

        lista = [titulo, autor, editora, ano_publicacao, isbn]
        #verificando se há algum campo vazio ou nao
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
        #inserindo os dados no banco de dados
        insert_book(titulo, autor, editora, ano_publicacao, isbn)

        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso')

        #limpando os campos de entrada
        e_titulo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano_publicacao.delete(0, END)
        e_isbn.delete(0, END)

            



    app_ = Label(frameDir, text='Inserir um novo livro', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # criando formulário de preenchimento
    # titulo do livro
    l_titulo = Label(frameDir, text='Título do livro*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_titulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_titulo = Entry(frameDir, width=25, justify='left', relief='solid')
    e_titulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # autor do livro
    l_autor = Label(frameDir, text='Autor do livro*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_autor = Entry(frameDir, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # editora do livro
    l_editora = Label(frameDir, text='Editora do livro*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_editora = Entry(frameDir, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    # ano de publicacao do livro
    l_ano_publicacao = Label(frameDir, text='Ano de publicação do livro*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_ano_publicacao.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_ano_publicacao = Entry(frameDir, width=25, justify='left', relief='solid')
    e_ano_publicacao.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    #ISBN do livro
    l_isbn = Label(frameDir, text='ISBN do livro*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(frameDir, width=25, justify='left', relief='solid')
    e_isbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)
    
    #botao salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir,command=add, image=img_salvar, compound=LEFT,width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                 font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# ver livros inseridos
def ver_livros():
    app_ = Label(frameDir, text='Todos os livros', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = exibir_livros()

    #criando a treeview com barra de rolagem dupla
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano de Publicação', 'ISBN']
    
    global tree 
    
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    #verical scrollbar
    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)

    #horizonal scrollbar
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,165,110,100,50,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #ajuste da largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

# realizar empréstimo
def realizar_emprestimo():
    global img_salvar
    def add():
        usuario_id = e_id_usuario.get()
        livro_id = e_id_livro.get()


        lista = [usuario_id, livro_id]

        #verificando se há algum campo nao preenchido
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
                
            
        # inserindo os dados no banco de dados
        insert_loan(usuario_id, livro_id, hoje, None)

        messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso.')

        # limpando os campos de entrada
        e_id_usuario.delete(0, END)
        e_id_livro.delete(0, END)

    app_ = Label(frameDir, text='Realizar um empréstimo', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    #criando formulario de preenchimento
    # ID usuario
    l_id_usuario = Label(frameDir, text='Digite o ID do usuário*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_usuario = Entry(frameDir, width=25, justify='left', relief='solid')
    e_id_usuario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # ID livro
    l_id_livro = Label(frameDir, text='Digite o ID do livro*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_livro = Entry(frameDir, width=25, justify='left', relief='solid')
    e_id_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)


    # botao salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir,command=add, image=img_salvar, compound=LEFT,width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                 font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

#ver livros emprestados
def ver_livros_emprestados():
    app_ = Label(frameDir, text='Livros emprestados', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = []

    book_on_loan = get_books_on_loan()

    for book in book_on_loan:
        dado = [f'{book[0]}', f'{book[1]}', f'{book[2]}' f'{book[3]}', f'{book[4]}', f'{book[5]}']
        dados.append(dado)

    #criando a treeview com barra de rolagem dupla
    list_header = ['ID','Título', 'Nome do Usuário', 'D.Empréstimo', 'D.Devolução']
    
    global tree 
    
    tree = ttk.Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    #verical scrollbar
    vsb = ttk.Scrollbar(frameDir, orient='vertical', command=tree.yview)

    #horizonal scrollbar
    hsb = ttk.Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","ne","ne"]
    h=[20,175,120,90,90,100,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #ajuste da largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#devolução de um emprestimo
def devolucao_emprestimo():
    global img_salvar

    def add():
        devolucao_id = e_id_emprestimo.get()
        devolucao_data = e_data_devolucao.get()


        lista = [devolucao_id, devolucao_data]

        #verificando se há algum campo nao preenchido
        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
                
            
        # inserindo os dados no banco de dados
        update_loan_return_date(devolucao_id, devolucao_data)

        messagebox.showinfo('Sucesso', 'Livro devolvido com sucesso.')

        # limpando os campos de entrada
        e_id_emprestimo.delete(0, END)
        e_data_devolucao.delete(0, END)

    app_ = Label(frameDir, text='Atualizar a data de devolução de um empréstimo', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    
    app_linha = Label(frameDir, width=400, height=1, anchor=NW,font=('Verdana 1 '),bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    #criando formulario de preenchimento
    # ID do emprestimo
    l_id_emprestimo = Label(frameDir, text='Digite o ID do empréstimo*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_emprestimo = Entry(frameDir, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    # ID livro
    l_data_devolucao = Label(frameDir, text='Digite a data de devolução (AAAA-MM-DD)*', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_devolucao.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_data_devolucao = Entry(frameDir, width=25, justify='left', relief='solid')
    e_data_devolucao.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)


    # botao salvar
    img_salvar = Image.open('salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir,command=add, image=img_salvar, compound=LEFT,width=100, anchor=NW, text=' Salvar', bg=co1, fg=co4,
                 font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

#Função para controlar o Menu ------

def control(i):
    # novo usuario
    if i == 'novo_usuario':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao novo usuario
        novo_usuario()

        # ver usuarios
    if i == 'ver_usuarios':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao ver usuario
        ver_usuarios()
        # novo livro
    if i == 'novo_livro':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao novo livro
        novo_livro()
    # ver livros
    if i == 'ver_livros':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao ver livros
        ver_livros()
    # realizar emprestimo
    if i == 'emprestimo':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao realizar emprestimo
        realizar_emprestimo()
     # ver livros emprestados
    if i == 'ver_livos_emprestados':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao para ver os livros emprestados
        ver_livros_emprestados()
    # devolucao do emprestimo
    if i == 'devolucao':
        for widget in frameDir.winfo_children():
            widget.destroy()

        #chamando a funcao para devolucao dos emprestimos
        devolucao_emprestimo()

#Menu ---------
# Novo user
img_usuario = Image.open('addicon.png')
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
#criando botao do novo usuário
b_usuario = Button(frameEsq, command=lambda:control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text=' Novo usuário', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro
img_novo_livro = Image.open('addicon.png')
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
#criando botao do novo livro
b_novo_livro = Button(frameEsq, command=lambda:control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text=' Novo livro', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

#Ver livros
img_ver_livro = Image.open('livros2icon.png')
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
#criando botao de ver os livros
b_ver_livro = Button(frameEsq, command=lambda:control('ver_livros'), image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

#Ver todos usuarios
img_ver_usuario = Image.open('usericon.png')
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
#criando botao de ver os usuarios
b_ver_usuario = Button(frameEsq, command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text=' Exibir todos os usuários', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

#Realizar emprestimo
img_emprestimo = Image.open('addicon.png')
img_emprestimo = img_emprestimo.resize((18, 18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
#criando botao de realizar emprestimo
b_emprestimo = Button(frameEsq,command=lambda:control('emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=' Realizar um empréstimo', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

#Devolucao do Emprestimo
img_dev_emprestimo = Image.open('updateicon.png')
img_dev_emprestimo = img_dev_emprestimo.resize((18, 18))
img_dev_emprestimo = ImageTk.PhotoImage(img_dev_emprestimo)
#criando botao de devolucao de emprestimo
b_dev_emprestimo = Button(frameEsq,command=lambda:control('devolucao'), image=img_dev_emprestimo, compound=LEFT, anchor=NW, text=' Devolução de um empréstimo', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_dev_emprestimo.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

#Ver livros emprestados
img_ver_emprestimo = Image.open('carrinhoicon.png')
img_ver_emprestimo = img_ver_emprestimo.resize((18, 18))
img_ver_emprestimo = ImageTk.PhotoImage(img_ver_emprestimo)
#criando botao de ver os livros emprestados
b_ver_emprestimo = Button(frameEsq,command=lambda:control('ver_livos_emprestados'), image=img_ver_emprestimo, compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=co4, fg=co1,
                    font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_emprestimo.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)



"""
esse método inicia o loop principal da interface gráfica. Enquanto esse loop está rodando,
a janela permanecerá aberta e interativa, esperando por eventos como cliques de botão, digitação de texto, redimensionamento da janela, etc.
em mainloop(), a janela da aplicação não aparecerá nem responderá a qualquer interação do usuário. Ele é fundamental para manter a interface gráfica ativa e funcional.
"""
janela.mainloop()