import os
import csv
import pandas as pd

ligaDict = {"E0": "Premier League", "E1": "Championship", "E2": "League 1", "E3": "League 2", "EC": "Conference"}

year, datePlayed, playingTeams, ligaName = [], [], [], []

# Get the parent directory path
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

for root, dirs, files in os.walk(parent_directory):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        if file_path.split(".")[1] == "csv" and file_path.split("/")[-1][0] == "E":
            print("going in")
            # Do something with the file_path
            df = pd.read_csv(file_path, delimiter=",", encoding="latin-1")
            for count, x in enumerate(df["HomeTeam"]):
                middle = str(df["Date"][count]).split("/")
                if len(middle) == 1:
                        continue
                if len(middle[2]) == 2:
                    year.append(middle[2])
                else:
                    year.append(middle[2][2:])
                middle.reverse()
                print(("-".join(list(middle))))
                if len("-".join(list(middle))) < 10:
                    print("first")
                    datePlayed.append("20"+"-".join(list(middle)))
                else:
                    print("second")
                    datePlayed.append("-".join(list(middle)))
                playingTeams.append(str(df["HomeTeam"][count])+"_"+str(df["AwayTeam"][count]))
                ligaName.append(ligaDict[str(df["Div"][count])])

pd.DataFrame(zip(year,datePlayed,playingTeams,ligaName),columns=["year","datePlayed","playingTeams","ligaName"]).to_csv("seasonsGames.csv")


            
