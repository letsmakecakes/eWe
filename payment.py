from flask import Flask, render_template, request, session, redirect
from email.mime import image
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
import os,random

from DBConnection1 import Db

app = Flask(__name__)
app.secret_key="payment"

@app.route('/')
def b():
    return render_template("adminmaster.html")


@app.route('/account')
def hello_world():
    session['amount'] = 1000
    session['toaccount']=2

    return render_template("accoundeatails.html")
@app.route('/addacnt',methods=['post'])
def addacnt():

    a=session['amount']
    dcno=request.form['textfield']
    Name = request.form['textfield2']
    cvv = request.form['textfield3']
    db=Db()
    qry=db.selectOne("select * from bank where debit_creditcardno='"+dcno+"' and name='"+Name+"' and cvv='"+cvv+"'")
    balance=qry['balance']
    if qry is not None:
        if a < int(balance):
            session['account_id']=qry['Acid']
            account_id=session['account_id']
            otpvalue = random.randint(0000, 9999)
            print(otpvalue)
            session['otp'] = otpvalue

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('riss.haritha@gmail.com', 'risstech')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your OTP is " + str(otpvalue))

            msg['Subject'] = 'Verification'

            msg['To'] = "harithavalsan123@gmail.com"

            msg['From'] = 'riss.haritha@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))

            qry = db.insert("insert into otp(otpvalue,upiid) values('" + str(otpvalue) + "','" + str(account_id) + "')")
            return redirect('/otp')

        else:
            return "<script>alert('Insufficient balance......');window.location='/'</script>"

    else:
        return  "<script>alert('invalid details');window.location='/'</script>"





@app.route('/upiid')
def upiid():
    return render_template("upiid.html")



@app.route('/upiidpost',methods=['post'])
def upiipost():
    vv = request.form['textfield']
    db=Db()
    qry=db.selectOne("select * from upiids,bank where upiids.account_id= bank.Acid and upiids.upiid='"+vv+"'")
    upiids=qry['upiid']
    upi=qry['upi_id']

    if upiids==vv:

        otpvalue = random.randint(0000, 9999)
        print(otpvalue)
        session['otp']=otpvalue

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('riss.haritha@gmail.com', 'risstech')

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your OTP is " + str(otpvalue))

        msg['Subject'] = 'Verification'

        msg['To'] = "harithavalsan123@gmail.com"

        msg['From'] = 'riss.haritha@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))

        qry=db.insert("insert into otp(otpvalue,upiid) values('"+str(otpvalue)+"','"+str(upi)+"')")
        return redirect('/otp')
    else:
        return  "<script>alert('invalid upiid details');window.location='/upiid'</script>"


@app.route('/otp')
def otp():
    return render_template("otp.html")
@app.route('/otppost',methods=['post'])
def otppost():
    otp1=session['otp']
    otp2=request.form['textfield']
    print(type(otp2),type(otp1))
    if otp1==int(otp2):
        fromaccount=session['account_id']
        Toaccount = session['toaccount']
        print(Toaccount)
        amount1=session['amount']
        print(fromaccount)
        db=Db()
        qry1=db.update("update bank set balance=balance-'"+str(amount1)+"' where Acid='"+str(fromaccount)+"' ")
        qry1=db.update("update bank set balance=balance+'"+str(amount1)+"' where Acid='"+str(Toaccount)+"' ")
        return "<script>alert('invalid otp details');window.location='/'</script>"
    else:
        return "<script>alert('invalid otp details');window.location='/otp'</script>"



if __name__ == '__main__':
    app.run()
