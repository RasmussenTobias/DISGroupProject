from email.policy import default
import os
import csv
import pandas as pd
from collections import defaultdict
'''
ligaDict = {"E0": "Premier League", "E1": "Championship", "E2": "League 1", "E3": "League 2", "EC": "Conference"}

year, datePlayed, playingTeams, ligaName = [], [], [], []

# Get the parent directory path
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

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