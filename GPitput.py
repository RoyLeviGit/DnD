import os
import openai

from Logger import Logger


class GPitput:
    def __init__(self, setting=None, name="", max_history_length=None):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.__setting = setting if setting is not None else {
            "dialogue_opening": "The following is a conversation with a DnD Dungeon Master (DM). "
                                "The DM is creative, clever, "
                                "and never decides the actions for the players.\n\n",
            "asker": "Player: ",
            "responser": "DM: "
        }
        self.__history = {
            "ask": [],
            "response": []
        }
        self.__max_history_length = max_history_length
        self.__logger = Logger(f"{__class__.__name__}{name}")

    def chat(self, ask, max_tokens=100, temperature=0.8, stop_seq=None):
        prompt = self.__generate_prompt(ask)
        stop_seq = self.__generate_stop_sequence(stop_seq)
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop_seq
        )
        response = completions.choices[0].text

        self.__append_to_history(ask, response)
        self.__log(ask, prompt, response)

        return response

    def __generate_prompt(self, ask):
        prompt = self.__setting["dialogue_opening"]
        for hist_ask, hist_resp in zip(self.__history["ask"], self.__history["response"]):
            prompt += self.__setting["asker"] + hist_ask + "\n"
            prompt += self.__setting["responser"] + hist_resp + "\n"

        if len(prompt) > 4096:
            print("Reached maximum history")
            self.__shorten_history()
            return self.__generate_prompt(ask)

        prompt += self.__setting["asker"] + ask + "\n" + self.__setting["responser"]
        return prompt

    def __generate_stop_sequence(self, stop_seq):
        if stop_seq is None:
            stop_seq = []
        if len(self.__setting["asker"]) > 0:
            stop_seq += [self.__setting["asker"]]

        if len(self.__setting["responser"]) > 0:
            stop_seq += [self.__setting["responser"]]

        return stop_seq

    def __append_to_history(self, ask, response):
        self.__history["ask"].append(ask)
        self.__history["response"].append(response)
        if self.__max_history_length is not None and len(self.__history["ask"]) > self.__max_history_length:
            self.__shorten_history()

    def __shorten_history(self):
        self.__history["ask"] = self.__history["ask"][1:]
        self.__history["response"] = self.__history["response"][1:]

    def __log(self, ask, prompt, response):
        self.__logger.log(ask, "ask")
        self.__logger.log(prompt, "prompt")
        self.__logger.log(response, "response")
