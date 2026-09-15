from database.conexao import conectar_bd

def inserir_tarefa(texto_tarefa):

    conexao, cursor = conectar_bd()
    cursor.execute("""
                        insert into tarefas (tarefas,status) values ("?,?}"); """, [texto_tarefa.value, "PENDENTE"])
                            
    conexao.commit()
    conexao.close()


def recuperar_tarfas():
    conexao, cursor = conectar_bd
    cursor.execute(""" SELECT cod_tarefa, status, tarefa FROM tarefas; """)

    tarefas = cursor.fetchall()
    conexao.close()