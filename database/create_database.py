from database.conexao import conectar_bd

def criar_banco_dados ():
    conexao, cursor = conectar_bd()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tarefas (
                    cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                    tarefa TEXT,
                    status TEXT);""")
    
    conexao.commit()
    conexao.close()

