import PySimpleGUI as sg

def tela1():
    lista=[]
    # All the stuff inside your window.
    layout = [  [sg.Text("Digite o seu nome:"), sg.InputText(key='nome')],
                [sg.Text("Digite a primeira nota:"), sg.InputText(key='nota1')],
                [sg.Text("Digite a segunda nota:"), sg.InputText(key='nota2')],
                [sg.Text('',key='resultado')],
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
            window['resultado'].update(lista)

        if event == 'Adicionar aluno':
            nome = values['nome']
            nota1 = values['nota1']
            nota2 = values['nota2']

            if nome== '' and nota1== '' and nota2== '':
                sg.popup('Os campo estão vazios ')
            elif nome.isdigit()== False and len(nome) < 3: 
                    sg.popup('O nome está curto')
            elif nome.isdigit()== True:
                sg.popup('O nome não pode ser númerico')

            elif nota1.isdigit() == True and nota2.isdigit() == True:

                nota1=float(nota1)
                nota2=float(nota2)
                if nota1 > 10 or nota2 > 10:
                    sg.popup('São só validas menores do que 10')

            else:
                sg.popup('As notas devem ser numéricas')    
    
            lista.append({  
                'nome': nome,
                'nota1': nota1,
                'nota2': nota2
            })

           
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