class CharacterSheet:
    def __init__(self, name: str, char_class: str, level: int, strength: int, dexterity: int, constitution: int,
                 intelligence: int, wisdom: int, charisma: int, skills: dict, feats: list, proficiencies: list,
                 equipment: list, spellcasting: dict, background: str, personality: str, appearance: str, notes: str):
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
        print("Abilities:")
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
        print(f"Spellcasting [{self.spellcasting['ability']}]:")
        for spell in self.spellcasting['spells']:
            print(f"  {spell}")
        print(f"Background: {self.background}")
        print(f"Personality: {self.personality}")
        print(f"Appearance: {self.appearance}")
        print(f"Notes: {self.notes}")

    def action_request_string(self):
        request_string = "Abilities: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma\n"

        request_string += "Skills:"
        for skill in self.skills.keys():
            request_string += " " + skill + ","
        request_string = request_string[:-1] + "\n"  # switch last ',' to '\n'

        request_string += "Feats:"
        for feat in self.feats:
            request_string += " " + feat + ","
        request_string = request_string[:-1] + "\n"  # switch last ',' to '\n'

        request_string += "Proficiencies:"
        for proficiency in self.proficiencies:
            request_string += " " + proficiency + ","
        request_string = request_string[:-1] + "\n"  # switch last ',' to '\n'

        request_string += "Equipment:"
        for item in self.equipment:
            request_string += " " + item + ","
        request_string = request_string[:-1] + "\n"  # switch last ',' to '\n'

        request_string += "Spellcasting:"
        for spell in self.spellcasting['spells']:
            request_string += " " + spell + ","
        request_string = request_string[:-1] + "\n"  # switch last ',' to '\n'

        return request_string
