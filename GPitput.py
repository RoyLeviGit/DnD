import os
import openai

from Logger import Logger


class GPitput:
    def __init__(self, setting=None):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.__setting = setting if setting is not None else {
            "dialogue_opening": "The following is a conversation with a DnD Dungeon Master (DM). "
                                "The DM is creative, clever, "
                                "and never decides the actions for the players.\n\n",
            "asker": "Players: ",
            "responser": "DM: "
        }
        self.__history = {
            "ask": [],
            "response": []
        }
        self.__logger = Logger(__class__.__name__)

    def chat(self, ask, max_tokens=128, temperature=0.2):
        prompt = self.__generate_prompt(ask)
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
            # TODO stop=self.__setting["asker"]
        )
        response = completions.choices[0].text
        self.__history["ask"].append(response)
        self.__history["response"].append(response)

        self.__log(ask, prompt, response)

        return response

    def __generate_prompt(self, ask):
        prompt = self.__setting["dialogue_opening"]
        for hist_ask, hist_resp in zip(self.__history["ask"], self.__history["response"]):
            prompt += self.__setting["asker"] + hist_ask + "\n"
            prompt += self.__setting["responser"] + hist_resp + "\n"

        if len(prompt) > 4096:
            print("Reached maximum history")
            # TODO better history management
            self.__clear_history()
            prompt = self.__setting["dialogue_opening"]

        prompt += self.__setting["asker"] + ask + "\n" + self.__setting["responser"]
        return prompt

    def __clear_history(self):
        self.__history["ask"] = []
        self.__history["response"] = []

    def __log(self, ask, prompt, response):
        self.__logger.log(ask, "ask")
        self.__logger.log(prompt, "prompt")
        self.__logger.log(response, "response")
