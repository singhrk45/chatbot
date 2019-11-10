# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:57:13 2019

@author: SINGH RK
"""

from flask import Flask,render_template,request,url_for,redirect,session,jsonify
from nlp import NLP
import sqlite3 as sq




con = sq.connect('sarthak_ka_database.db')
with con:
    cur=con.cursor()
    cur.execute("Create table if not exists details(fname text not null,lname text,email text primary key not null,password text not null,weight int not null,height int not null,profession text,gender text)")


k=NLP()
app=Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login",methods =['GET','POST'])
def login():
	error =None
	if request.method == 'POST':
		username = request.form['email']
		password = request.form['password']
		con = sq.connect('sarthak_ka_database.db')
		with con:
			cur=con.cursor()
			try:
				print('checking')
				cur.execute("""SELECT fname,password  from details where email = ? """,(username,))
				d=cur.fetchone()
				print(d)
				fn = d[0]
				pas = d[1]
				if password == pas :
					
					#print(username)
					return redirect(url_for('chatbot',username=fn.lower()))
				else:
					error = "Invaild Email or Password"

			except :
				print('Unsuccessful')
		#print(username,password)
	return render_template('login2.html',error=error)


@app.route("/signup", methods =['GET','POST'])
def signup():
	if request.method == 'POST':
		fname = request.form['first_name']
		lname = request.form['last_name']
		bday = request.form['bday']
		email = request.form['email']
		ps= request.form['password']
		weight = request.form['weight']
		height = request.form['height']
		prof = request.form['profession']
		gen = request.form['gender']
		con = sq.connect('sarthak_ka_database.db')
		with con:
			cur = con.cursor()
			
			cur.execute("""INSERT INTO details(fname,lname,email,password,weight,height,profession,gender)VALUES(?,?,?,?,?,?,?,?)""",(fname,lname,email,ps,weight,height,prof,gen))

		return redirect(url_for('login'))




		print(fname,lname,bday,email,ps,weight,height,prof,gen)
	return render_template('Signup.html')

@app.route("/xyz/<username>")
def chatbot(username):
	return render_template('chat.html',username = username)


@app.route('/ask', methods = ["POST"])
def ask():
	message = request.form['messageText']
	res = k.processing(message)
	print(message)
	return jsonify({'status':'OK','answer':res})


if __name__=="__main__":
	app.run(port=5000,debug=True)