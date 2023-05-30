import sqlite3 as lite

def banco_medico():

    criar = lite.connect("medicos.db")
    cursor = criar.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS medicos(nome TEXT NOT NULL, email TEXT NOT NULL, crm TEXT PRIMARY KEY NOT NULL, senha INTEGER NOT NULL)")
    criar.commit()
    criar.close()
banco_medico()
def banco_paciente():

    criar=lite.connect("pacientes.db")
    cursor=criar.cursor()
    
    
    cursor.execute("CREATE TABLE IF NOT EXISTS pacientes( cod INTEGER PRIMARY KEY AUTOINCREMENT, crm TEXT NOT NULL, nome TEXT NOT NULL, cpf TEXT NOT NULL, email TEXT NOT NULL, data TEXT NOT NULL, horario TEXT NOT NULL, telefone TEXT NOT NULL)")
   
    criar.commit()
    criar.close()



