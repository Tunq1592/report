from flask import Flask, render_template, request, url_for, redirect
import sqlite3
from flask_bootstrap import Bootstrap

app=Flask(__name__, static_url_path= ('/static'))
Bootstrap(app)

@app.route('/')
def form_cs():
    return render_template('Form_cs.html')

    
@app.route('/', methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        datetime = request.form['Datetime']
        tttn = request.form['TTTN']
        shđ = request.form['SHĐ']
        tkh = request.form['TKH']
        cmnd = request.form['CMND']
        tttnkh = request.form['TTTNKH']
        sreenshot = request.form['Sreenshot']
        status = request.form['Status']
        cs_team = request.form['CS_Team']
        comment = request.form['Comment']
        comment_payment = request.form['Comment_Payment']
        conn_db = sqlite3.connect('reports.db')
        cursor = conn_db.cursor()
        cursor.execute(
                "INSERT INTO reports (Datetime, TTTN, SHĐ, TKH, CMND, TTTNKH, Sreenshot, Status, CS_Team, Comment, Comment_payment) VALUES (?,?,?,?,?,?,?,?,?,?,?)", 
                (datetime, tttn, shđ, tkh, cmnd, tttnkh, sreenshot, status, cs_team, comment, comment_payment)
                )
        conn_db.commit()
        return redirect('/')

@app.route('/report')
def test():
        con = sqlite3.connect("reports.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from reports")
        rows = cur.fetchall()
        return render_template('report_cs.html', rows = rows)

@app.route('/report' , methods= ['GET', 'POST'])
def form_payment():
        if request.method == 'POST':
                datetime = request.form['Datetime']
                tttn = request.form['TTTN']
                shđ = request.form['SHĐ']
                tkh = request.form['TKH']
                cmnd = request.form['CMND']
                tttnkh = request.form['TTTNKH']
                sreenshot = request.form['Sreenshot']
                status = request.form['Status']
                cs_team = request.form['CS_Team']
                comment = request.form['Comment']
                comment_payment = request.form['Comment_Payment']
                conn_db = sqlite3.connect('reports.db')
                conn_db.row_factory = sqlite3.Row
                cursor = conn_db.cursor()
                cursor.execute(" UPDATE reports SET Datetime = ?, TTTN = ?, SHĐ = ?, TKH = ?, CMND = ?, TTTNKH = ?, Sreenshot = ?, Status = ?, CS_Team = ?, Comment = ?, Comment_payment = ? WHERE CMND = ? ", ( 
                        datetime, tttn, shđ, tkh, cmnd, tttnkh, sreenshot, status, cs_team, comment, comment_payment, cmnd)
                        )
                conn_db.commit()
                cursor.execute("select * from reports")
                rows = cursor.fetchall()
                return render_template ('report_cs.html', rows = rows)

@app.route('/delete')
def form_test():
        con = sqlite3.connect("reports -Nov082019.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from reports")
        rows = cur.fetchall()
        return render_template('Formdemo.html', rows = rows)
@app.route('/delete', methods= ['GET', 'POST'])
def form_login():
        if request.method == 'POST':
                cmnd = request.form['CMND']
                cs_team = request.form['CS_Team']
                status = request.form['Status']
                start_day = request.form['startday']
                end_day = request.form['endday']
                con = sqlite3.connect('reports -Nov082019.db')
                con.row_factory = sqlite3.Row
                cursor = con.cursor()
                if len(cmnd) == 0 and len(status) > 0 and len(cs_team) > 0 and (len(start_day) == 10 and len(end_day) == 10):   
                        _execute = ("""delete from reports where datetime between '%s' and '%s' and Status = '%s' and CS_Team = '%s' """%(start_day, end_day, status, cs_team))
                        cursor.execute(_execute)
                        con.commit()
                        return redirect ('/delete')
                elif len(cmnd) > 0 and len(status) > 0 and len(cs_team) > 0  and (len(start_day) == 0 and len(end_day) == 0):
                        _execute = ("""delete from reports where CMND = '%s' and Status = '%s' and CS_Team = '%s' """ %(cmnd, status, cs_team))
                        cursor.execute(_execute)
                        con.commit()
                        return redirect ('/delete')
                elif len(cmnd) > 0 and len(status) == 0 and len(cs_team) == 0  and (len(start_day) == 0 and len(end_day) == 0):
                        _execute = ("""delete from reports where CMND = '%s' """ %(cmnd))
                        cursor.execute(_execute)
                        con.commit()
                        return redirect('/delete')
                elif len(cmnd) == 0 and len(status) == 0 and len(cs_team) == 0  and (len(start_day) == 10 and len(end_day) == 10):
                        _execute = ("""delete from reports where datetime between '%s' and '%s' """ %(start_day, end_day))
                        cursor.execute(_execute)
                        con.commit()
                        return redirect('/delete')
                else:
                        return redirect('/delete')
                
if __name__ == '__main__':
   app.run(debug = True, host ='192.168.6.64', port = 80)
    