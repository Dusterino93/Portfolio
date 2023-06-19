import Smash_Classes

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

# These functions create dictionaries using lists as keys and class objects as values.
def archetype_creator(characters):
    '''Creates a dictionary from a list as String-Class pair with all the instance attributes therein.
    Also checks during each loop iteration if the item/char/character is within specific lists in 
    order to create the specific key-value pairs.
    
    Parameters
    ----------
    characters : list
        list of strings, specifically names of characters to use the "key" in the dictionary
        
    Returns
    -------
    temp_dict : dictionary
        temporary dictionary containing the names of each respective character and their associative archetype clases.
    '''
    temp_dict = {}
    for char in characters:
        if char not in temp_dict:
            if characters == all_rounder:
                char_entry = {char : Smash_Classes.AllRounder(name = char, role = 'Offensive', playstyle = 'All Rounder', specialty = 'Easy to Learn, Jack of all Trades.')}
            elif characters == rushdown:
                char_entry = {char : Smash_Classes.Rushdown(name = char, role = 'Offensive', playstyle = 'Rushdown', specialty = 'Close-Range Combat & Juggling.')}
            elif characters == pressurer:
                char_entry = {char : Smash_Classes.Pressurer(name = char, role = "Offensive", playstyle = 'Pressurer', specialty = 'High Damage Combos, Openings/Weaknesses Exploitation.')}
            elif characters == hit_and_run:
                char_entry = {char : Smash_Classes.HitAndRun(name = char, role = "Offensive", playstyle = 'Hit and Run', specialty = "Fast. Good at for punishing opponent's mistakes.")}
            elif characters == mix_up:
                char_entry = {char : Smash_Classes.MixUp(name = char, role = "Offensive", playstyle = 'Mix-Up', specialty = 'Versatile Moveset based on Tactics and Mind Games with Opponent')}
            elif characters == zone_breaker:
                char_entry = {char : Smash_Classes.ZoneBreaker(name = char, role = "Offensive", playstyle = 'Zone Breaker', specialty = 'Combines a little bit of Rushdown, Pressurerer, Hit & Run, and Mix-Up Tactics. \nCan quickly disrupt opponents and approach from a safe distance.')}
            elif characters == dominating:
                char_entry = {char : Smash_Classes.Dominating(name = char, role = "Offensive", playstyle = 'Dominating', specialty = 'Very high power, with exploitable weaknesses. Does not suffer from low defenses, though.')}
            elif characters == footsies:
                char_entry = {char : Smash_Classes.Footsies(name = char, role = "Offensive", playstyle = 'Footsies', specialty = 'Superior priority and/or speed on the ground. Less combo-oriented.')}
            elif characters == glass_cannon:
                char_entry = {char : Smash_Classes.GlassCannon(name = char, role = "Offensive", playstyle = 'Glass Cannon', specialty = 'Have very powerful attacks, but equally low defenses.')}
            elif characters == tag_team:
                char_entry = {char : Smash_Classes.TagTeam(name = char, role = "Offensive", playstyle = 'Tag Team', specialty = 'Has a partner. Great for combo-ing, but very low defenses.')}
            elif characters == psychological:
                char_entry = {char : Smash_Classes.Psych(name = char, role = "Offensive", playstyle = 'Psychological', specialty = 'Extremely annoying with spammable moves + Very hard to kill.')}
            elif characters == zoner:
                char_entry = {char : Smash_Classes.Zoner(name = char, role = 'Defensive', playstyle = 'Zoner', specialty = 'Good at controlling the stage. Lots of tools with range.')}
            elif characters == bait_and_punish:
                char_entry = {char : Smash_Classes.BaitAndPunish(name = char, role = 'Defensive', playstyle = 'Bait & Punish', specialty = 'Opponent Conditioning + Punishing it.')}
            elif characters == trapper:
                char_entry = {char : Smash_Classes.Trapper(name = char, role = 'Defensive', playstyle = 'Trapper', specialty = 'Traps that apply lots of pressure. Can attack while facing away & evading opponents.')}
            elif characters == turtle:
                char_entry = {char : Smash_Classes.Turtle(name = char, role = 'Defensive', playstyle = 'Turtle', specialty = 'Focused on wearing down opponents from afar or with indirect moves.')}
            elif characters == keep_away:
                char_entry = {char : Smash_Classes.KeepAway(name = char, role = 'Defensive', playstyle = 'Keep Away', specialty = 'Excels at being very annoying and getting in and out of places quickly.')}
            elif characters == stage_control:
                char_entry = {char : Smash_Classes.StageControl(name = char, role = 'Defensive', playstyle = 'Stage Control', specialty = 'Combo of Trapper, Turtle, and Keep-Away archetypes. Control the stage.')}
            elif characters == half_grappler:
                char_entry = {char : Smash_Classes.HalfGrappler(name = char, role = 'Defensive', playstyle = 'Half-Grappler', specialty = 'Heavy focus on grabs and throws.')}
            elif characters == dynamic:
                char_entry = {char : Smash_Classes.Dynamic(name = char, role = "Flexible", playstyle = 'Dynamic', specialty = 'Tend to have unique quirk or ability that greatly affects play strategy like power-ups or certain tools.')}
            elif characters == precision:
                char_entry = {char : Smash_Classes.Precision(name = char, role = "Flexible", playstyle = 'Precision', specialty = 'Relies on specific sweetspots in order to deal their full damage.')}
            temp_dict.update(char_entry)
        elif char in characters in temp_dict:
            continue
    return temp_dict

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

