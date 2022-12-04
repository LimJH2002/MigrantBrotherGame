import PySimpleGUI as sg

#layouts
sg.theme('DarkTeal12')
layout = [[sg.Text("Welcome to our ACE Migrants Mini Game!")],
          [sg.Text("Number of Players", size = (15, 1)), sg.InputText(key='num_of_players')], 
          [sg.Button("CONTINUE"), sg.Button("EXIT")]]

layout2 = [[sg.Text("Welcome to our ACE Migrants Mini Game!")],
          [sg.Text("Number of Players", size = (15, 1)), sg.InputText()], 
          [sg.Button("Test")]]

# Create the window
window = sg.Window("Migrant Brother Game", layout)
names = []

# Create an event loop
while True:
    
    event, values = window.read()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "CONTINUE":
        num_players = int(values['num_of_players'])
        for i in range(num_players):
            name = sg.popup_get_text('Enter Your Name')
            names.append(name)

    

window.close()