import PySimpleGUI as sg

#layouts & fonts
font = ("Arial", 15)
sg.theme('DarkTeal12')
layout = [[sg.Text("Welcome to our ACE Migrants Mini Game!", font=font)],
          [sg.Text("Number of Players", size = (15, 1), font=font), sg.InputText(key='num_of_players')], 
          [sg.Button("CONTINUE"), sg.Button("EXIT")]]

layout2 = [[sg.Text("Day 1", font=font)],
           [sg.Text('Player Name', font=font, size=(10,1)), sg.Text('Money($)', font=font, size=(7,1)), sg.Text('Happiness', font=font, size=(8,1))], 
           [sg.Button("Start Day 1")]]

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
            name = sg.popup_get_text('Enter Your Name', font=font, modal=True)
            players_list.append(player(name))

        window.close()

        j = 2
        for i in range(num_players):
            profile = [sg.Text(players_list[i].name, font=font, size=(10,1), justification='center'), 
                       sg.Text(players_list[i].money, font=font, size=(7,1), justification='center'), 
                       sg.Text(players_list[i].happiness, font=font, size=(8,1), justification='center')]
            layout2.insert(j, profile)
            j += 1

        window = sg.Window("Game Start", layout2)

    

window.close()