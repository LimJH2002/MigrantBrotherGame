import PySimpleGUI as sg

#layouts & fonts
font = ("Arial", 15)
sg.theme('DarkTeal12')
layout = [[sg.Text("Welcome to our ACE Migrants Mini Game!", font=font)],
          [sg.Text("Number of Players", size = (15, 1), font=font), sg.InputText(key='num_of_players')], 
          [sg.Button("CONTINUE"), sg.Button("EXIT")]]

layout2 = [[sg.Text("Welcome to our ACE Migrants Mini Game!")],
          [sg.Text("Number of Players", size = (15, 1)), sg.InputText()], 
          [sg.Button("Test")]]

#Classes Declaration
class player:
    def __init__(self, name):
        self.name = name
        self.money = 300
        self.happiness = 50

class situation:
    def __init__(self, scenario, a_text, a_points, b_text, b_points):
        self.scenario = scenario
        self.a_t = a_text
        self.a_p = a_points
        self.b_t = b_text
        self.b_p = b_points

# Create the window
window = sg.Window("Migrant Brother Game", layout)
players_list = []

# Create an event loop
while True:
    
    event, values = window.read()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "CONTINUE":
        num_players = int(values['num_of_players'])
        for i in range(num_players):
            name = sg.popup_get_text('Enter Your Name', font=font)
            players_list.append(player(name))

    

window.close()