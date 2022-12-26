from GPitput import GPitput


class DungeonMaster:
    def __init__(self):
        self.last_scene = ""
        g_pitput_scene_setting = {
            "dialogue_opening": "The following is a conversation with a DnD Dungeon Master (DM). "
                                "The DM is creative, clever, "
                                "and never decides the actions for the players.\n\n",
            "asker": "Player: ",
            "responser": "DM: "
        }
        self.g_pitput_scene = GPitput(setting=g_pitput_scene_setting,
                                      name="Scene",
                                      max_history_length=1)

        action_response_settings = {
            "dialogue_opening": "The following is a conversation with a DnD Dungeon Master (DM). "
                                "The DM is creative, clever, and never decides the actions for the players.\n"
                                "All the DM does is given context, a player action, and character sheet "
                                "he answers with the minimal(!) relevant character sheet entries "
                                "in this format and nothing else!:\n"
                                "DM: <list_entry1>: <list_entry1_group>\n"
                                "...\n"
                                "<list_entryN>: <list_entryN_group>\n"
                                "Or this format and nothing else!:\n"
                                "DM: Can't do action: <reason>\n\n"
                                "Character sheet: "
                                "Abilities: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma\n"
                                "Skills: Nature, Investigation, Religion, Survival, Acrobatics, Animal Handling, "
                                "Intimidation, Athletics, Deception, Insight, Sleight of Hand\n"
                                "Feats: Mobile, Dual Wielder, Inspiring Leader\n"
                                "Proficiencies: Shields, Simple weapons, Thieves' tools, "
                                "Musical instruments, All armor\n"
                                "Equipment: Longbow, Wand, Shortbow, Longsword, Potion of healing, Leather armor, "
                                "Shield, Staff\n"
                                "Spellcasting: Telepathy, True Resurrection, Suggestion\n"
                                "Context: You approach the pedestal and can make out a strange symbol carved "
                                "into the top. The symbol appears to be a spiral with a single eye in the center. "
                                "The pedestal is made of a dark stone and is cold to the touch. As you get closer, "
                                "you can hear a faint humming sound coming from within the pedestal\n"
                                "Player: jump to space and back\n"
                                "DM: Can't do action: You don't have any abilities, skills, feats, proficiencies, "
                                "equipment, or spells that would allow you to jump to space and back. "
                                "There is no context in the provided character sheet or the given situation "
                                "that would allow for such an action.\n"
                                "Player: do nothing\n"
                                "DM: \n"
                                "Player: break pedestal\n"
                                "DM: Abilities: Strength\n"
                                "Skills: Athletics\n\n",
            "asker": "",
            "responser": "DM: "
        }
        self.g_pitput_action_response = GPitput(setting=action_response_settings,
                                                name="ActionResponse",
                                                max_history_length=1)

    def describe_opening_scene(self):
        opening_scene = self.g_pitput_scene.chat("describe opening scene", temperature=1)
        self.last_scene = opening_scene
        return opening_scene

    def react_to_action_request(self, action, character_sheet):
        action_request = f"Character sheet: {character_sheet.action_request_string()}\n" \
                         f"Context: {self.last_scene}\n" \
                         f"Player: {action}"
        return self.g_pitput_action_response.chat(action_request,
                                                  temperature=0,
                                                  stop_seq=["Character sheet:", "Context:", "Player:"])

    def describe_scene(self, action):
        scene = self.g_pitput_scene.chat(f"{action}. describe scene")
        self.last_scene = scene
        return scene

    def advance_plot(self):
        plot_advancement = self.g_pitput_scene.chat("advance plot")
        self.last_scene = plot_advancement
        return plot_advancement

    def generate_npc(self):
        npc_name = self.g_pitput_scene.chat("generate name for NPC", max_tokens=8)
        npc_appearance = self.g_pitput_scene.chat("describe NPC appearance", max_tokens=30)
        npc_personality = self.g_pitput_scene.chat("describe NPC personality", max_tokens=30)
        npc_info = self.g_pitput_scene.chat("provide important information or quest objectives for NPC")
        return {"name": npc_name, "appearance": npc_appearance, "personality": npc_personality, "info": npc_info}

    def generate_encounter(self):
        enemy_type = self.g_pitput_scene.chat("generate enemy type", max_tokens=8)
        enemy_stats = self.g_pitput_scene.chat("generate statblock")
        return enemy_type, enemy_stats

    def generate_loot(self):
        loot_item = self.g_pitput_scene.chat("generate loot item", max_tokens=8)
        return loot_item
