from flask import Flask, request, render_template,redirect,url_for
from connectionAuth import conn
import psycopg2
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
      #render_template("alert.html",alert_message="Username already exists, be more creative!",redirect_url="/createUser")
      return render_template("alert.html",alert_message="Username already exists, be more creative!",redirect_url="/createUser")
   else:
      cur.execute("insert into users values(%s,%s)",(username,password))
      conn.commit()
      return render_template("ligaPrev.html")
   
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

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
    

#preview
    
@app.route("/ligaPreview",methods=["POST"])
def showMatches():
   liga = request.form['button']
   cur.execute("select distinct(year) from season where ligaName=%s",(liga,))
   seasonsForLiga = cur.fetchall()
   description = [f"Season 20{x}" for x in seasonsForLiga]
   description = [x.replace("('","").replace("',)","") for x in description]
   
   return render_template("seasons.html",num_buttons=len(seasonsForLiga),button_desc=description,liga=liga)

@app.route("/matches",methods=["post"])
def matches():
   
   cur.execute('''
               with tb1 as
               (select date,playingTeams,max(home) as h,max(draw) as d,max(away) as a
               from odds group by playingTeams,date limit 100)
               select date,playingTeams,(1/h+1/d+1/a)*100-100 as arb from tb1
               ''')
   res = cur.fetchall()
   
   return render_template("matches.html",rows = res,
                          totalMatches=len(res),
                          liga=liga)
                          

@app.route("/matchStats",methods=["GET"])
def showMatchStats():
   key = request.form["button"]
   curr.execute("select * from matchStats where datePlayed AND playingTeams =%s",(key.split("*")[0],key.split("*")[1]))
   stats = cur.fetchone()
   #return print(test)
   return render_template("singleMatch.html",match_stats = stats) 



if __name__ == '__main__':
    app.debug = True
    app.run()
    cur.close()
    conn.close()
