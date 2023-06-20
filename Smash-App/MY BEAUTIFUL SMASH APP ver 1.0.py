# Importing tkinter and required modules for the application

from tkinter import *
import tkinter.ttk, Smash_Classes
from Roster_Creator import *

# Creating lists that categorizes different characters to be called later
offensive_options = ['',
                     'All-Rounder',
                     'Rushdown',
                     'Pressurer', 
                     'Hit and Run', 
                     'Mix Up', 
                     'Zone Breaker', 
                     'Dominating',
                     'Footsies',
                     'Glass Cannon',
                     'Tag Team',
                     'Psychological']

defensive_options = ['',
                     'Zoner',
                     'Bait and Punish', 
                     'Trapper'
                     'Turtle',
                     'Keep Away',
                     'Stage Control',
                     'Half-Grappler']

flexible_options = ['',
                    'Dynamic', 
                    'Precision']

all_options = ['Any',
               'All-Rounder',
               'Rushdown',
               'Pressurer', 
               'Hit and Run', 
               'Mix Up', 
               'Zone Breaker', 
               'Dominating',
               'Footsies',
               'Glass Cannon',
               'Tag Team',
               'Psychological',
               'Zoner',
               'Bait and Punish',
               'Trapper',
               'Turtle',
               'Keep Away',
               'Stage Control', 
               'Half-Grappler',
               'Dynamic',
               'Precision']

role_dict = {'Any' : all_options,
             'Offensive': offensive_options,
             'Defensive' : defensive_options,
             'Flexible' : flexible_options}

full_roster = ['Mario', 'Yoshi', 'Lucario', 'Pit', 'Dark Pit', 'Ryu', 'Ken','Fox', 'Sheik', 
               'Pikachu', 'Mii Brawler', 'Peach', 'Diddy Kong', 'Kirby', 'Pichu', 'Roy', 'Daisy', 
               'Chrom', 'Banjo & Kazooie','Greninja', 'Captain Falcon', 'Lucina', 'Wii Fit Trainer',
               'Bowser Jr.', 'Meta Knight', 'Falco', 'Pokemon Trainer', 'Lucas', 'Mii Swordfighter',
               'Zero Suit Samus','Ganondorf','Wolf', 'King K. Rool','Ridley', 'Incineroar', 
               'Byleth',B'Ike', 'Little Mac', 'Dr. Mario', 'Mewtwo', 'Mr. Game & Watch',
               'Rosalina & Luma', 'Ice Climbers', 'Young Link', 'Jigglypuff', 'Ness', 
               'Bayonetta', 'Link', 'Samus', 'R.O.B.', 'Snake', 'Mii Gunner', 'Piranha Plant', 
               'Dark Samus','Toon Link', 'King Dedede', 'Corrin', 'Wario', 'Bowser', 'Robin', 
               'Pac-Man', 'Palutena', 'Villager', 'Isabelle', 'Sonic', 'Duck Hunt', 'Mega Man', 
               'Simon', 'Richter','Luigi', 'Donkey Kong', 'Olimar', 'Shulk', 'Cloud', 'Inkling', 
               'Joker', 'Hero', 'Terry', 'Zelda', 'Marth']

all_rounder = ['Mario', 
               'Yoshi', 
               'Lucario', 
               'Pit', 
               'Dark Pit', 
               'Ryu', 
               'Ken' ]
rushdown = ['Fox', 
            'Sheik', 
            'Pikachu', 
            'Mii Brawler']
pressurer = ['Peach', 
             'Diddy Kong', 
             'Kirby', 
             'Pichu', 
             'Roy', 
             'Daisy', 
             'Chrom', 
             'Banjo & Kazooie']
hit_and_run = ['Greninja', 
               'Captain Falcon', 
               'Lucina', 
               'Wii Fit Trainer']
mix_up = ['Bowser Jr.', 
          'Meta Knight', 
          'Falco', 
          'Pokemon Trainer', 
          'Lucas', 
          'Mii Swordfighter']
zone_breaker = ['Zero Suit Samus']
dominating = ['Ganondorf',
              'Wolf', 
              'King K. Rool',
              'Ridley', 
              'Incineroar', 
              'Byleth', ]
footsies = ['Ike', 
            'Little Mac']
glass_cannon = ['Dr. Mario', 
                'Mewtwo', 
                'Mr. Game & Watch']
tag_team = ['Rosalina & Luma', 
            'Ice Climbers']
psychological = ['Young Link', 
                 'Jigglypuff', 
                 'Ness', 
                 'Bayonetta']
zoner = ['Link', 
         'Samus', 
         'R.O.B.', 
         'Snake', 
         'Mii Gunner', 
         'Piranha Plant', 
         'Dark Samus']
bait_and_punish = ['Toon Link', 
                   'King Dedede', 
                   'Corrin', 
                   'Wario', 
                   'Bowser']
trapper = ['Robin', 
           'Pac-Man']
turtle = ['Palutena', 
          'Villager', 
          'Isabelle']
keep_away = ['Sonic']
stage_control = ['Duck Hunt', 
                 'Mega Man', 
                 'Simon', 
                 'Richter']
half_grappler = ['Luigi', 
                 'Donkey Kong']
dynamic = ['Olimar', 
           'Shulk', 
           'Cloud', 
           'Inkling', 
           'Joker', 
           'Hero', 
           'Terry']
precision = ['Zelda', 
             'Marth']

# To make dictionaries of respective archetypes using list-object pairs 
AR_dict = archetype_creator(all_rounder)

HnR_dict = archetype_creator(hit_and_run)

rd_dict = archetype_creator(rushdown)

pressure_dict = archetype_creator(pressurer)

