import sqlite3 as lite
from tkinter import messagebox,ttk,END
import tkinter as tk
import cadastro_paciente2 as cp
co0 = "#f0f3f5"
co1="#4fa882"

def cadastrar_medicos(nome,email,crm,senha,confir_senha,e_nome,e_email,e_crm,e_senha,e_confir_senha):

    if nome is None or email is None or crm is None or nome== "" or email == "" or crm == "":
        messagebox.showerror("Erro","Preencha todos os Campos")
    else:
        if senha==confir_senha:
            con=lite.connect('medicos.db')
            cursor=con.cursor()
            cursor.execute("INSERT INTO medicos VALUES (?,?,?,?)" ,(nome,email,crm,senha))
            con.commit()
            con.close()

            e_nome.delete(0,'end')
            e_email.delete(0,'end')
            e_crm.delete(0,'end')
            e_senha.delete(0,'end')
            e_confir_senha.delete(0,'end')
            e_nome.focus_set()
            messagebox.showinfo('Sucesso','Cadastrado realizado com Sucesso')

        else :
            messagebox.showinfo("Atenção","As senhas fornecidas não correspondem. Por favor, verifique se digitou corretamente e tente novamente.")
            e_senha.focus_set()


def agendar_paciente(f_listar,crm,nome,cpf,email,data,horario,telefone,e_nome,e_cpf,e_email,e_data,e_horario,e_telefone):

    if nome is None or cpf is None or email is None or data is None or horario is None or telefone is None or nome== "" or cpf == "" or email == "" or data == "" or horario == "" or telefone == "":
        messagebox.showerror("Erro","Preencha todos os Campos")
    else:
            
        conet=lite.connect('pacientes.db')
        cursor=conet.cursor()
        cursor.execute("INSERT INTO pacientes(crm, nome, cpf, email, data, horario, telefone) VALUES (?, ?, ?, ?, ?, ?, ?)",(crm, nome, cpf, email, data, horario, telefone))
        conet.commit()
        conet.close()
        
        e_nome.delete(0,'end')
        e_cpf.delete(0,'end')
        e_email.delete(0,'end')
        e_data.delete(0,'end')
        e_horario.delete(0,'end')
        e_telefone.delete(0,'end')
        e_nome.focus_set()
        exibir_todo_banco(f_listar)
        messagebox.showinfo("Sucesso","Agendamento Realizado")
    
def fazer_login(crm,senha,tela_login):
    conect=lite.connect("medicos.db")
    cursor=conect.cursor()
    cursor.execute("SELECT * FROM medicos WHERE crm = ? AND senha = ? ",(crm,senha,))
    resultado=cursor.fetchone()
    conect.commit()
    conect.close()

    if resultado is not None:
    
        tela_login.destroy()
        cp.cadastro_paciente(crm)
    

    else:
        messagebox.showinfo("Info","Cadastro não Encontrado")


        
def atualizar_dados(f_listar,f_opcao,e_nome,e_cpf,e_email,e_data,e_horario,e_telefone):

    def apagar():
        e_nome.delete(0,'end')
        e_cpf.delete(0,'end')
        e_email.delete(0,'end')
        e_data.delete(0,'end')
        e_horario.delete(0,'end')
        e_telefone.delete(0,'end')
        e_nome.focus_set()

    def atualizar_banco(f_listar,cod,e_nome,e_cpf,e_email,e_data,e_horario,e_telefone):
        nome=e_nome
        cpf=e_cpf
        email=e_email
        data=e_data
        horario=e_horario
        telefone=e_telefone
        
        if nome is None or cpf is None or email is None or data is None or horario is None or telefone is None or nome== "" or cpf == "" or email == "" or data == "" or horario == "" or telefone == "":
            messagebox.showerror("Erro","Preencha todos os Campos")
        else:   
            conect=lite.connect("pacientes.db")
            cur=conect.cursor()
            cur.execute("UPDATE pacientes SET nome=?,cpf=?,email=?,data=?,horario=?,telefone=? WHERE cod = ?", (nome,cpf,email,data,horario,telefone,cod))
            conect.commit()
            conect.close()
            
            apagar()

            exibir_todo_banco(f_listar)
            b_atualizar.destroy()
            messagebox.showinfo('Sucesso',"Dados Atualizado.")




    try:
        selecionar=exibir_topicos.focus()
        item_dentro_dicionario=exibir_topicos.item(selecionar)
        item_lista=item_dentro_dicionario['values']
        
        if e_cpf is not None:
            e_nome.delete(0,'end')
            e_cpf.delete(0,'end')
            e_email.delete(0,'end')
            e_data.delete(0,'end')
            e_horario.delete(0,'end')
            e_telefone.delete(0,'end')
            
          
        e_nome.insert(0,item_lista[2])
        e_cpf.insert(0,item_lista[3])
        e_email.insert(0,item_lista[4])
        e_data.insert(0,item_lista[5])
        e_horario.insert(0,item_lista[6])
        e_telefone.insert(0,item_lista[7])

        b_atualizar = tk.Button(f_opcao, text="ATUALIZAR", fg=co1, bg=co0,font=('Helvetica 10 '), width=9, height=2, relief="raised",overrelief="groove",command=lambda:atualizar_banco(f_listar,item_lista[0],e_nome.get(),e_cpf.get(),e_email.get(),e_data.get(),e_horario.get(),e_telefone.get()))
        b_atualizar.place(x=115, y=320)
        

        #e_nome.focus_set()


    except IndexError:
        messagebox.showerror('Erro','Selecionar Dados')
        

