from flask import Flask, request, render_template,redirect,url_for
from connectionAuth import conn
cur = conn.cursor()
app = Flask(__name__)


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
      return "valid"
   
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
       return "welcome"
    else:
       return redirect(url_for("createUser"))

if __name__ == '__main__':
    app.debug = True
    app.run()
