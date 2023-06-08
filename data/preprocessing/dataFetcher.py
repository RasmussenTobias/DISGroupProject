from email.policy import default
import os
import csv
import pandas as pd
from collections import defaultdict
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
'''
ligaDict = {"E0": "Premier League", "E1": "Championship", "E2": "League 1", "E3": "League 2", "EC": "Conference"}

year, datePlayed, playingTeams, ligaName = [], [], [], []

# Get the parent directory path

for root, dirs, files in os.walk(parent_directory):
    for file in files:
        file_path= os.path.join(root, file)
        #print(file_path)
        if file_path.split(".")[1] == "csv" and file_path.split("/")[-1][0] == "E":
            #print("going in")
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
                #print(("-".join(list(middle))))
                if len("-".join(list(middle))) < 10:
                    #print("first")
                    datePlayed.append("20"+"-".join(list(middle)))
                else:
                    #print("second")
                    datePlayed.append("-".join(list(middle)))
                playingTeams.append(str(df["HomeTeam"][count])+"_"+str(df["AwayTeam"][count]))
                ligaName.append(ligaDict[str(df["Div"][count])])
                
                

pd.DataFrame(zip(year,datePlayed,playingTeams,ligaName),columns=["year","datePlayed","playingTeams","ligaName"]).to_csv("seasonsGames.csv")
'''

