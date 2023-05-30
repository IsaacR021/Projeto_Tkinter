import tkinter as tk
from PIL import ImageTk, Image
import funcoes as fc
from centralizar_tela import centralizar
import tela_inicial

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co8 = "#263238"   # + verde
co10="#A9A9A9"


def chamar_cadastro():
    

    tele_cadastro = tk.Tk()
    #tele_cadastro.geometry("1043x453")
    centralizar(tele_cadastro)
    tele_cadastro.configure(background=co8)
    tele_cadastro.resizable(width=False, height=False)

    icone_path="imagens/medical.ico"
    tele_cadastro.iconbitmap(icone_path)

    tele_cadastro.title("Clínica Oliveira")


    f_titulo = tk.Frame(tele_cadastro, width=310, height=50,background=co8, relief="flat")
    f_titulo.grid(row=1, column=0)

    l_titulo = tk.Label(f_titulo, text="Cadastrar Médico", font=('Helvetica 20 bold'), bg=co8, fg=co1, relief="flat")
    l_titulo.place(x=35, y=10)


    f_opcao = tk.Frame(tele_cadastro, width=310, height=453,background=co10, relief="flat")
    f_opcao.grid(row=2, column=0)


    
    image = Image.open( r"C:\Users\isaac\OneDrive\Área de Trabalho\projeto tkinter\imagens\fototkinte.jpg")
    image = image.resize((750, 453))  

    
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(tele_cadastro, image=photo)
    label.place(x=310, y=0)  



    l_nome = tk.Label(f_opcao, text="Nome Completo", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_nome.place(x=10, y=20)
    e_nome=tk.Entry(f_opcao,width=45,justify="left",relief="solid")
    e_nome.place(x=10,y=40)


    l_email = tk.Label(f_opcao, text="E-mail", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_email.place(x=10, y=60)
    e_email=tk.Entry(f_opcao,width=45,justify="left",relief="solid")
    e_email.place(x=10,y=80)


    l_crm = tk.Label(f_opcao, text="CRM", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_crm.place(x=10, y=100)
    e_crm=tk.Entry(f_opcao,width=30,justify="left",relief="solid")
    e_crm.place(x=10,y=120)

    l_senha = tk.Label(f_opcao, text="Senha", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_senha.place(x=10, y=140)
    e_senha=tk.Entry(f_opcao,width=20,justify="left",relief="solid",show='*')
    e_senha.place(x=10,y=160)

    l_confir_senha = tk.Label(f_opcao, text="Confirmar Senha", font=('Helvetica 10 '), bg=co10, fg="black", relief="flat")
    l_confir_senha.place(x=10, y=180)
    e_confir_senha=tk.Entry(f_opcao,width=20,justify="left",relief="solid",show="*")
    e_confir_senha.place(x=10,y=200)



    b_register = tk.Button(f_opcao, text="REGISTRAR", fg=co8, bg=co0, width=15, height=3, relief="raised", 
                       overrelief="groove", command=lambda: fc.cadastrar_medicos(e_nome.get(), e_email.get(), e_crm.get(), 
                                                                                 e_senha.get(), e_confir_senha.get(),e_nome,e_email,e_crm,e_senha,e_confir_senha))
    b_register.place(x=30, y=250)
    
    b_voltar = tk.Button(f_opcao, text="VOLTAR", fg=co8, bg=co0,width=15, height=3, relief="raised", overrelief="groove" , command=lambda:[tele_cadastro.destroy(),tela_inicial.tela_inicial()])

    b_voltar.place(x=160, y=250)


    tele_cadastro.mainloop()

if __name__=="__main__":
    chamar_cadastro()

