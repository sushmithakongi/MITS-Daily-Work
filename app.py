from flask import Flask
from flask import request
import psycopg2

app = Flask(__name__)

@app.route('/',methods = ('POST','GET'))
def index():
   conn = psycopg2.connect("postgresql://postgres:sql2002@localhost:5432/infobell")
   if request.method=='POST':
        user=request.form['userName']
        password=request.form['userPassWord']
        if user=='Prasad' and password=='1234':
            return 'Welcome %s' %user
        else:
            return 'login failed %s' %user
   else:
        user=request.args.get('userName')
        password=request.args.get('userPassWord')
   return 'it works'

if __name__ == "__main__":
   app.run(debug="TRUE")