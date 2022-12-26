import random

from Dice import DnDDice
from CharacterSheet import CharacterSheet


class CharacterGenerator:
    def __init__(self):
        self.Dice = DnDDice()
        self.classes = ["Fighter", "Wizard", "Rogue", "Cleric", "Paladin", "Bard"]
        self.skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight",
                       "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion",
                       "Religion", "Sleight of Hand", "Stealth", "Survival"]
        self.feats = ["Actor", "Alert", "Athlete", "Charger", "Crossbow Expert", "Defensive Duelist", "Dual Wielder",
                      "Dungeon Delver", "Durable", "Elemental Adept", "Grappler", "Great Weapon Master", "Healer",
                      "Heavily Armored", "Heavy Armor Master", "Inspiring Leader", "Keen Mind", "Lightly Armored",
                      "Linguist", "Lucky", "Mage Slayer", "Magic Initiate", "Martial Adept", "Medium Armor Master",
                      "Mobile", "Moderately Armored", "Mounted Combatant", "Observant", "Polearm Master", "Resilient",
                      "Ritual Caster", "Savage Attacker", "Sentinel", "Shield Master", "Skulker", "Spell Sniper",
                      "Tavern Brawler", "Tough", "War Caster", "Weapon Master"]
        self.equipment = ["Chain mail", "Leather armor", "Longbow", "Longsword", "Potion of healing", "Shield",
                          "Shortbow", "Short sword", "Staff", "Wand"]
        self.spells = {
            "Intelligence": ["Acid Arrow", "Blindness/Deafness", "Continual Flame", "Darkness", "Detect Magic",
                             "Detect Thoughts", "Gentle Repose", "Identify", "Invisibility", "Knock", "Levitate",
                             "Locate Object", "Melf's Minute Meteors", "Mislead", "Modify Memory", "Nondetection",
                             "Phantom Steed", "Polymorph", "Scrying", "Sending", "Suggestion", "Telekinesis",
                             "Telepathy", "True Resurrection"],
            "Wisdom": ["Animal Friendship", "Augury", "Calm Emotions", "Charm Person", "Commune", "Control Water",
                       "Create or Destroy Water", "Cure Wounds", "Death Knell", "Detect Evil and Good",
                       "Detect Poison and Disease", "Divination", "Divine Favor", "Entangle", "Find Traps", "Goodberry",
                       "Grave Dirt", "Heal", "Invisibility to Undead", "Lesser Restoration", "Life Transference",
                       "Locate Animals or Plants", "Locate Object", "Locate Undead", "Longstrider", "Magic Weapon",
                       "Mending", "Purify Food and Drink", "Raise Dead", "Remove Curse", "Remove Disease",
                       "Remove Poison", "Revivify", "Sanctuary", "Searing Smite", "Shield of Faith", "Silence",
                       "Speak with Dead", "Speak with Plants", "Stinking Cloud", "Stoneskin", "Suggestion", "Sunburst",
                       "Tongues", "True Resurrection", "True Seeing", "Zone of Truth"],
            "Charisma": ["Animal Friendship", "Bane", "Bless", "Chaos Bolt", "Charm Person", "Command",
                         "Compelled Duel", "Compelling Argument", "Crown of Madness", "Cure Wounds", "Dancing Lights",
                         "Darkness", "Daze", "Death Knell", "Delay Poison", "Detect Thoughts", "Dimension Door",
                         "Disguise Self", "Disintegrate", "Divine Favor", "Eldritch Blast", "Enthrall",
                         "Expeditious Retreat", "Fear", "Friends", "Gaseous Form", "Geas", "Gust of Wind", "Heal",
                         "Hold Person", "Inflict Wounds", "Invisibility", "Lesser Restoration",
                         "Locate Animals or Plants", "Locate Object", "Mage Armor", "Magic Missile", "Magic Weapon",
                         "Minor Illusion", "Mislead", "Misty Step", "Modify Memory", "Nondetection",
                         "Pass without Trace", "Polymorph", "Prayer of Healing", "Prestidigitation", "Raise Dead",
                         "Ray of Frost", "Remove Curse", "Remove Disease", "Resurrection", "Revivify", "Scorching Ray",
                         "Searing Smite", "See Invisibility", "Shield", "Shield of Faith", "Silence", "Sleep"]
        }
        self.proficiencies = ["All armor", "Shields", "Simple weapons", "Martial weapons", "Musical instruments",
                              "Thieves' tools"]
        self.backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit",
                            "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]
        self.personality_traits = ["Brave", "Curious", "Determined", "Energetic", "Friendly", "Generous", "Gentle", "Happy",
                                   "Introverted", "Loyal", "Optimistic", "Patient", "Protective", "Quiet", "Resourceful",
                                   "Sensitive", "Thoughtful", "Understanding"]
        self.appearance_details = ["Tall", "Short", "Muscular", "Lean", "Curvy", "Petite", "Pale", "Tan", "Olive", "Dark",
                                   "Light", "Short", "Long", "Curly", "Straight", "Wavy", "Spiky", "Smooth"]


    def generate_character(self):
        name = self.generate_name()
        char_class = self.generate_class()
        level = self.generate_level()
        strength = self.generate_ability_score()
        dexterity = self.generate_ability_score()
        constitution = self.generate_ability_score()
        intelligence = self.generate_ability_score()
        wisdom = self.generate_ability_score()
        charisma = self.generate_ability_score()
        skills = self.generate_skills(intelligence)
        feats = self.generate_feats(level)
        proficiencies = self.generate_proficiencies()
        equipment = self.generate_equipment()
        spellcasting = self.generate_spellcasting()
        background = self.generate_background()
        personality = self.generate_personality()
        appearance = self.generate_appearance()
        notes = self.generate_notes()

        return CharacterSheet(name, char_class, level, strength, dexterity, constitution, intelligence, wisdom,
                              charisma, skills, feats, proficiencies, equipment, spellcasting, background, personality,
                              appearance, notes)

    def generate_name(self):
        # Generate a random name
        return "John Doe"

    def generate_class(self):
        # Randomly select a class from the list of available classes
        return random.choice(self.classes)

    def generate_level(self):
        # Randomly generate a level between 1 and 20
        return self.Dice.roll_d20()

    def generate_ability_score(self):
        # Roll 4 6-sided dice and sum the results, then add the highest 3 rolls together
        return self.Dice.roll_top("d6", 4, 3)

    def generate_skills(self, intelligence):
        # Randomly select a number of skills equal to the character's intelligence modifier
        num_skills = intelligence
        skills = {}
        for _ in range(num_skills):
            skill = random.choice(self.skills)
            skills[skill] = 1
        return skills

    def generate_feats(self, level):
        # Randomly select a number of feats equal to the character's level
        num_feats = level
        feats = []
        for _ in range(num_feats):
            feat = random.choice(self.feats)
            feats.append(feat)
        return feats

    def generate_proficiencies(self):
        # Randomly select a number of proficiencies from the list of available proficiencies
        num_proficiencies = self.Dice.roll_d4()
        return random.sample(self.proficiencies, num_proficiencies)

    def generate_equipment(self):
        # Randomly select a number of items from the list of available equipment
        num_items = self.Dice.roll_d4()
        return random.sample(self.equipment, num_items)

    def generate_spellcasting(self):
        # Generate a random spellcasting ability and list of known spells
        spellcasting_ability = random.choice(["Intelligence", "Wisdom", "Charisma"])
        # Roll 3 4-sided dice and sum the results, then add the highest 2 rolls together
        num_spells = self.Dice.roll_top("d4", 3, 2)
        spells = []
        for i in range(num_spells):
            spells.append(random.choice(self.spells[spellcasting_ability]))
        return {"ability": spellcasting_ability, "spells": spells}

    def generate_background(self):
        # Generate a random background for the character
        return random.choice(self.backgrounds)

    def generate_personality(self):
        # Randomly select a personality trait from a list of options
        return random.choice(self.personality_traits)

    def generate_appearance(self):
        # Randomly select an appearance detail from a list of options
        return random.choice(self.appearance_details)

    def generate_notes(self):
        # Generate a random note
        return "I used to be an adventurer like you, then I took an arrow in the knee."