'''
bookmaker,datePlayed,playingTeams = [],[],[]

B365= []
BS= []
BW= []
GB= []
IW= []
LB= []
PS = []
SO= []
SB= []
SJ= []
SY= []
VC= []
WH= []


bookmakers = ["B365",
"BS",
"BW",
"GB",
"IW",
"LB",
"PS",
"SO",
"SB",
"SJ",
"SY",
"VC",
"WH"]

bookmakerLi = [B365,
BS,
BW,
GB,
IW,
LB,
PS,
SO,
SB,
SJ,
SY,
VC,
WH]




# Get the parent directory path
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


def getOdds(df,count,name):
    #print(df[name+"H"][count])
    #print(f'returning: {("H_"+str(df[name+"H"][count]),"D_"+str(df[name+"D"][count]),"A_"+str(df[name+"A"][count]))}')
    try:
        print(f'adding: {("H_"+str(df[name+"H"][count]),"D_"+str(df[name+"D"][count]),"A_"+str(df[name+"A"][count]))}')
        return ("H_"+str(df[name+"H"][count]),"D_"+str(df[name+"D"][count]),"A_"+str(df[name+"A"][count]))
    except:
        return
    
    
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        file_path= os.path.join(root, file)
        #print(file_path)
        if file_path.split(".")[1] == "csv" and file_path.split("/")[-1][0] == "E":
            #print("going in")
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
                #print(("-".join(list(middle))))
                if len("-".join(list(middle))) < 10:
                    #print("first")
                    datePlayed.append("20"+"-".join(list(middle)))
                else:
                    #print("second")
                    datePlayed.append("-".join(list(middle)))
                    
                playingTeams.append(str(df["HomeTeam"][count])+"_"+str(df["AwayTeam"][count]))
                for count,bookie in enumerate(bookmakers):
                    bookmakerLi[count].append(getOdds(df,count,bookie))
                ligaName.append(ligaDict[str(df["Div"][count])])
                bookmaker.append("placeholder")
                    
            
pd.DataFrame(zip(bookmaker,
                 datePlayed,
                 playingTeams,
                 ligaName,
                 B365,
                BS,
                BW,
                GB,
                IW,
                LB,
                PS,
                SO,
                SB,
                SJ,
                SY,
                VC,
                WH),
             columns=["bookmaker","datePlayed","playingTeams","ligaName",
                      'B365', 'BS', 'BW', 'GB', 'IW', 'LB', 'PS', 'SO', 'SB', 'SJ', 'SY', 'VC', 'WH']).to_csv("odds.csv")               
                    
                    
df = pd.read_csv("odds.csv")


import os

# Define the input directory path and the output CSV file path
input_directory = '/Users/samuelcadell/Desktop/DISGroupProject-main/data'
output_file = 'odds.csv'

# Define the columns to extract from the input file
columns_to_extract = ['Date', 'HomeTeam', 'AwayTeam']

# Define the list of bookmakers
bookmakers = ['B365', 'BS', 'BW', 'GB', 'IW', 'LB', 'PS', 'SO', 'SB', 'SJ', 'SY', 'VC', 'WH']

# Function to create field names for each bookmaker (home, draw, away)
def create_field_names(bookmaker):
    return [bookmaker + '_Bookmaker', bookmaker + 'H', bookmaker + 'D', bookmaker + 'A']

# Initialize new DataFrame to store the transformed data
output_df = pd.DataFrame(columns=columns_to_extract + ['Bookmaker', 'Home', 'Draw', 'Away'])

# Process each file in the input directory and its subdirectories
for root, dirs, files in os.walk(input_directory):
    for file in files:
        if file.endswith('.csv'):
            # Read input CSV file using pandas
            input_file = os.path.join(root, file)
            print(file)
            try:
                df = pd.read_csv(input_file)
            except UnicodeDecodeError:
                print(f"Error reading file: {input_file}. Skipping...")
                continue
            
            # Check if all required columns exist in the DataFrame
            missing_columns = set(columns_to_extract) - set(df.columns)
            if missing_columns:
                print(f"Missing columns in file: {input_file}. Skipping...")
                continue
            
            # Process each row in the input DataFrame
            for _, row in df.iterrows():
                try:
                    # Extract the required columns
                    extracted_columns = [row['Date'], str(row['HomeTeam']) + '_' + str(row['AwayTeam'])]

                    # Extract odds for each bookmaker
                    for bookmaker in bookmakers:
                        bookmaker_odds = [bookmaker, row[bookmaker + 'H'], row[bookmaker + 'D'], row[bookmaker + 'A']]
                        output_row = extracted_columns + bookmaker_odds

                        # Append the row to the output DataFrame
                        output_df.loc[len(output_df)] = output_row + [None] * (len(output_df.columns) - len(output_row))

                except KeyError:
                    # Handle missing or incorrect columns by inserting "none" values
                    extracted_columns = ["none"] * len(columns_to_extract)
                    bookmaker_odds = ["none"] * 4

                    output_row = extracted_columns + bookmaker_odds + [None] * (len(output_df.columns) - len(extracted_columns) - len(bookmaker_odds))

                    output_df.loc[len(output_df)] = output_row

# Save the output DataFrame to CSV
output_df.to_csv(output_file, index=False)

print("CSV extraction and transformation completed.")
'''
'''
df = pd.read_csv("odds.csv")

df = df.rename(columns={"HomeTeam": "playingTeams", "AwayTeam": "Bookmaker", "Bookmaker": "Home", "Home": "Draw", "Draw": "Away", "Away": "dump"})
df = df.drop(columns=["dump"])

rows_to_drop = []
for index, row in df.iterrows():
    if row['playingTeams'] == "none":
        rows_to_drop.append(index)
        
df = df.drop(rows_to_drop)

columnOrder = ["Bookmaker", "Date","playingTeams", "Home", "Draw", "Away"]
df = df[columnOrder]
df.to_csv("odds_formatted.csv", index=False)

print(df)

datePlayed, playingTeams,fthg,ftag,attendance,refferee,homeshots,awayshots,hshotsontarget,ashotsontarget,hhitwoodwork,ahitwoodwork,hcorners,acorners,hfouls,afouls,hfreekicks,afreekicks,hoffsides,aoffsides,hyellow,ayellow,hred,ared = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        file_path = os.path.join(root,file)
        print(file_path)
        if file_path.split(".")[1] == "csv" and file_path.split("\\")[-1][0] == "E":
            print("going in")
            df = pd.read_csv(file_path,delimiter=",",encoding="latin-1")            
            for count,x in enumerate(df["HomeTeam"]):
                if "Date" in df.columns and df["Date"][count]:
                    datePlayed.append(df["Date"][count])
                else: 
                    datePlayed.append("None")
                if "HomeTeam" in df.columns and  df["HomeTeam"][count]:
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
                    hshotsontarget.append(df["HST"][count])
                else: 
                    hshotsontarget.append("None")
                if "AST" in df.columns and df["AST"][count]:
                    ashotsontarget.append(df["AST"][count])
                else: 
                    ashotsontarget.append("None")
                if "HHW" in df.columns and df["HHW"][count]:
                    hhitwoodwork.append(df["HHW"][count])
                else: 
                    hhitwoodwork.append("None")
                if "AHW" in df.columns and df["AHW"][count]:
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
        

pd.DataFrame(zip(datePlayed, playingTeams,fthg,ftag,attendance,refferee,homeshots,awayshots,hshotsontarget,ashotsontarget,hhitwoodwork,ahitwoodwork,hcorners,acorners,hfouls,afouls,hfreekicks,afreekicks,hoffsides,aoffsides,hyellow,ayellow,hred,ared),columns=["datePlayed", "playingTeams","fthg","ftag","attendance","refferee","homeshots","awayshots","hshotsontarget","ashotsontarget","hhitwoodwork","ahitwoodwork","hcorners","acorners","hfouls","afouls","hfreekicks","afreekicks","hoffsides","aoffsides","hyellow","ayellow","hred","ared"]).to_csv("gameStats.csv")
'''