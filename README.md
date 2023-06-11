## Initialization:
1. Clone / download repository files and run the following to install the required packages
>$ pip install -r requirements.txt
2. Create a new database in pgAdmin (preferably named disprojektdata)
3. Fill out the connection details (myHost,myPort,myDbName,myUser,myPassword) in the "connectionAuth.py" file.

## Database initialization:
1. Run the "go.bat" file and enter the password for the psql user to insert the data into the database (will take approximately 1 min).

## Running the webpage:
$ python run.py

## Interact with the webpage:
When opening the application, either try to login or create a new user - either way it will redirect to create a new user if the user does not 
exist in the database. 
Open the user list to delete and update current users.
When successfully logged in you can proceed through leagues, seasons and matches where arbitrage information as well as match stats for each game is available. 
Use the ← and → arrows at the top left of your browser to go back and forth.