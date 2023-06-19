# Meant to be a general umbrella class that allows the character to call upon itself
class character():
    '''An umbrella class that encompasses all Super Smash Bros. characters. Allows them all to call upon themselves with their name, role, playstyle, and the specialty of their assigned subclass
    
    Parameters
    ----------
    Doesn't really have any since it's a Class.
    
    Return
    ------
    Returns an object with the ability to call upon itself and relay its role, playstyle, and archetype specialty by using self.(insert attribute).
    '''
    
    def __init__(self, name, role=None, playstyle=None, specialty=None):
        self.name = name
        self.role = role
        self.playstyle = playstyle
        self.specialty = specialty
    
    
    # Creating a method/function to be able to call up characteristics of the character
    def info(self):
        print('Name:' + '\t' + self.name + '\nRole:' + '\t' + 
              self.role + '\nPlaystyle:' + '\t' + self.playstyle +  '\nSpecialty:' + '\t' + self.specialty)
    

    # Create subclasses of "Offensive" characters. Each one has specific instance attributes related to how they play. 
class AllRounder(character):
    '''Defines the All-Rounder class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.
    '''
    
    def __init__(self, name, role = "Offensive", playstyle = 'All Rounder', specialty = 'Easy to Learn,  Jack of All Trades.'):
        super().__init__(name, role, playstyle, specialty)


class Rushdown(character):
    '''Defines the All-Rounder class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.
    '''
        
class Pressurer(character):
    '''Defines the Pressurer Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''

    def __init__(self, name, role = "Offensive", playstyle = 'Pressurer', specialty = 'High Damage Combos, Openings/Weaknesses Exploitation.'):
        super().__init__(name, role, playstyle, specialty)
        
        
class HitAndRun(character):
    '''Defines the Hit and Run Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Hit and Run', specialty = "Fast. Good at for punishing opponent's mistakes."):
        super().__init__(name, role, playstyle, specialty)

        
class MixUp(character):
    '''Defines the Mix Up Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Mix-Up', specialty = 'Versatile Moveset based on Tactics and Mind Games with Opponent'):
        super().__init__(name, role, playstyle, specialty)
        
        
class ZoneBreaker(character):
    '''Defines the Zone Breaker Class, an Offensive Subclass.'''
    def __init__(self, name, role = "Offensive", playstyle = 'Zone Breaker', specialty = 'Combines a little bit of Rushdown, Pressurerer, Hit & Run, and Mix-Up Tactics. \nCan quickly disrupt opponents and approach from a safe distance.'):
        super().__init__(name, role, playstyle, specialty)

        
class Dominating(character):
    '''Defines the Dominating Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Dominating', specialty = 'Very high power, with exploitable weaknesses. Does not suffer from low defenses, though.'):
        super().__init__(name, role, playstyle, specialty)

        
class Footsies(character):
    '''Defines the Footsies Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Footsies', specialty = 'Superior priority and/or speed on the ground. Less combo-oriented.'):
        super().__init__(name, role, playstyle, specialty)

        
class GlassCannon(character):
    '''Defines the Glass Cannon Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Glass Cannon', specialty = 'Have very powerful attacks, but equally low defenses.'):
        super().__init__(name, role, playstyle, specialty)

        
class TagTeam(character):
    '''Defines the Tag-Team Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Tag Team', specialty = 'Has a partner. Great for combo-ing, but very low defenses.'):
        super().__init__(name, role, playstyle, specialty)

        
class Psych(character):
    '''Defines the Psychological Class, an Offensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Offensive", playstyle = 'Psychological', specialty = 'Extremely annoying with spammable moves + Very hard to kill.'):
        super().__init__(name, role, playstyle, specialty)             

        
# Create subclasses of "Defensive" characters. Each one has specific instance attributes related to how they play. 
class Zoner(character):
    '''Defines the Zoner Class, a Defensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = 'Defensive', playstyle = 'Zoner', specialty = 'Good at controlling the stage. Lots of tools with range.'):
        super().__init__(name, role, playstyle, specialty)

        
class BaitAndPunish(character):
    '''Defines the Bait & Punish Class, a Defensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = 'Defensive', playstyle = 'Bait & Punish', specialty = 'Opponent Conditioning + Punishing it.'):
        super().__init__(name, role, playstyle, specialty)

        
class Trapper(character):
    '''Defines the Trapper Class, a Defensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = 'Defensive', playstyle = 'Trapper', specialty = 'Traps that apply lots of pressure. Can attack while facing away & evading opponents.'):
        super().__init__(name, role, playstyle, specialty)

        
class Turtle(character):
    '''Defines the Turtle Class, a Defensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = 'Defensive', playstyle = 'Turtle', specialty = 'Focused on wearing down opponents from afar or with indirect moves.'):
        super().__init__(name, role, playstyle, specialty)

        
class KeepAway(character):
    '''Defines the Keep Away Class, a Defensive Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = 'Defensive', playstyle = 'Keep Away', specialty = 'Excels at being very annoying and getting in and out of places quickly.'):
        super().__init__(name, role, playstyle, specialty)
        
        
class StageControl(character):
    '''Defines the Stage Control Class, a Defensive Subclass.
    
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = 'Defensive', playstyle = 'Stage Control', specialty = 'Combo of Trapper, Turtle, and Keep-Away archetypes. Control the stage.'):
        super().__init__(name, role, playstyle, specialty)

        
class HalfGrappler(character):
    '''Defines the Half-Grappler Class, a Defensive Subclass.'''
    def __init__(self, name, role = 'Defensive', playstyle = 'Half-Grappler', specialty = 'Heavy focus on grabs and throws.'):
        super().__init__(name, role, playstyle, specialty)

        
# Create subclasses of "Flexible" characters. Each one has specific instance attributes related to how they play. class flexible(character):
class Dynamic(character):
    '''Defines the Dynamic class, a Flexible Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Flexible", playstyle = 'Dynamic', specialty = 'Tend to have unique quirk or ability that greatly affects play strategy like power-ups or certain tools.'):
        super().__init__(name, role, playstyle, specialty)
    
    
class Aura(character):
    '''Defines the Aura class, a Flexible Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    Note: There is currently only one character that is considered an 'Aura' or at least uses 'Aura' attacks in the game. As such, it seemed like a waste since their playstyle is much more intricate than simply a character that uses an 'Aura' mechanic. This class was intentionally left here in case the game decides to add more characters of similar playstyles. Until then, the default values are set to the only character that uses it currently, even though the character, 'Lucario' is classified a different subtype. Furthermore, in reality, like 'Lucario', all characters have overlapping characteristics and archetypes, so these subclasses were decided based on which class better represented them the most.
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name = 'Lucario', role = 'Flexible', playstyle = 'Aura', specialty = 'Exclusive to Lucario. Attacks get stronger as percentage gets higher.'):
        super().__init__(name, role, playstyle, specialty)
        
        
class Precision(character):
    '''Defines the Precision class, a Flexible Subclass.
    
    Parameters
    ----------
    character : the umbrella 'Character' class. Denotes that it inherits all the attributes of that class.
    
    
    Return
    ------
    Class object with default values for role, playstyle, and specialty attributes.'''
    
    def __init__(self, name, role = "Flexible", playstyle = 'Precision', specialty = 'Relies on specific sweetspots in order to deal their full damage.'):
        super().__init__(name, role, playstyle, specialty)