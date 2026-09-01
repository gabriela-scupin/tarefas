import flet as ft

class Campo_tarefa(ft.Row):
    def __init__(self):
        super().__init__()
        self.caixa_texto = ft.TextField(label="Incluir outra tarefa",
                                   filled=True)
        self.caixa_estado= ft.Text("Pendente")
        self.caixa_selecao= ft.Checkbox(on_change=self.alterar_cor)

        self.caixa_editar = ft.Button (content="Editar",
                      height=30,
                      color="#5F003B",
                      )
        self.caixa_excluir = ft.Button (content="Excluir",
                              height=30,
                              color="#5F003B",
                              )
        
        coluna_caixa= ft.Column(controls= [self.caixa_editar, self.caixa_excluir],
                                       expand=True,
                                       wrap= True)

  
        self.caixa_tarefas = ft.Container(content= ft.Row(controls= [self.caixa_estado,
                                                                    self.caixa_selecao,  
                                                                    self.caixa_texto,
                                                                   coluna_caixa],
                                                        ))

        self.controls = [self.caixa_tarefas]

    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.caixa_estado.value = "Concluído"
        else:
            self.caixa_selecao.bgcolor = "#FFFFFF"
            self.caixa_estado.value = "Pendente"