MU_dict = archetype_creator(mix_up)

ZB_dict = archetype_creator(zone_breaker)

dom_dict = archetype_creator(dominating)

foot_dict = archetype_creator(footsies)

gc_dict = archetype_creator(glass_cannon)

TT_dict = archetype_creator(tag_team)

psych_dict = archetype_creator(psychological)

zoner_dict = archetype_creator(zoner)

BnP_dict = archetype_creator(bait_and_punish)

trap_dict = archetype_creator(trapper)

turt_dict = archetype_creator(turtle)

KA_dict = archetype_creator(keep_away)

SC_dict = archetype_creator(stage_control)

HG_dict = archetype_creator(half_grappler)

dynamic_dict = archetype_creator(dynamic)

precision_dict = archetype_creator(precision)

# Creating a tk Class to make the application window
class Application(Frame):
    
    # Setting up the initial window where everything will be in
    def __init__(self, master=None, Frame=None):
        Frame.__init__(self, master)
        super(Application, self).__init__()
        self.grid(column = 5, row = 20, padx = 50, pady = 50, sticky = 'nsew')
        self.createWidgets()
    
    # To update the second drop-down menu based on selection of the first
    def getUpdateData(self, event):
        self.archetype_chosen['values'] = role_dict[self.role_chosen.get()]
    
    # To save the selection of the archetype and store it in a variable
    def save_selection(self, event):
        clicked = StringVar()
        clicked.trace('w', self.getUpdateData)
        output = clicked.get()
        #output = self.archetype_chosen.get()
        return output
    
    # Function to return a random character from a list based on user's selections    
    def getCharacter(self, event=None, *args):
        from random import choice
        temp_list = []
        if self.archetype_chosen.get() == 'Any':
            temp_list = full_roster
        elif self.archetype_chosen.get() == 'All-Rounder':
            temp_list = all_rounder
        elif self.archetype_chosen.get() == 'Rushdown':
            temp_list = rushdown
        elif self.archetype_chosen.get() == 'Pressurer':
            temp_list = pressurer
        elif self.archetype_chosen.get() == 'Hit and Run':
            temp_list = hit_and_run
        elif self.archetype_chosen.get() == 'Mix Up':
            temp_list = mix_up
        elif self.archetype_chosen.get() == 'Zone Breaker':
            temp_list = zone_breaker
        elif self.archetype_chosen.get() == 'Dominating':
            temp_list = dominating
        elif self.archetype_chosen.get() == 'Footsies':
            temp_list = footsies
        elif self.archetype_chosen.get() == 'Glass Cannon':
            temp_list = glass_cannon
        elif self.archetype_chosen.get() == 'Tag Team':
            temp_list = tag_team
        elif self.archetype_chosen.get() == 'Psychological':
            temp_list = psychological
        elif self.archetype_chosen.get() == 'Zoner':
            temp_list = zoner
        elif self.archetype_chosen.get() == 'Bait and Punish':
            temp_list = zoner
        elif self.archetype_chosen.get() == 'Trapper':
            temp_list = trapper
        elif self.archetype_chosen.get() == 'Turtle':
            temp_list = turtle
        elif self.archetype_chosen.get() == 'Keep Away':
            temp_list = keep_away
        elif self.archetype_chosen.get() == 'Stage Control':
            temp_list = stage_control
        elif self.archetype_chosen.get() == 'Half-Grappler':
            temp_list = half_grappler
        elif self.archetype_chosen.get() == 'Dynamic':
            temp_list = dynamic
        elif self.archetype_chosen.get() == 'Precision':
            temp_list = precision
        else:
            Label(text = "Looks like it didn't work. Please try again.").grid(row = 6, column = 1, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        try:
            from random import choice
            temp_char = choice(temp_list)
            print("Looks like you're playing " + temp_char + '!!')
            charinfo(temp_char)
        except IndexError: 
            error_lbl = Label(text = "Looks like you got an Index Error. \nIf it was intentional, HI! LOOK AT ME! I'M A SAFEGUARD. \nIf it wasn't intentional, hang in there bro. You almost got it! Just slowly work through it! \n\nIf you need an actual error code response: ").grid(row = 5, column = 1, padx = 5, pady = 5)

    # To create the Labels and Dropdown Menus to create selections from
    def createWidgets(self):
        Label(text = 'Please Select From the Following: ').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew')
        Label(text = 'Role').grid(row = 1, column = 0, sticky = 'nsew', padx = 5, pady = 5)
        Label(text = 'Playstyle').grid(row = 2, column = 0, sticky = 'nsew', padx = 5, pady = 5)
        
        clicked = StringVar()
        clicked.trace('w', self.save_selection)
        self.archetype_chosen = tkinter.ttk.Combobox()
        self.archetype_chosen.bind('<<ComboboxSelected>>', self.save_selection)
        self.archetype_chosen.grid(row = 2, column = 1, sticky = 'nsew')
        
        self.role_chosen = tkinter.ttk.Combobox(width = 20, values = list(role_dict.keys()))
        self.role_chosen.bind('<<ComboboxSelected>>', self.getUpdateData)
        self.role_chosen.grid(row = 1, column = 1, sticky = 'nsew')
            
        # Buttons used to submit/clear the user's responses
        submit_btn = Button(text = 'FIND ME A FIGHTER!', command = self.getCharacter)
        submit_btn.bind('<<ButtonClick>>', self.getCharacter)
        submit_btn.grid(row = 4, column = 1, padx = 5, pady = 5)
        
        

# To create a new Application-Class Object and its execution        
app = Application()
app.master.title('Who Should I Play in Smash Ultimate?')
app.mainloop()