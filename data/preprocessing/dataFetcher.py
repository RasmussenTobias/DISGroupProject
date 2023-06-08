import os
import csv
import pandas as pd

ligaDict = {"E0": "Premier League", "E1": "Championship", "E2": "League 1", "E3": "League 2", "EC": "Conference"}

year, datePlayed, playingTeams, ligaName = [], [], [], []

datePlayed, playingTeams,fthg,ftag,attendance,refferee,homeshots,awayshots,hsotontharget,ashotontarget,hhitwoodwork,ahitwoodwork,hcorners,acorners,hfouls,afouls,hfreekicks,afreekicks,hoffsides,aoffsides,hyellow,ayellow,hred,ared = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

# Get the parent directory path
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

for root, dirs, files in os.walk(parent_directory):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        if file_path.split(".")[1] == "csv" and file_path.split("\\")[-1][0] == "E":
            print("going in")
            # Do something with the file_path
            df = pd.read_csv(file_path, delimiter=",", encoding="latin-1")
            for count, x in enumerate(df["HomeTeam"]):
                middle = str(df["Date"][count]).split("\\")
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


for root, dirs, files in os.walk(parent_directory):
    for file in files:
        file_path = os.path.join(root,file)
        print(file_path)
        if file_path.split(".")[1] == "csv" and file_path.split("\\")[-1][0] == "E":
            print("going in")
            df = pd.read_csv(file_path,delimiter=",",encoding="latin-1")            
            for count,x in enumerate(df["HomeTeam"]):
                if df["Date"][count]:
                    datePlayed.append(df["Date"][count])
                else: 
                    datePlayed.append("None")
                if df["HomeTeam"][count]:
                    playingTeams.append(str(df["HomeTeam"][count])+"_"+str(df["AwayTeam"][count]))
                else: 
                    playingTeams.append("None")
                if "FTHG" in df.columns and df["FTHG"][count]:
                    fthg.append(df["FTHG"][count])
                else: 
                    fthg.append("None")
                if "FTAG" in df.columns and  df["FTAG"][count]:                
                    ftag.append(df["FTAG"][count])
                else: 
                    ftag.append("None")
                
                if "Attendance" in df.columns and df["Attendance"][count]:
                    attendance.append(df["Attendance"][count])
                else: 
                    attendance.append("None")
                if "Refferee" in df.columns and df["Refferee"][count]:
                    refferee.append(df["Refferee"][count])
                else: 
                    refferee.append("None")
                if "HS" in df.columns and df["HS"][count]:
                    homeshots.append(df["HS"][count])
                else: 
                    homeshots.append("None")
                if "AS" in df.columns and df["AS"][count]:
                    awayshots.append(df["AS"][count])
                else: 
                    awayshots.append("None")
                if "HST" in df.columns and df["HST"][count]:
                    hsotontharget.append(df["HST"][count])
                else: 
                    hsotontharget.append("None")
                if "HST" in df.columns and df["AST"][count]:
                    ashotontarget.append(df["AST"][count])
                else: 
                    ashotontarget.append("None")
                if "Attendance" in df.columns and df["HHW"][count]:
                    hhitwoodwork.append(df["HHW"][count])
                else: 
                    hhitwoodwork.append("None")
                if "Attendance" in df.columns and df["AHW"][count]:
                    ahitwoodwork.append(df["AHW"][count])
                else: 
                    ahitwoodwork.append("None")
                if "HC" in df.columns and df["HC"][count]:
                    hcorners.append(df["HC"][count])
                else: 
                    hcorners.append("None")
                if "AC" in df.columns and df["AC"][count]:
                    acorners.append(df["AC"][count])
                else: 
                    acorners.append("None")
                if "HF" in df.columns and df["HF"][count]:
                    hfouls.append(df["HF"][count])
                else: 
                    hfouls.append("None")
                if "AF" in df.columns and df["AF"][count]:
                    afouls.append(df["AF"][count])
                else: 
                    afouls.append("None")
                if "HFKC" in df.columns and df["HFKC"][count]:
                    hfreekicks.append(df["HFKC"][count])
                else: 
                    hfreekicks.append("None")
                if "AFKC" in df.columns and df["AFKC"][count]:
                    afreekicks.append(df["AFKC"][count])
                else: 
                    afreekicks.append("None")
                if "HO" in df.columns and df["HO"][count]:
                    hoffsides.append(df["HO"][count])
                else: 
                    hoffsides.append("None")
                if "AO" in df.columns and df["AO"][count]:
                    aoffsides.append(df["AO"][count])
                else: 
                    aoffsides.append("None")
                if "HY" in df.columns and df["HY"][count]:
                    hyellow.append(df["HY"][count])
                else: 
                    hyellow.append("None")
                if "AY" in df.columns and df["AY"][count]:
                    ayellow.append(df["AY"][count])
                else: 
                    ayellow.append("None")
                if "HR" in df.columns and df["HR"][count]:
                    hred.append(df["HR"][count])
                else: 
                    hred.append("None")
                if "AR" in df.columns and df["AR"][count]:
                    ared.append(df["AR"][count]) 
                else: 
                    ared.append("None")   
        

pd.DataFrame(zip(datePlayed, playingTeams,fthg,ftag,attendance,refferee,homeshots,awayshots,hsotontharget,ashotontarget,hhitwoodwork,ahitwoodwork,hcorners,acorners,hfouls,afouls,hfreekicks,afreekicks,hoffsides,aoffsides,hyellow,ayellow,hred,ared),columns=["datePlayed", "playingTeams","fthg","ftag","attendance","refferee","homeshots","awayshots","hsotontharget","ashotontarget","hhitwoodwork","ahitwoodwork","hcorners","acorners","hfouls","afouls","hfreekicks","afreekicks","hoffsides","aoffsides","hyellow","ayellow","hred","ared"]).to_csv("gameStats.csv")