# To obtain the character info the character
def charinfo(char):
    '''The function checks to see which archetype-dictionary the character belongs to and prints out a small exerpt of how to play characters of that archetype. The names of the characters are stored as a string in their respective dictionaries as keys with the class objects of their respective archetypes stored as values within their associated dictionary.
    
    Parameters
    ----------
    char : string
        The name of the character (i.e., 'Mario', 'Luigi', 'Pikachu', etc.)
        
    Returns
    -------
    The information of the character printed as
    
    Name: (insert character name here)
    Role: (i.e., 'Offensive', 'Defensive', or 'Flexible')
    Playstye: (i.e., 'All-Rounder, 'Zoner', etc.)
    Specialty: (i.e., 'Easy to learn, but hard to master. Jack of all trades, master of none.')
    '''
    
    if char in AR_dict:
        output = AR_dict[char].info()
    elif char in rd_dict:
        output = rd_dict[char].info()
    elif char in pressure_dict:
        output = pressure_dict[char].info()
    elif char in HnR_dict:
        output = HnR_dict[char].info()
    elif char in MU_dict:
        output = MU_dict[char].info()
    elif char in ZB_dict:
        output = ZB_dict[char].info()
    elif char in dom_dict:
        output = dom_dict[char].info()
    elif char in foot_dict:
        output = foot_dict[char].info()
    elif char in gc_dict:
        output = gc_dict[char].info()
    elif char in TT_dict:
        output = TT_dict[char].info()
    elif char in psych_dict:
        output = psych_dict[char].info()
    elif char in zoner_dict:
        output = zoner_dict[char].info()
    elif char in BnP_dict:
        output = BnP_dict[char].info()
    elif char in trap_dict:
        output = trap_dict[char].info()
    elif char in turt_dict:
        output = turt_dict[char].info()
    elif char in KA_dict:
        output = KA_dict[char].info()
    elif char in SC_dict:
        output = SC_dict[char].info()
    elif char in HG_dict:
        output = HG_dict[char].info()
    elif char in dynamic_dict:
        output = dynamic_dict[char].info()
    elif char in precision_dict:
        output = precision_dict[char].info()
    elif type(char) != str:
        print('Please try entering the name again with quotations at the ends.')
    else:
        print('Character not found. Please try again.').grid(row = 6, column = 1, padx = 5, pady = 5)
    return output