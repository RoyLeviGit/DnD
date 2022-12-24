from GPitput import GPitput


class DungeonMaster:
    def __init__(self):
        self.g_pitput = GPitput()

    def describe_opening_scene(self):
        opening_scene = self.g_pitput.chat("describe opening scene")
        return opening_scene

    def describe_action_scene(self, action):
        return self.g_pitput.chat(f"Player 1: {action}\ndescribe scene")

    def handle_player_choice(self, choice):
        result = self.g_pitput.chat(f"Player 1: {choice}\ndescribe result")
        return result

    def advance_plot(self):
        plot_advancement = self.g_pitput.chat("advance plot")
        return plot_advancement

    def generate_npc(self):
        npc_name = self.g_pitput.chat("generate name for NPC", max_tokens=5)
        npc_appearance = self.g_pitput.chat("describe NPC appearance", max_tokens=64)
        npc_personality = self.g_pitput.chat("describe NPC personality", max_tokens=64)
        npc_info = self.g_pitput.chat("provide important information or quest objectives for NPC", max_tokens=128)
        return {"name": npc_name, "appearance": npc_appearance, "personality": npc_personality, "info": npc_info}

    def generate_encounter(self):
        enemy_type = self.g_pitput.chat("generate enemy type", max_tokens=5)
        enemy_stats = self.g_pitput.chat("generate enemy stats", max_tokens=128)
        return enemy_type, enemy_stats

    def generate_loot(self):
        loot_item = self.g_pitput.chat("generate loot item", max_tokens=5)
        return loot_item
