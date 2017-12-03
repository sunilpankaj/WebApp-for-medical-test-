from flask import Flask, render_template, request
import mysql.connector as mariadb

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/act', methods = ['GET','POST'])
def act():
	if(request.method == 'POST'):
		try:
			name =request.form['name']
			age = request.form['age']
			conn = mariadb.connect(user='root',password='gaytri713@', database='testdb')
			cur = conn.cursor()
			sql = "INSERT INTO test(name,age)values('{}','{}')".format(name,age);
			cur.execute(sql)
			conn.commit()
			msg = "Data Has Been Stored"
			return render_template('output.html',msg=msg)
		except:
			return "Data Base Connection Error!"

@app.route('/list')
def list():
		conn = mariadb.connect(user='root',password='gaytri713@', database='testdb')
		cur = conn.cursor()
		cur.execute("select *from test")
		rows= cur.fetchall()
		return render_template("list.html",rows=rows)

if __name__ == '__main__':
	app.run(debug = True)
