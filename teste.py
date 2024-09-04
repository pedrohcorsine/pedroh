import PySimpleGUI as sg

def tela1():
   
    # All the stuff inside your window.
    layout = [  [sg.Text("Digite o seu nome:"), sg.InputText(key='nome')],
                [sg.Text("Digite a primeira nota:"), sg.InputText(key='nota1')],
                [sg.Text("Digite a terceira nota:"), sg.InputText(key='nota2')],
                [sg.Text('')],
                [sg.Button('Adicionar aluno'), sg.Button('Cancel'), sg.Button('Resultado')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
            
        if event == 'Resultado':
            window.close()
            tela2()

        if event == 'Adicionar aluno':
            nome = values['nome']
            nota1 = values['nota1']
            nota2 = values['nota2']

        print('Hello', values[0], '!')

    window.close()


def tela2():

    # All the stuff inside your window.
    layout = [  [sg.Text("What's your name?")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('Hello', values[0], '!')

    window.close()


tela1()