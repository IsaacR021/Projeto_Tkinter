import tkinter as tk
from PIL import ImageTk, Image
import funcoes as fc
#from funcoes import fazer_login
import centralizar_tela as ct
import tela_inicial
from tkinter import messagebox

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co8 = "#263238"   # + verde
co10="#A9A9A9"


def chamar_login():
    
    
    tela_login = tk.Tk()
    ct.centralizar(tela_login)
    tela_login.configure(background=co8)
    tela_login.resizable(width=False, height=False)

    icone_path="imagens/medical.ico"
    tela_login.iconbitmap(icone_path)

    tela_login.title("Clínica Oliveira")


    f_titulo = tk.Frame(tela_login, width=310, height=50,
    background=co2, relief="flat")
    f_titulo.grid(row=1, column=0)

    l_titulo = tk.Label(f_titulo, text="Clínica Oliveira", font=('Helvetica 25 bold'), bg=co2, fg=co1, relief="flat")
    l_titulo.place(x=30, y=10)


    f_opcao = tk.Frame(tela_login, width=310, height=453,background=co8, relief="flat")
    f_opcao.grid(row=2, column=0)


    
    image = Image.open( r"C:\Users\isaac\OneDrive\Área de Trabalho\projeto tkinter\imagens\fototkinte.jpg")
    image = image.resize((750, 453))  

    
    photo = ImageTk.PhotoImage(image)


    label = tk.Label(tela_login, image=photo)
    label.place(x=310, y=0)  


    
    l_login = tk.Label(f_opcao, text="Login/CRM", font=('Helvetica 10 bold'), bg=co8, fg=co1, relief="flat")
    l_login.place(x=10, y=20)
    e_login=tk.Entry(f_opcao,justify="left",relief="solid",font=('calibri',11))
    e_login.place(width=200,height=30,x=15,y=45)



    l_senha = tk.Label(f_opcao, text="Senha", font=('Helvetica 10 bold'), bg=co8, fg=co1, relief="flat")
    l_senha.place(x=10, y=100)
    e_senha=tk.Entry(f_opcao,justify="left",relief="solid",font=('calibri',11),show='*')
    e_senha.place(width=200,height=30,x=15,y=125)
    
    

    




    b_entrar = tk.Button(f_opcao, text="ENTRAR", fg=co8, bg=co0, width=15, height=3, relief="raised", 
                       overrelief="groove", command=lambda:fc.fazer_login(e_login.get(),e_senha.get(),tela_login))
    b_entrar.place(x=30, y=250)
    
    b_voltar = tk.Button(f_opcao, text="VOLTAR", fg=co8, bg=co0,width=15, height=3, relief="raised", overrelief="groove" , command=lambda:[tela_login.destroy(),tela_inicial.tela_inicial()])

    b_voltar.place(x=160, y=250)


    # Loop principal do Tkinter
    tela_login.mainloop()

if __name__=="__main__":
    chamar_login()

