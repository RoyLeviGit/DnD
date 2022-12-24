import datetime
import json


class Logger:
    def __init__(self, file_name):
        self.file_path = f"log/{file_name}_{str(datetime.datetime.now())}.json"

    def log(self, tag, text):
        log_dict = {'date': str(datetime.datetime.now()), 'tag': tag, 'text': text}
        with open(self.file_path, 'a') as file:
            json.dump(log_dict, file)
            file.write('\n')

    def clear_log(self):
        with open(self.file_path, 'w') as file:
            file.write('')