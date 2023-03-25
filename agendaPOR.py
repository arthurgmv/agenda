import PySimpleGUI as sg

agenda = []

def adicionar_evento(values):
    nome = values["nome"]
    data = values["data"]
    hora = values["hora"]
    descricao = values["descricao"]

    evento = {"nome": nome, "data": data, "hora": hora, "descricao": descricao}
    agenda.append(evento)

def visualizar_eventos():
    if not agenda:
        sg.popup("Não há eventos na agenda.")
    else:
        eventos = []
        for evento in agenda:
            eventos.append([evento["nome"], evento["data"], evento["hora"], evento["descricao"]])
        window = sg.Window("Agenda - Visualizar eventos", [[sg.Table(values=eventos, headings=["Nome", "Data", "Hora", "Descrição"])], [sg.Button("Ok")]])
        event, values = window.read()
        window.close()

def excluir_evento(values):
    if not agenda:
        sg.popup("Não há eventos na agenda.")
    else:
        evento_para_excluir = int(values["eventos"])
        if evento_para_excluir < 1 or evento_para_excluir > len(agenda):
            sg.popup("Evento inválido.")
        else:
            del agenda[evento_para_excluir - 1]
            sg.popup("Evento excluído com sucesso.")

sg.theme("reddit")

layout = [[sg.Text("--- Agenda ---", font=("Helvetica", 20))],
          [sg.Text("1 - Adicionar evento", font=("Helvetica", 14))],
          [sg.Text("Nome:", size=(10, 1)), sg.InputText(key="nome")],
          [sg.Text("Data (formato DD/MM/AAAA):", size=(25, 1)), sg.InputText(key="data")],
          [sg.Text("Hora (formato HH:MM):", size=(20, 1)), sg.InputText(key="hora")],
          [sg.Text("Descrição:", size=(10, 1)), sg.Multiline(key="descricao", size=(40, 5))],
          [sg.Button("Adicionar", size=(10, 1))],
          [sg.Text("2 - Visualizar eventos", font=("Helvetica", 14))],
          [sg.Button("Visualizar", size=(10, 1))],
          [sg.Text("3 - Excluir evento", font=("Helvetica", 14))],
          [sg.Text("Selecione o evento a ser excluído:", size=(30, 1)), sg.Combo(values=[str(i+1) for i in range(len(agenda))], key="eventos", size=(10, 1))],
          [sg.Button("Excluir", size=(10, 1))],
          [sg.Text("4 - Sair", font=("Helvetica", 14))],
          [sg.Button("Sair", size=(10, 1))]]

window = sg.Window("Agenda", layout)

while True:
    event, values = window.read()

    if event == "Adicionar":
        adicionar_evento(values)
        sg.popup("Evento adicionado com sucesso.")
    elif event == "Visualizar":
        visualizar_eventos()
    elif event == "Excluir":
        excluir_evento(values)
        sg.popup("Evento excluído com sucesso.")
    elif event == "Sair" or event == sg.WIN_CLOSED:
        break

window.close()
