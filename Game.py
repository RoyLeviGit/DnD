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
            action = self.ui.get_input("Player: ")

            # If the action triggers an encounter, generate an enemy and handle the encounter
            if action == "explore":
                enemy_type, enemy_stats = self.dm.generate_encounter()
                self.ui.print_output(f"You have encountered a {enemy_type}! Stats: {enemy_stats}")

            # If the action triggers a conversation with an NPC, generate the NPC and handle the conversation
            elif action == "talk to NPC":
                npc = self.dm.generate_npc()
                self.ui.print_output(
                    f"You are speaking with {npc['name']}, "
                    f"who has {npc['appearance']} "
                    f"and a {npc['personality']} personality.\n"
                    f"{npc['info']}"
                )

            # If the action triggers a plot advancement, advance the plot
            elif action == "advance plot":
                self.ui.print_output(self.dm.advance_plot())

            elif len(action) > 1 and action[1] == "@":
                self.dm.react_to_action_request(action[1:], self.character_sheet)
                self.ui.print_output(self.dm.describe_scene(action[1:]))

            else:
                self.ui.print_output(self.dm.describe_scene(action))

