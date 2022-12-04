import PySimpleGUI as sg

#Global variables
day = 1

#layouts & fonts
font = ("Arial", 15)
sg.theme('DarkTeal12')
layout = [[sg.Text("Welcome to our ACE Migrants Mini Game!", font=font)],
          [sg.Text("Number of Players", size = (15, 1), font=font), sg.InputText(key='num_of_players')], 
          [sg.Button("CONTINUE"), sg.Button("EXIT")]]

layout2 = [[sg.Text("Day 1", font=font)],
           [sg.Text('PLAYER NAME', font=font, size=(15,1), justification='center'), sg.Text('MONEY($)', font=font, size=(10,1), justification='center'), sg.Text('HAPPINESS', font=font, size=(10,1), justification='center')], 
           [sg.Button("START GAME")]]

#Classes Declaration
class player:
    def __init__(self, name):
        self.name = name
        self.money = 300
        self.happiness = 50

class situation:
    def __init__(self, scenario, a_text, a_money, a_happiness, b_text, b_money, b_happiness):
        self.scenario = scenario
        self.a_t = a_text
        self.a_m = a_money
        self.a_h = a_happiness
        self.b_t = b_text
        self.b_m = b_money
        self.b_h = b_happiness

#Creating situation objects
s1 = situation('Settling dinner plans after work',
                'Scenario A: Go out with friends to eat at restaurant',
                -20, 50,
                'Scenario B: Dabao briyani back to eat',
                -5, 10)

situations = [s1]

#Helper Functions
def game_turn():
    choice = sg.Window('Continue?', [[sg.T('Do you want to continue?')], [sg.Button("A"), sg.Button("B")]], disable_close=True).read(close=True)
    if choice[0] == 'a':
        pass
    elif choice[0] == 'b':
        pass
    return

# Create the window
window = sg.Window("Migrant Brother Game", layout, auto_size_buttons=True, auto_size_text=True)
players_list = []

# Create an event loop
while True:
    
    event, values = window.read()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "CONTINUE":
        num_players = int(values['num_of_players'])
        for i in range(num_players):
            name = sg.popup_get_text('Enter Your Name', font=font, modal=False)
            players_list.append(player(name))

        window.close()

        #Populating players list
        j = 2
        for i in range(num_players):
            profile = [sg.Text(players_list[i].name, font=font, size=(15,1), justification='center'), 
                       sg.Text(players_list[i].money, font=font, size=(10,1), justification='center'), 
                       sg.Text(players_list[i].happiness, font=font, size=(10,1), justification='center')]
            layout2.insert(j, profile)
            j += 1

        window = sg.Window("Game Start", layout2)

    if event == "START GAME":
        game_turn()

window.close()