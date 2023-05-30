import tkinter as tk
from PIL import ImageTk, Image
import tela_cadastro as cadastro
import tela_login as login
#from funcoes import centralizar
import centralizar_tela as ct

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co8 = "#263238"   # + verde

def tela_inicial():

    tela_inicial = tk.Tk()
    #tela_inicial.geometry("1043x453")
    ct.centralizar(tela_inicial)
    tela_inicial.configure(background=co8)
    tela_inicial.resizable(width=False,height=False)

    icone_path="imagens/medical.ico"
    tela_inicial.iconbitmap(icone_path)

    tela_inicial.title("Clínica Oliveira")

    f_titulo=tk.Frame(tela_inicial,width=310,height=50,background=co2,relief="flat")
    f_titulo.grid(row=1,column=0)

    l_titulo=tk.Label(f_titulo,text="Clínica Oliveira",font=('Helvetica 25 bold'),bg=co2,fg=co1,relief="flat")
    l_titulo.place(x=35,y=10)


    f_opcao=tk.Frame(tela_inicial,width=310,height=453,background=co8,relief="flat")
    f_opcao.grid(row=2,column=0)




    image = Image.open(r"C:\Users\isaac\OneDrive\Área de Trabalho\projeto tkinter\imagens\fototkinte.jpg")  
    image = image.resize((750, 453))  

    photo = ImageTk.PhotoImage(image)

    label = tk.Label(tela_inicial, image=photo)
    label.place(x=310, y=0)  





    b_login=tk.Button(f_opcao,text="LOGIN",width=20,height=3,bg=co0,foreground=co8,relief='raised',overrelief='groove',command=lambda:[tela_inicial.destroy(),login.chamar_login()])
    b_login.place(x=80,y=100)


    b_register=tk.Button(f_opcao,text="REGISTRAR",fg=co8,bg=co0,width=20,height=3,relief="raised",overrelief="groove",command=lambda: [tela_inicial.destroy(), cadastro.chamar_cadastro()])
    b_register.place(x=80,y=200)

    tela_inicial.mainloop()
if __name__=="__main__":
    tela_inicial()
