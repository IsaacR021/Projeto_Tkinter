import tkinter as tk
#from tkinter import ttk,END,Event
import tela_login as login
import centralizar_tela as ct
import funcoes as fc
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # verde quase preto
co10="#A9A9A9" #cinzaescuro
co11="#C0C0C0" #pagina
co13="#000000" #pretão
def cadastro_paciente(crm):

    
    cadastro_paciente = tk.Tk()
    ct.centralizar(cadastro_paciente)
    cadastro_paciente.configure(background=co8)

    icone_path="imagens/medical.ico"
    cadastro_paciente.iconbitmap(icone_path)

    cadastro_paciente.title("Clínica Oliveira")


    f_titulo=tk.Frame(cadastro_paciente,width=310,height=50,background=co8,relief="flat")
    f_titulo.grid(row=1,column=0)

    l_titulo=tk.Label(f_titulo,text="Agendar Paciente",font=('Helvetica 15 bold'),bg=co8,fg=co1,relief="flat")
    l_titulo.place(x=50,y=10)


    f_opcao=tk.Frame(cadastro_paciente,width=310,height=453,background=co10,relief="flat")
    f_opcao.grid(row=2,column=0)


    f_listar=tk.Frame(cadastro_paciente,bg=co11,relief="flat")
    f_listar.place(width=750,height=453,x=310,y=0)



   

    l_nome = tk.Label(f_opcao, text="Nome do Paciente", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_nome.place(x=10, y=20)
    e_nome=tk.Entry(f_opcao,width=45,justify="left",relief="solid")
    e_nome.place(x=10,y=40)


    l_cpf = tk.Label(f_opcao, text="CPF", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_cpf.place(x=10, y=60)
    e_cpf=tk.Entry(f_opcao,width=45,justify="left",relief="solid")
    e_cpf.place(x=10,y=80)

    l_email = tk.Label(f_opcao, text="E-mail", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_email.place(x=10, y=100)
    e_email=tk.Entry(f_opcao,width=45,justify="left",relief="solid")
    e_email.place(x=10,y=120)



    l_data = tk.Label(f_opcao, text="Data", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_data.place(x=10, y=140)
    e_data=tk.Entry(f_opcao,width=30,justify="left",relief="solid")
    e_data.place(x=10,y=160)

    l_horario = tk.Label(f_opcao, text="Horário", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_horario.place(x=10, y=180)
    e_horario=tk.Entry(f_opcao,width=20,justify="left",relief="solid")
    e_horario.place(x=10,y=200)

    l_telefone = tk.Label(f_opcao, text="Telefone", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_telefone.place(x=10, y=220)
    e_telefone=tk.Entry(f_opcao,width=20,justify="left",relief="solid")
    e_telefone.place(x=10,y=240)



    b_agendar = tk.Button(f_opcao, text="AGENDAR", fg=co13, bg=co0,font=('Helvetica 10 '), width=9, height=1, relief="raised",overrelief="groove",command=lambda:fc.agendar_paciente(f_listar,crm,e_nome.get(),e_cpf.get(),e_email.get(),e_data.get(),e_horario.get(),e_telefone.get(),e_nome,e_cpf,e_email,e_data,e_horario,e_telefone))
    b_agendar.place(x=10, y=290)
    
    b_voltar = tk.Button(f_opcao, text="VOLTAR", fg=co13, bg=co0,width=9, height=2, relief="raised", overrelief="groove" , command=lambda:[cadastro_paciente.destroy(),login.chamar_login()])
    b_voltar.place(x=225, y=350)

    b_editar = tk.Button(f_opcao, text="EDITAR", fg=co13, bg=co0,font=('Helvetica 10 '), width=9, height=1, relief="raised",overrelief="groove",command=lambda:fc.atualizar_dados(f_listar,f_opcao,e_nome,e_cpf,e_email,e_data,e_horario,e_telefone))
    b_editar.place(x=115, y=290)

    b_deletar = tk.Button(f_opcao, text="DELETAR", fg=co7, bg=co0,font=('Helvetica 10 '), width=9, height=1, relief="raised",overrelief="groove",command=lambda:fc.excluir_agendamento(f_listar,e_nome,e_cpf,e_email,e_data,e_horario,e_telefone))
    b_deletar.place(x=220, y=290)

    e_pesquisar=tk.Entry(f_listar,text="Pesquisar",fg="gray")
    e_pesquisar.insert(0,'Pesquisar Por CRM/CPF')
    fc.pegar_dados_entry(e_pesquisar)
    e_pesquisar.bind('<FocusIn>',fc.apagar_entry)
    e_pesquisar.bind('<FocusOut>',fc.pegar_dados_entry(e_pesquisar))
    e_pesquisar.bind('<FocusOut>',fc.escrever_info)
    e_pesquisar.place(height=25,width=135,x=10,y=1)

    b_pesquisar = tk.Button(f_listar, text="Pesquisar", fg=co13, bg=co0,font=('Helvetica 10 '), width=9, height=1, relief="raised",overrelief="groove",command=lambda:fc.exibir_pesquisando(f_listar,e_pesquisar.get()))
    b_pesquisar.place(height=22,x=150,y=3)

    b_exibir_todos = tk.Button(f_listar, text="Exibir Todos", fg=co13, bg=co0,font=('Helvetica 10 '), width=9, height=1, relief="raised",overrelief="groove",command=lambda:fc.exibir_todo_banco(f_listar))
    b_exibir_todos.place(height=22,x=640,y=3)



    fc.exibir_todo_banco(f_listar)

    

    cadastro_paciente.mainloop()

if __name__=="__main__":
    cadastro_paciente(1030)
    