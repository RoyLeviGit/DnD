import datetime
import json
from pathlib import Path


class Logger:
    def __init__(self, file_name):
        log_folder = Path("log")
        log_folder.mkdir(exist_ok=True)  # Create the log folder if it doesn't exist
        self.__file_path = log_folder / f"{file_name}_{str(datetime.datetime.now())}.json"
        self.first_log_line = True
        self.__clear_log()

    def log(self, text, tag):
        log_dict = {'date': str(datetime.datetime.now()), 'tag': tag, 'text': text}
        with self.__file_path.open(mode='a') as file:  # Use Path.open to open the log file
            if self.first_log_line:
                file.write('\n\t')
                self.first_log_line = False
            else:
                file.write(',\n\t')
            json.dump(log_dict, file)

    def __clear_log(self):
        with self.__file_path.open(mode='w') as file:  # Use Path.open to open the log file
            file.write('[')
        self.first_log_line = True

    def __del__(self):
        with self.__file_path.open(mode='a') as file:  # Use Path.open to open the log file
            file.write('\n]')

