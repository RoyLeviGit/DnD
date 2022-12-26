from UI import UI
from CharacterGenerator import CharacterGenerator
from DungeonMaster import DungeonMaster


class Game:
    def __init__(self):
        # Create an instance of the UI class
        self.ui = UI()

        # Create an instance of the CharacterSheet class
        self.character_sheet = CharacterGenerator().generate_character()
        self.character_sheet.print_char_sheet()
        print('\n\n')

        # Create an instance of the DungeonMaster class
        self.dm = DungeonMaster()

        # Start the game by describing the opening scene
        self.ui.print_output(self.dm.describe_opening_scene())

    def game_loop(self):
        # Allow the players to take actions and describe the scene after each action
        while True:
            player_action = self.ui.get_input("Player: ")

            # If the action triggers an encounter, generate an enemy and handle the encounter
            if player_action == "explore":
                enemy_type, enemy_stats = self.dm.generate_encounter()
                self.ui.print_output(f"You have encountered a {enemy_type}! Stats: {enemy_stats}")

            # If the action triggers a conversation with an NPC, generate the NPC and handle the conversation
            elif player_action == "talk to NPC":
                npc = self.dm.generate_npc()
                self.ui.print_output(
                    f"{npc['name']}\n"
                    f"{npc['appearance']}\n"
                    f"{npc['personality']}\n"
                    f"{npc['info']}"
                )

            # If the action triggers a plot advancement, advance the plot
            elif player_action == "":
                self.ui.print_output(self.dm.advance_plot())

            # If the hook to disable action check, just advance scene
            elif len(player_action) > 1 and player_action[0] == "@":
                self.ui.print_output(self.dm.describe_scene(player_action[1:]))

            else:
                # Action check
                dm_reaction = self.dm.react_to_action_request(player_action, self.character_sheet)
                self.__act_by_rules(player_action, dm_reaction)

    def __act_by_rules(self, player_action, dm_reaction):
        if "Can't do action:" in dm_reaction:
            self.ui.print_output(dm_reaction)
            self.ui.print_output("Try a different action")
            return

        abilities, skills = self.__get_abilities_skills(dm_reaction)
        if len(abilities) > 0:
            # roll abilities dice
            pass
        if len(skills) > 0:
            # roll skills dice
            pass

        if len(abilities) > 0 or len(skills) > 0:
            self.ui.print_output("Relevant abilities and skills:" + dm_reaction)
        else:
            self.ui.print_output(dm_reaction)

        self.ui.print_output(self.dm.describe_scene(player_action))

    def __get_abilities_skills(self, dm_reaction):
        abilities = []
        skills = []
        for line in dm_reaction.split("\n"):
            if "Abilities:" in line:
                abilities = [ability.split() for ability in line.split(":")[1].strip().split(",")]
            elif "Skills:" in line:
                skills = [skill.split() for skill in line.split(":")[1].strip().split(",")]
        return abilities, skills
