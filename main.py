from UI import UI
from CharacterGenerator import CharacterGenerator
from DungeonMaster import DungeonMaster


def play_game():
    # Create an instance of the UI class
    ui = UI()
    # Create an instance of the DungeonMaster class
    dm = DungeonMaster()

    # Start the game by describing the opening scene
    ui.print_output(dm.describe_opening_scene())

    # Allow the players to take actions and describe the scene after each action
    while True:
        action = ui.get_input("Enter your action: ")
        ui.print_output(dm.describe_action_scene(action))

        # If the action triggers an encounter, generate an enemy and handle the encounter
        if action == "explore":
            enemy_type, enemy_stats = dm.generate_encounter()
            ui.print_output(f"You have encountered a {enemy_type}!")
            while enemy_stats["hit points"] > 0:
                choice = ui.get_input("Enter your action: ")
                result = dm.handle_player_choice(choice)
                ui.print_output(result)
                if "defeated the enemy" in result:
                    break
            if enemy_stats["hit points"] <= 0:
                ui.print_output("You have defeated the enemy!")
                ui.print_output(f"You have found {dm.generate_loot()}!")

        # If the action triggers a conversation with an NPC, generate the NPC and handle the conversation
        elif action == "talk to NPC":
            npc = dm.generate_npc()
            ui.print_output(
                f"You are speaking with {npc['name']}, "
                f"who has {npc['appearance']} "
                f"and a {npc['personality']} personality.")
            ui.print_output(npc['info'])
            while True:
                choice = ui.get_input("Enter your conversation action: ")
                result = dm.handle_player_choice(choice)
                ui.print_output(result)
                if "ending the conversation" in result:
                    break

        # If the action triggers a plot advancement, advance the plot
        elif action == "advance plot":
            ui.print_output(dm.advance_plot())


def print_hi():
    CharacterGenerator.generate_character(CharacterGenerator()).print_char_sheet()
    print('\n\n')


if __name__ == '__main__':
    print_hi()
    play_game()
