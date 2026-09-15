import flet as ft
from component.campo_tarefas import Campo_tarefa
import sqlite3
from database.conexao import conectar_bd
from database.create_database import criar_banco_dados
from model import model_tarefa


def main(page: ft.Page):

    # Define o título que aparece na janela do programa
    page.title= "Feito por Gabriela Scúpin" #escrevendo algo na janela

    # Define a cor de fundo da janela
    page.bgcolor= "#e3c4ff" #alterando a cor da janela

    # Define a altura da janela
    page.window.height= 800 #alterando a altura da janela

    # Define a largura da janela
    page.window.width= 700 #alterando a largura da janela

    # Deixa os elementos da página alinhados horizontalmente no centro
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER


    lista_tarefas= []
    criar_banco_dados()

    def adicionar_tarefa ():
        model_tarefa.inserir(caixa_tarefas.value)
        novo_campo = Campo_tarefa(texto_tarefa = caixa_texto.value , 
                                  funcao_tarefa = excluir_tarefa)
        lista_tarefas.append(novo_campo)
        Campo_tarefa.value = ""

    def excluir_tarefa():
        for campo in lista_tarefas:
            if campo.caixa_selecao.value == True:
                lista_tarefas.remove(campo)


    # Cria o título que será mostrado na tela
    titulo = ft.Text(value="Tarefas da gabisnaga", 
                          color="#38084B",
                          size=45,
                          weight="bold",
                          font_family="Georgia")

    caixa_texto = ft.TextField(label="Digite a sua tarefa",
                                   filled=True)
    
    botao_adicionar = ft.FloatingActionButton(content= "+",
                                           bgcolor= "#f0cafa",
                                           hover_color= "#ffc4d8",
                                           on_click= adicionar_tarefa )

    caixa_tarefas = ft.Row(controls= [caixa_texto, botao_adicionar],
                                        alignment= "center")

    coluna_notas= ft.Column(controls=lista_tarefas,
        expand=True,
        wrap=True)


    page.add(titulo)
    page.add(caixa_tarefas)
    page.add(coluna_notas)




ft.run(main)
    