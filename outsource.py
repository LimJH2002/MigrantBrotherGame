'''
Help me fill up the scenario things if youre ok with it. Thank you!
'''

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

s2 = situation('Family member falls sick',
                'Scenario A: Send money back home for medical fees',
                -50, 40,
                'Scenario B: Tell them you don\'t have enough money to send home this week',
                0, -20)

s3 = situation('Given an opportunity to sign up for an upksilling course',
                'Scenario A: Take up the opportunity to upskill',
                -30, 30,
                'Scenario B: Reject the offer due to course fees and lack of time',
                0, -20)

s4 = situation('Employer asks you to work overtime this Sunday',
                'Scenario A: Agree even though you are participating in an RC soccer competitions',
                20, -20,
                'Scenario B: Reject employer and join the RC soccer competition as planned',
                -20, 40)

s5 = situation('You come down with a cold',
                'Scenario A: See a doctor and take MC',
                -5, 15,
                'Scenario B: Continue working',
                0, -10)

s6 = situation('Your friend invites you to go Geylang together',
                'Scenario A: Politely decline',
                0, -20,
                'Scenario B: Go together',
                -25, 100)

s7 = situation('Employer fails to pay your salary on time',
                'Sorreh',
                -30, -50,
                'Bopes',
                -30, -50)

s8 = situation('Your kid misses you',
                'Scenario A: Buy a gift for them',
                -30, 20,
                'Scenario B: Video call your kid',
                0, -10)
s9 = situation('You meet someone on an online dating app',
               'Scenario A: Go out with them. (Roll dice, if >=4 then +50hp \
if <=3 then -50hp)',
               -20, 50 or -50,
               'Scenario B: Skipz',
               0, -10)

s10 = situation('Shopping for clothes',
                'Scenario A: Wait for sale/buy from outlet stores',
                -10, 10,
                'Scenario B: Buy whatever catches your eye',
                -20, 30)

s11 = situation('Wedding anniversary',
                'Scenario A: Buy nice gift for wife',
                -50, 60,
                'Scenario B: Videocall and wish happy anniversary :’D',
                0, 10)

s12 = situation('Drinking in public at night after 10pm',
                 'Scenario A: Drink with friends(-$10). (Roll dice, not caught if >= 4 else caught \
and pay fine of -$30',
                 -10 or -40, 70,
                 'Scenario B: Don’t drink',
                 0, -10)

s13 = situation('Celebrating Deepavali',
                 'Scenario A: Go out to Little India with friends to eat and celebrate',
                 -40, 50,
                 'Scenario B: Make homecooked traditional dishes back in your dorm',
                 -10, 20)

s14 = situation('Watch World Cup with friends',
                 'Scenario A: Bet. (Roll dice. a_money = 10 and a_happiness = 50 \
if <= 4 else a_money = -10 and a_happiness = -50',
                 -10 or 10, 50 or -50,
                 'Scenario B: Don’t bet',
                 0, -10)



               

               
