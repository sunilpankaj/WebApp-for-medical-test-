from flask import Flask, render_template, request
import mysql.connector as mariadb

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('hospital.html')

@app.route('/act', methods = ['GET','POST'])
def act():
	
	if(request.method == 'POST'):
		try:
			personid = request.form['Personidentity']
			hemo = request.form['hemoglobin']
			tc = request.form['TC']
			p = request.form['DCP']
		    l = request.form['DCL']
		    e = request.form['DCE']
		    m = request.form['DCM']
		    b = request.form['DCB']
		    ERS = request.form[' ERS ']
		    Sugar= request.form[' Sugar  ']
		    Urea =request.form['Urea']
		    Creatinin =request.form[' Creatinin  ']
		    Cholestrol =request.form['Cholestrol  ']
		    HDL= request.form[' HDL  ']
		    LDL =request.form[' LDL  ']
		    LDH =request.form[' LDH  ']
		    TG =request.form[' TG   ']
		    SGOT= request.form[' SGOT  ']
		    SGPT =request.form['SGPT   ']
		    ALP =request.form['ALP   ']
		    BilirubuimTotal =request.form['BilirubuimTotal']
		    BilirubuimDirect =request.form['BilirubuimDirect']
		    Amylase =request.form['Amylase']
		    RA =request.form['RA ']
		    CRP =request.form[' CRP ']
		    ASO =request.form['ASO ']
		    ALBUMIN= request.form['ALBUMIN ']
		    TotalProtin =request.form[' TotalProtin']
		    UricAcid =request.form[' UricAcid ']
		    Calcium= request.form[' Calcium ']
		    AcidPhasphate= request.form['AcidPhasphate  ']
		    MicroAlbumin= request.form[' MicroAlbumin ']
		    BT =request.form[' BT ']
		    CT= request.form['CT']
		    Platelatecount= request.form['Platelatecount']
		    
			conn = mariadb.connect(user='root',password='gaytri713@', database='final')
			cur = conn.cursor()
			sql = "INSERT INTO test(Personidentity,hemoglobin,TC,DCP,DCL,DCE,DCM,DCB,ERS,Sugar,Urea,Creatinin,Cholestrol,HDL,LDL,LDH,TG,SGOT,SGPT,ALP,BilirubuimTotal,BilirubuimDirect,Amylase,RA,CRP,ASO,ALBUMIN,TotalProtin,UricAcid,Calcium,AcidPhasphate,MicroAlbumin,BT,CT,Platelatecount)values('{}','{}''{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',,'{}','{}','{}','{}','{}','{}',)".format(Personidentity,hemoglobin,TC,DCP,DCL,DCE,DCM,DCB,ERS,Sugar,Urea,Creatinin,Cholestrol,HDL,LDL,LDH,TG,SGOT,SGPT,ALP,BilirubuimTotal,BilirubuimDirect,Amylase,RA,CRP,ASO,ALBUMIN,TotalProtin,UricAcid,Calcium,AcidPhasphate,MicroAlbumin,BT,CT,Platelatecount );
			cur.execute(sql)
			conn.commit()
			msg = "Data Has Been Stored"
			return render_template('output.html',msg=msg)
		except:
			return "Data Base Connection Error!"
			
@app.route('/list')
def list():
		conn = mariadb.connect(user='root',password='gaytri713@', database='final')
		cur = conn.cursor()
		cur.execute("select *from exam")
		rows= cur.fetchall()
		return render_template("list.html",rows=rows)
	
if __name__ == '__main__':
	app.run(port = 5002,debug = True)

