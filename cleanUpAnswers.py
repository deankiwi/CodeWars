"""
This script will watch a selected file for changes and move the answers to a new file.

special comments in file
first line/comment is the website which the answers are from
second line/comment is the question name

if the last line is a comment # done then the script will move the answers to a new file and clear the old file
"""

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, fileName):
        self.fileName = fileName

    def on_modified(self, event):
        with open(self.fileName, "r") as file:
            lines = file.readlines()
            file.close()

        if lines[-1] == "# done" or lines[-1] == "# done\n":
            print("moving answers")
            moveAnswers(lines, self.fileName)


def moveAnswers(lines, fileName):
    # TODO check website and question are in correct format
    website = lines[0][1:].strip()
    question = lines[1][1:].strip()

    if question == "Name of question":
        print('Enter name of question on line 2')
        return
    answers = lines[2:-1]
    newFileName = f"{website}/{question}.py"
    print("moving to: " + newFileName)
    # create folder if it does not exist
    if not os.path.exists(website):
        os.makedirs(website)
    # write answers to new file
    with open(newFileName, "a") as file:
        for line in answers:
            file.write(line)
        file.close()
    with open(fileName, "w") as file:
        file.write("# " + website + "\n")
        file.write("# " + "Name of question" + "\n")
        file.close()


def main():
    path = "./"
    fileName = "liveCodingFile.py"
    event_handler = MyHandler(fileName)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
