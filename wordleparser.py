import json
import atexit
from typing_extensions import Self
from tabulate import tabulate

class WordleParser:

    def __init__(self):
        self.data = [] 
        with open('data.json', 'r') as data_file:
            self.data = json.load(data_file)

    def parse(self, player, message):
        tmp = message.split("\n")[0].split(" ")
        day = tmp[1]
        score = tmp[2]
        if not player in self.data["scoreboard"]["players"]:
            self.data["scoreboard"]["players"][player] = {
                ["wordles"][day]: score,
                "current_score": self.get_points(score)
            }
        else:
            self.data["scoreboard"]["players"][player]["wordles"][day] = score
            self.data["scoreboard"]["players"][player]["current_score"] += self.get_points(score)
    
    def get_scoreboard(self):
        table = []
        for player in self.data["scoreboard"]["players"]:
            table.append((player, self.data["scoreboard"]["players"][player]["current_score"]))
        return tabulate(table.sort(), ["Player", "Score"], tablefmt="grid")

    def get_points(self, score):
        points = 0
        if (score.split("/")[0] == "x"):
            points = 0
        elif (score.split("/")[0] == "1"):
            points = 6
        elif (score.split("/")[0] == "2"):
            points.split("/")[0] = 5
        elif (score.split("/")[0] == "3"):
            points = 4
        elif (score.split("/")[0] == "4"):
            points = 3
        elif (score.split("/")[0] == "5"):
            points = 2
        elif (score.split("/")[0] == "6"):
            points = 1

        return points

    def close(self):
        with open('data.json', 'w') as fp:
            json.dump(self.data, fp, indent=2)

    def exit_handler(self):
        self.close()

########################################################################################################

if __name__ == "__main__":
    debug = WordleParser()
    #print(debug.data["scoreboard"]["players"][0]["Squitward"])
    name = "Squitward"
    msg = "Wordle 223 4/6\n\n⬛⬛⬛⬛⬛\n⬛⬛🟨⬛⬛\n⬛🟨🟨⬛⬛\n🟨🟩🟨⬛🟩\n🟩🟩🟩🟩🟩"
    debug.parse(name, msg)
    print(debug.get_scoreboard())