def exibir_todo_banco(f_listar):
    lista_de_pacientes=[]
    conect=lite.connect("pacientes.db")
    cur=conect.cursor()
    cur.execute("SELECT * FROM pacientes")
    pacientes=cur.fetchall()

    for paciente in pacientes:
        lista_de_pacientes.append(paciente)
    global exibir_topicos
    topicos=['Cod','Méd.Responsável','Paciente','CPF','E-Mail','Data','Horário','Telefone']
    exibir_topicos=ttk.Treeview(f_listar,selectmode="extended",columns=topicos,show="headings")
    exibir_topicos.place(width=720,height=410,x=10,y=30)
        
    largura=[20,80,60,60,120,60,60,80]
    alinhamento=['center',"center","center","center","center","center","center","center"]
    i=0
        
    for topico in topicos:
         exibir_topicos.heading(topico, text=topico.title(),anchor="center")
         exibir_topicos.column(topico, anchor=alinhamento[i],width=largura[i])
         i+=1

    for item in lista_de_pacientes:
        exibir_topicos.insert('','end',values=item)


   # return lista_de_pacientes

def exibir_pesquisando(f_listar,e_pesquisar):
    lista_de_pacientes=[]
    conect=lite.connect("pacientes.db")
    cur=conect.cursor()
    cur.execute("SELECT * FROM pacientes WHERE crm = ?",(e_pesquisar,))
    pacientes=cur.fetchall()
    for paciente in pacientes:
        lista_de_pacientes.append(paciente)
    cur.execute("SELECT * FROM pacientes WHERE cpf = ?",(e_pesquisar,))
    pacientes=cur.fetchall()

    for paciente in pacientes:
        lista_de_pacientes.append(paciente)
    global exibir_topicos
    topicos=['Cod','Méd.Responsável','Paciente','CPF','E-Mail','Data','Horário','Telefone']
    exibir_topicos=ttk.Treeview(f_listar,selectmode="extended",columns=topicos,show="headings")
    exibir_topicos.place(width=720,height=410,x=10,y=30)
        
    largura=[20,80,60,60,120,60,60,80]
    alinhamento=['center',"center","center","center","center","center","center","center"]
    i=0
        
    for topico in topicos:
         exibir_topicos.heading(topico, text=topico.title(),anchor="center")
         exibir_topicos.column(topico, anchor=alinhamento[i],width=largura[i])
         i+=1

    for item in lista_de_pacientes:
        exibir_topicos.insert('','end',values=item)

    if lista_de_pacientes == []:
        messagebox.showinfo("Info","Nenhum Cadastro Encontrado")






def excluir_agendamento(f_listar,e_nome,e_cpf,e_email,e_data,e_horario,e_telefone):
    try:
        selecionar=exibir_topicos.focus()
        item_dentro_dicionario=exibir_topicos.item(selecionar)
        item_lista=item_dentro_dicionario['values']
        
        if e_cpf is not None:
            e_nome.delete(0,'end')
            e_cpf.delete(0,'end')
            e_email.delete(0,'end')
            e_data.delete(0,'end')
            e_horario.delete(0,'end')
            e_telefone.delete(0,'end')
            
        
        codi=item_lista[0]
        conect=lite.connect("pacientes.db")
        cur=conect.cursor()
        cur.execute("DELETE FROM pacientes WHERE cod=?",(codi,))
        conect.commit()
        conect.close()
        exibir_todo_banco(f_listar)


        
    except IndexError:
        messagebox.showerror('Erro','Selecionar Dados')



def pegar_dados_entry(e_pesquisar):
    global pesquisar
    pesquisar=e_pesquisar


def apagar_entry(event):
        if pesquisar.get()=='Pesquisar Por CRM/CPF':
            pesquisar.delete(0,END)
            pesquisar.config(fg='black')

def escrever_info(event):
    if pesquisar.get() is None or pesquisar.get() == '':
        pesquisar.insert(0, 'Pesquisar Por CRM/CPF')
        pesquisar.config(fg='gray')