class CharacterSheet:
    def __init__(self, name: str, char_class: str, level: int, strength: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int, skills: dict, feats: list, proficiencies: list, equipment: list, spellcasting: dict, background: str, personality: str, appearance: str, notes: str):
        self.name = name
        self.char_class = char_class
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.skills = skills
        self.feats = feats
        self.proficiencies = proficiencies
        self.equipment = equipment
        self.spellcasting = spellcasting
        self.background = background
        self.personality = personality
        self.appearance = appearance
        self.notes = notes

    def print_char_sheet(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class} (Level {self.level})")
        print("Ability Scores:")
        print(f"  Strength: {self.strength}")
        print(f"  Dexterity: {self.dexterity}")
        print(f"  Constitution: {self.constitution}")
        print(f"  Intelligence: {self.intelligence}")
        print(f"  Wisdom: {self.wisdom}")
        print(f"  Charisma: {self.charisma}")
        print("Skills:")
        for skill, modifier in self.skills.items():
            print(f"  {skill}: {modifier}")
        print("Feats:")
        for feat in self.feats:
            print(f"  {feat}")
        print("Proficiencies:")
        for proficiency in self.proficiencies:
            print(f"  {proficiency}")
        print("Equipment:")
        for item in self.equipment:
            print(f"  {item}")
        if self.spellcasting:
            print(f"Spellcasting [{self.spellcasting['ability']}]: {', '.join(self.spellcasting['spells'])}")
        print(f"Background: {self.background}")
        print(f"Personality: {self.personality}")
        print(f"Appearance: {self.appearance}")
        print(f"Notes: {self.notes}")