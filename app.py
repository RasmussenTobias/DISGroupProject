from flask import Flask, request, render_template,redirect,url_for
from connectionAuth import conn
import psycopg2
from jinja2 import pass_eval_context
from markupsafe import Markup, escape
from flask import session
import secrets
cur = conn.cursor()
app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

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
      #render_template("alert.html",alert_message="Username already exists, be more creative!",redirect_url="/createUser")
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
    
    cur.execute("select * from users where username=%s and password=%s",(username,password))
    loginResult = cur.fetchone()
    if loginResult:
       return render_template("ligaPrev.html")
    else:
       return redirect(url_for("createUser"))
 
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
   cur.execute("select distinct(year) from season where ligaName=%s",(liga,))
   seasonsForLiga = cur.fetchall()
   description = [f"Season 20{x}" for x in seasonsForLiga]
   description = [x.replace("('","").replace("',)","") for x in description]
   
   return render_template("seasons.html",num_buttons=len(seasonsForLiga),button_desc=description,liga=liga)

@app.route("/matches", methods=["POST"])
def matches():
    cur.execute('''
        WITH tb1 AS (
            SELECT date, playingTeams, MAX(home) AS h, MAX(draw) AS d, MAX(away) AS a
            FROM odds GROUP BY playingTeams, date LIMIT 100
        )
        SELECT date, playingTeams, (1 / h + 1 / d + 1 / a) * 100 - 100 AS arb FROM tb1
    ''')
    res = cur.fetchall()

    session['rows'] = res  # Store rows in the session

    return render_template("matches.html", rows=res, totalMatches=len(res), liga=liga)
                          

@app.route("/matchStats", methods=["POST"])
def showMatchStats():
    index = int(request.form.get("click"))
    rows = session.get('rows')  # Retrieve rows from the session
    if rows and 0 <= index < len(rows):
        row = rows[index]
        played_date = row[0]
        playing_teams = row[1]
        print(row)
        cur.execute("SELECT * FROM matchStats WHERE datePlayed = %s AND playingTeams = %s", (played_date, playing_teams))
        match_stats = cur.fetchone()
        print(match_stats)
    return render_template("singleMatch.html", match_stats=match_stats)
   

if __name__ == '__main__':
    app.debug = True
    app.run()
    cur.close()
    conn.close()
