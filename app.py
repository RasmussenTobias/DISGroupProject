from flask import Flask, request, render_template,redirect,url_for
from connectionAuth import conn
import psycopg2
from jinja2 import pass_eval_context
from markupsafe import Markup, escape
from flask import request
import secrets
cur = conn.cursor()
app = Flask(__name__)


liga = None


@app.route("/createUser",methods=["GET"])
def createUser():
   return render_template('createUser.html')

@app.route("/checkUser",methods=["POST"])
def updateOrReject():
   username = request.form['username']
   password = request.form['password']
   
   cur.execute("select * from users where username=%s",(username,))
   res = cur.fetchone()
   if res:      
      return render_template("alert.html",alert_message="Username already exists, be more creative!",redirect_url="/createUser")
   else:
      cur.execute("insert into users values(%s,%s)",(username,password))
      conn.commit()
      return render_template("ligaPrev.html")
   
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')
 
@app.route("/register",methods=["GET"])
def goToRegister():
   return render_template('createUser.html')
   

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']

    if 'see-users' in request.form:  # Check if the "See available users" button was clicked
        cur.execute("SELECT username,password FROM users")
        users = cur.fetchall()
        user_list = [{'username': user[0], 'password': user[1]} for user in users]  # Fetch and format the user data

        return render_template('users.html', users=user_list)

    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    loginResult = cur.fetchone()

    if loginResult:
        return render_template('ligaPrev.html')  # Render the ligaPrev.html template
    else:
        return redirect(url_for('createUser'))  # Redirect to the createUser route


from flask import redirect, url_for

@app.route('/delete', methods=['POST'])
def delete_user():
    username = request.form['username']
    password = request.form['password']

    cur.execute("DELETE FROM users WHERE username = %s AND password = %s", (username, password))
    conn.commit()

    return redirect(url_for('login'))



# Flask endpoints
@app.route('/edit', methods=['POST'])
def edit_user():
    username = request.form['username']
    password = request.form['password']

    return render_template('editUser.html', username=username, password=password)

@app.route('/update/<string:old_username>', methods=['POST'])
def update_user(old_username):
    new_username = request.form['username']
    new_password = request.form['password']
    print(old_username,new_username,new_password)
    cur.execute("UPDATE users SET username=%s, password=%s WHERE username=%s",
                (new_username, new_password, old_username))
    conn.commit()

    return render_template('login.html')
 
 
#Custom split function    
@app.template_filter('custom_split')
@pass_eval_context
def custom_split(eval_ctx, value, index):
    parts = value.split('_')
    if index < len(parts):
        return Markup.escape(parts[index]) if eval_ctx.autoescape else parts[index]
    else:
        return ""    

#preview
    
@app.route("/ligaPreview",methods=["POST"])
def showMatches():
   liga = request.form['button']
   cur.execute("SELECT DISTINCT year FROM season WHERE ligaName = %s ORDER BY year DESC",(liga,))
   seasonsForLiga = cur.fetchall()
   description = [f"Season 20{x}" for x in seasonsForLiga]
   description = [x.replace("('","").replace("',)","") for x in description]
   
   return render_template("seasons.html",num_buttons=len(seasonsForLiga),button_desc=description,liga=liga)

@app.route("/matches", methods=["POST"])
def matches():
    league = request.form.get("liga")  # Assuming the league value is obtained from the previous page
    season = request.form.get("button")  # Retrieve the selected season from the button value
    print(f"Liga = {league}, season = {season}")
    cur.execute('''
        WITH tb1 AS (
            SELECT date, playingTeams, MAX(home) AS h, MAX(draw) AS d, MAX(away) AS a
            FROM odds GROUP BY playingTeams, date LIMIT 1000) 
        SELECT date, playingTeams, (1 / h + 1 / d + 1 / a) * 100 - 100 AS arb FROM tb1
    ''')
    res = cur.fetchall()
    global rows
    rows = res  # Store rows in the global variable

    return render_template("matches.html", rows=res, totalMatches=len(res), liga=liga)

                          


@app.route("/matchStats", methods=["GET"])
def showMatchStats():
    played_date = request.args.get('playedDate')
    playing_teams = request.args.get('playingTeams')
    cur.execute("SELECT * FROM matchStats WHERE datePlayed = %s AND playingTeams = %s", (played_date, playing_teams))
    match_stats = cur.fetchone()    
    return render_template("singleMatch.html", match_stats=match_stats)


   

if __name__ == '__main__':
    app.debug = True
    app.run()
    cur.close()
    conn.close()
