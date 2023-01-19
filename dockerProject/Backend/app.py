# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

@app.route('/login', methods = ['POST','GET'])
def home():
    
	if(request.method == 'POST'):
		data = "hello world"
		return data


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)

# @app.route('/home/<int:num>', methods = ['GET','POST'])
# def disp(num):

# 	return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

	app.run(debug = True)
# 	from flask import Flask
# from flask import request
# app= Flask(_name_)
# @app.route('/login',methods = ['POST','GET'])
# def login():
#     if request.method=='POST':
#         user=request.form['userName']
#         password=request.form['userPassWord']
#         if user=='Prasad' and password=='1234':
#             return 'Welcome %s' %user
#         else:
#             return 'login failed %s' %user
#     else:
#         user=request.args.get['userName']
#         password=request.args.get['userPassWord']
# if _name=="main_":
#     app.run(debug=True)



	