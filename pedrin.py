import PySimpleGUI as sg

# All the stuff inside your window.
layout = [
    [sg.Button ('', size=(6,3))]
    for i in ()
]


# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

  

window.close()