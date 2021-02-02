from flask import Flask, render_template, request, session, redirect
from DBConnection import Db
import datetime,random
from email.mime import image
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
app = Flask(__name__)
db=Db()
app.secret_key="tocs"


@app.route('/logout')
def logout():
    session["lo"]=" "
    return render_template('login.html')

@app.route('/admin')
def admin():
    if session["lo"]=="lin":
        type=session["ltype"]
        if type=='admin':
            return render_template("Admin/admin_home.html")
        else:
            return login()
    else:
        return login()

@app.route('/user')
def user():
    if session["lo"]=="lin":
        type=session["ltype"]
        if type=='user':
            return render_template("User/user_home.html")
        else:
            return login()
    else:
        return login()

@app.route('/ent')
def ent():
    if session["lo"]=="lin":
        type=session["ltype"]
        if type=='ent':
            return render_template("Entrepreneur/entrepreneur_home.html")
        else:
            return login()
    else:
        return login()
    #
    #
# @app.route('/panchayat')
# def panchayat():
#     type = session["ltype"]
#     if type == 'panchayat':
#         return render_template("panchayat/p_view_member_request.html")
#     else:
#         return login()
#

@app.route('/forget_pswd')
def forget_pswd():
    return render_template("forget_password.html")

@app.route('/forget_pswd1',methods=['post'])
def forget_pswd1():
    db = Db()
    mail=request.form['textfield']
    qry=db.selectOne("select * from login where username='"+mail+"'")
    res=qry['password']
    print(res)
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)

        gmail.ehlo()

        gmail.starttls()

        gmail.login('adwaithrajeev@gmail.com', 'AdwaithEzio')

    except Exception as e:
        print("Couldn't setup email!!" + str(e))

    msg = MIMEText("Your Password is " + str(res))

    msg['Subject'] = 'Verification'

    msg['To'] = mail

    msg['From'] = 'adwaithrajeev@gmail.com'

    try:

        gmail.send_message(msg)

    except Exception as e:

        print("COULDN'T SEND EMAIL", str(e))

    return 'ok'



@app.route('/')
def login():
    return render_template("login.html")

@app.route('/admin_home',methods=['post'])
def admin_home():
    db = Db()
    btn=request.form['lsubmit']
    if btn=="Login":
        username1 = request.form['textfield']
        password1 = request.form['password']
        qry = "SELECT * FROM `login` WHERE username='" + username1 + "' AND password='" + password1 + "'"
        res = db.selectOne(qry)
        type = res['type']
        lid = res['loginid']
        # email=res['username']
        # session['email']=email
        session["logid"] = lid
        session["ltype"] = type
        session["lo"] = "lin"
        if type == 'admin':
            return redirect('/admin')
        elif type == 'ent':
            return redirect('/ent')
        elif type == 'user':
            return redirect('/user')
        else:
            return "Invalid User"
    else:
        return render_template("Admin/create_account.html")


@app.route('/entrepreneur_management')
def entrepreneur_management():
    if session["lo"]=="lin":
        db = Db()
        qry="SELECT * FROM `entrepreneur`"
        res=db.select(qry)
        return render_template("Admin/view_entrepreneurs.html",data=res)
    else:
        return login()
@app.route('/vm_ent/<id>')
def vm_ent(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `entrepreneur` where entrepreneur_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/view_entrepreneur.html",data=res)
    else:
        return login()
@app.route('/view_entrepreneur1/<id>',methods=['post'])
def view_entrepreneur1(id):
    if session["lo"] == "lin":
        db = Db()
        btn10=request.form['delete']
        if btn10=="Delete":
            qry=db.delete("DELETE FROM `entrepreneur` WHERE entrepreneur_id='"+id+"'")
            return render_template("Admin/admin_home.html")
        else:
            qry = "SELECT * FROM `entrepreneur`"
            res = db.select(qry)
            return render_template("Admin/admin_home.html", data=res)
    else:
        return login()
@app.route('/product_management')
def product_management():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `product`"
        res=db.select(qry)
        return render_template("Admin/product_management.html",data=res)
    else:
        return login()
@app.route('/product_management1/<id>')
def product_management1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `product` where product_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/view_product.html",data=res)
    else:
        return login()
@app.route('/view_product1/<id>',methods=['post'])
def view_product1(id):
    if session["lo"] == "lin":
        db = Db()
        btn10=request.form['delete']
        if btn10=="Delete":
            qry=db.delete("DELETE FROM `product` WHERE product_id='"+id+"'")
            return render_template("Admin/admin_home.html")
        else:
            qry = "SELECT * FROM `product`"
            res = db.select(qry)
            return render_template("Admin/product_management.html",data=res)
    else:
        return login()
@app.route('/customer_details')
def customer_details():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `customer`"
        res=db.select(qry)
        return render_template("Admin/view_customers.html",data=res)
    else:
        return login()

@app.route('/customer_feedback')
def customer_feedback():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `customer_feedback`,customer,product where customer_feedback.customer_id=customer.customer_id and customer_feedback.product_id=product.product_id"
        res=db.select(qry)
        return render_template("Admin/customer_feedback.html",data=res)
    else:
        return login()

@app.route('/add_notification')
def notification():
    if session["lo"] == "lin":
        return render_template("Admin/add_notification.html")
    else:
        return login()

@app.route('/add_notification1', methods=['post'])
def notification1():
    if session["lo"] == "lin":
        db = Db()
        btn1=request.form['nsubmit']
        if btn1=='Submit':
            notification_title=request.form['ntextfield']
            notification_description=request.form['ntextarea']
            # notification_date=request.form['ndate']
            qry = db.insert("INSERT INTO `notification` VALUES(NULL,'" + notification_title + "','" + notification_description + "',curdate())")
            return render_template("Admin/admin_home.html")
        else:
            return render_template("Admin/admin_home.html")
    else:
        return login()


@app.route('/notification_management')
def notification_management():
    if session["lo"] == "lin":
        return render_template("Admin/notification_management.html")
    else:
        return login()


@app.route('/view_notifications')
def view_notifications():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `notification`"
        res=db.select(qry)
        return render_template("Admin/view_notifications.html",data=res)
    else:
        return login()


@app.route('/view_notifications1/<id>')
def view_notifications1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `notification` where notification_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/view_notification.html",data=res)
    else:
        return login()


@app.route('/view_notification1/<id>',methods=['post'])
def view_notification1(id):
    if session["lo"] == "lin":
        db = Db()
        btn10=request.form['delete']
        if btn10=="Delete":
            qry=db.delete("DELETE FROM `notification` WHERE notification_id='"+id+"'")
            return render_template("Admin/admin_home.html")
        else:
            qry = "SELECT * FROM `notification`"
            res = db.select(qry)
            return render_template("Admin/view_notifications.html", data=res)
    else:
        return login()


@app.route('/view_entrepreneurs')
def view_entrepreneurs():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `entrepreneur`"
        res=db.select(qry)
        return render_template("Admin/view_entrepreneurs.html",data=res)
    else:
        return login()


@app.route('/training_management')
def training_management():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training`"
        res=db.select(qry)
        return render_template("Admin/training_management.html",data=res)
    else:
        return login()


@app.route('/view_training_sessions')
def view_training_session():
    if session["lo"] == "lin":
        return render_template("Admin/view_training_session.html")
    else:
        return login()


@app.route('/add_trainig_session')
def add_training_session():
    if session["lo"] == "lin":
        return render_template("Admin/add_training_session.html")
    else:
        return login()


@app.route('/add_trainig_session1', methods=['post'])
def add_training_session1():
    if session["lo"] == "lin":
        db = Db()
        btn2=request.form['ssubmit']
        if btn2=='Submit':
            session_name=request.form['stextfield']
            session_details=request.form['stextarea']
            session_trainee=request.form['stextfield2']
            trainee_description=request.form['stextarea2']
            pic=request.files['ff']
            date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Videos\\"+date+'.mp4')
            path="/static/Videos/"+date+'.mp4'
            qry=db.insert("INSERT INTO `training` VALUES(NULL,'"+ session_name +"','"+ session_details +"','"+ session_trainee +"','"+ trainee_description +"','"+ str(path) +"' )")
            return render_template("Admin/admin_home.html")
        else:
            return render_template("Admin/add_training_session")
    else:
        return login()


@app.route('/conference_management')
def conference_management():
    if session["lo"] == "lin":
        return render_template("Admin/conference_management.html")
    else:
        return login()


@app.route('/add_conference')
def add_conference():
    if session["lo"] == "lin":
        return render_template("Admin/add_conference.html")
    else:
        return login()


@app.route('/add_conference1',methods=['post'])
def add_conference1():
    if session["lo"] == "lin":
        db = Db()
        btn=request.form['submit']
        if btn=='Submit':
            name=request.form['textfield']
            desc=request.form['textarea']
            qry=db.insert("INSERT INTO `conference` VALUES(NULL,'"+name+"','"+desc+"')")
            return render_template("Admin/admin_home.html")
        else:
            return render_template("Admin/conference_management.html")
    else:
        return login()


@app.route('/view_conference')
def view_conference():
    if session["lo"] == "lin":
        return render_template("Admin/view_conference.html")
    else:
        return login()


@app.route('/view_conference1/<id>',methods=['post'])
def view_conference1(id):
    if session["lo"] == "lin":
        db = Db()
        btn10=request.form['delete']
        if btn10=="Delete":
            qry=db.delete("DELETE FROM `conference` WHERE conferenceid='"+id+"'")
            return render_template("Admin/admin_home.html")
        else:
            qry = "SELECT * FROM `conference`"
            res = db.select(qry)
            return render_template("Admin/conferences.html", data=res)
    else:
        return login()


@app.route('/conferences')
def conferences():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `conference`"
        res=db.select(qry)
        return render_template("Admin/conferences.html",data=res)
    else:
        return login()


@app.route('/conferences1/<id>')
def conferences1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `conference` where conferenceid='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/view_conference.html",data=res)
    else:
        return login()


@app.route('/training_feedback')
def training_feedback():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training_feedback`"
        res=db.select(qry)
        return render_template("Admin/training_feedback.html",data=res)
    else:
        return login()


@app.route('/view_product')
def view_products():
    if session["lo"] == "lin":
        return render_template("Admin/view_products.html")
    else:
        return login()


@app.route('/view_entrepreneur')
def view_entrepreneur():
    if session["lo"] == "lin":
        return render_template("Admim/view_entrepreneur.html")
    else:
        return login()


@app.route('/training_sessions')
def training_sessions():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training`"
        res=db.select(qry)
        return render_template("Admin/training_sessions.html",data=res)
    else:
        return login()


@app.route('/training_sessions1/<id>')
def training_sessions1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training` WHERE session_no='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/view_training_session.html",data=res)
    else:
        return login()


@app.route('/view_training_session1/<id>',methods=['post'])
def view_training_session1(id):
    if session["lo"] == "lin":
        db = Db()
        btn10=request.form['delete']
        if btn10=="Delete":
            qry=db.delete("DELETE FROM `training` WHERE session_no='"+id+"' ")
            return render_template("Admin/admin_home.html")
        else:
            qry = "SELECT * FROM `training`"
            res = db.select(qry)
            return render_template("Admin/training_sessions.html",data=res)
    else:
        return login()


@app.route('/profile_view')
def profile_view():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/profile_view.html")
    else:
        return login()


@app.route('/training')
def training():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training`"
        res=db.select(qry)
        return render_template("Entrepreneur/training.html",data=res)
    else:
        return login()


@app.route('/training1/<id>')
def training1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training` where session_no='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Entrepreneur/view_training.html",data=res)
    else:
        return login()


@app.route('/view_training1',methods=['post'])
def view_training1():
    if session["lo"] == "lin":
        db = Db()
        btn10=request.form['back']
        if btn10=="Back":
            return render_template("Entrepreneur/entrepreneur_home.html")
    else:
        return login()


@app.route('/view_training')
def view_training():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/view_training.html")
    else:
        return login()


@app.route('/ewe_product')
def ewe_product():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/ewe_product.html")
    else:
        return login()


@app.route('/ewe_product1', methods=['post'])
def ewe_product1():
    if session["lo"] == "lin":
        db = Db()
        lid = session["logid"]
        btn4=request.form['epsubmit']
        if btn4=="Submit":
            product_name=request.form['eptextfield']
            product_prize=request.form['eptextfield2']
            product_size=request.form['epselect']
            product_description=request.form['eptextarea']
            product_stock=request.form['eptextfield3']
            pic = request.files['epfileField']
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            # pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
            path = "/static/Images/" + date + '.jpg'
            qry=db.insert("INSERT INTO `product` VALUES(NULL,'"+ product_name +"','"+ product_prize +"','"+ product_size +"','"+ product_description +"','"+ product_stock +"','"+str(lid) +"','"+ str(path) +"')")
            return render_template("Entrepreneur/entrepreneur_home.html")
        else:
            return render_template("Entrepreneur/entrepreneur_home.html")
    else:
        return login()


@app.route('/v_prd')
def v_prd():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `product`"
        res=db.select(qry)
        return render_template("Entrepreneur/view_products.html",data=res)
    else:
        return login()


@app.route('/sales')
def sales():
    if session["lo"] == "lin":
        db = Db()
        lid = session["logid"]
        qry="select * from cart,product,entrepreneur,customer where cart.order_status='booked' and cart.product_id=product.product_id and product.entrepreneur_id=entrepreneur.entrepreneur_id and cart.customer_id=customer.customer_id and product.entrepreneur_id='"+str(lid)+"'"
        res=db.select(qry)
        return render_template("Entrepreneur/view_sales.html",data=res)
    else:
        return login()


@app.route('/notifications')
def notifications():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `notification`"
        res=db.select(qry)
        return render_template("Entrepreneur/notifications.html",data=res)
    else:
        return login()


@app.route('/notifications_1/<id>')
def notifications_1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `notification` WHERE notification_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Entrepreneur/eview_notification.html",data=res)
    else:
        return login()


@app.route('/eview_notification1/<id>',methods=['post'])
def eview_notification1(id):
    if session["lo"] == "lin":
        btn10=request.form['back']
        if btn10=="Back":
            return render_template("Entrepreneur/entrepreneur_home.html")
    else:
        return login()


@app.route('/eview_notification')
def eview_notification():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/eview_notification.html")
    else:
        return login()


@app.route('/etraining_feedback')
def etraining_feedback():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/etraining_feedback.html")
    else:
        return login()


@app.route('/etraining_feedback1', methods=['post'])
def etraining_feedback1():
    if session["lo"] == "lin":
        db = Db()
        lid=session["logid"]
        btn3=request.form['etsubmit']
        if btn3=="Submit":
            session_name=request.form['ettextfield']
            trainee=request.form['ettextfield2']
            feedback=request.form['ettextarea']
            rating=request.form['etselect']
            qry=db.insert("INSERT INTO `training_feedback` VALUES(null,'"+ str(lid) +"','"+ session_name +"','"+ feedback +"','"+ rating +"',curdate(),'"+ trainee +"')")
            return render_template("Entrepreneur/entrepreneur_home.html")
        else:
            return render_template("Entrepreneur/entrepreneur_home.html")
    else:
        return login()


# @app.route('/sales')
# def sales():
#     db = Db()
#     lid=session['logid']
#     qry="select * from material,entrepreneur where material.entrepreneur_id=entrepreneur.entrepreneur_id and material.status='pending' and entrepreneur.entrepreneur_id='"+str(lid)+"'"
#     res=db.select(qry)
#     return render_template("Entrepreneur/sales.html",data=res)

@app.route('/econference')
def econference():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `conference`"
        res=db.select(qry)
        return render_template("Entrepreneur/econference.html",data=res)
    else:
        return login()


@app.route('/give_comments')
def give_comments():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/give_comments.html")
    else:
        return login()


@app.route('/give_comments1', methods=['post'])
def give_comments1():
    if session["lo"] == "lin":
        db = Db()
        lid = session["logid"]
        btn5=request.form['gcsubmit']
        if btn5=="Submit":
            # entrepreneur_name=request.form['gctextarea']
            comments=request.form['gctextarea']
            qry=db.insert("INSERT INTO `comments` VALUES(NULL,'"+str(lid)+"','"+comments+"')")
            return render_template("Entrepreneur/entrepreneur_home.html")
        else:
            return render_template("Entrepreneur/give_comments.html")
    else:
        return login()


@app.route('/get_help')
def get_help():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `help`"
        res=db.select(qry)
        return render_template("Entrepreneur/get_help.html",data=res)
    else:
        return login()

@app.route('/vh_help')
def vh_help():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `help`"
        res=db.select(qry)
        return render_template("Admin/view_help.html",data=res)
    else:
        return login()

@app.route('/delhelp/<id>')
def delhelp(id):
    if session["lo"] == "lin":
        db = Db()
        qry="delete from `help` WHERE helpid='"+id+"'"
        res=db.delete(qry)
        return redirect('/vh_help')
    else:
        return login()

@app.route('/add_help')
def add_help():
    if session["lo"] == "lin":
        return render_template("Admin/add_help.html")
    else:
        return login()

@app.route('/add_help1',methods=['post'])
def add_help1():
    if session["lo"] == "lin":
        db = Db()
        name=request.form['name']
        mail=request.form['email']
        ph=request.form['num']
        qry="insert into `help` values(null,'"+name+"','"+mail+"','"+ph+"')"
        res=db.insert(qry)
        return redirect('/admin')
    else:
        return login()


@app.route('/view_profile')
def view_profile1():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `entrepreneur` where entrepreneur_id='"+str(session["logid"])+"'"
        res=db.selectOne(qry)
        return render_template("Entrepreneur/profile_view.html",data=res)
    else:
        return login()


@app.route('/uview_profile')
def uview_profile():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `customer` where customer_id='"+str(session["logid"])+"'"
        res=db.selectOne(qry)
        return render_template("User/uview_profile.html",data=res)
    else:
        return login()


@app.route('/edit_profile',methods=['post'])
def edit_profile():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `entrepreneur` where entrepreneur_id='"+str(session["logid"])+"'"
        res=db.selectOne(qry)
        return render_template("Entrepreneur/entrepreneur_profile_update.html",data=res)
    else:
        return login()


@app.route('/edit_profile1/<id>')
def edit_profile1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `entrepreneur` where entrepreneur_id='"+str(id)+"'"
        res=db.selectOne(qry)
        return render_template("Admin/entrepreneur_profile_update.html",data=res)
    else:
        return login()


@app.route('/uedit_profile',methods=['post'])
def uedit_profile():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `customer` where customer_id='"+str(session["logid"])+"'"
        res=db.selectOne(qry)
        return render_template("User/uedit_profile.html",data=res)
    else:
        return login()


@app.route('/entrepreneur_profile_update', methods=['post'])
def entrepreneur_profile_update():
    if session["lo"] == "lin":
        db = Db()
        btn = request.form['ersubmit']
        if btn == "Save":
            name = request.form['ertextfield']
            date_of_birth = request.form['erdate']
            contact_number = request.form['ernumber']
            address = request.form['ertextarea']
            district = request.form['ertextfield4']
            pin = request.form['ernumber2']
            group = request.form['eRadioGroup1']
            pic = request.files['erfileField']
            if request.files is not None:
                if pic.filename=="":
                    qry = db.update("UPDATE `entrepreneur` SET entrepreneur_name='" + name + "', date_of_birth='" + date_of_birth + "', phone_no='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', `group`='" + group + "' WHERE entrepreneur_id='" + str(session["logid"]) + "'")
                    return render_template("Entrepreneur/entrepreneur_home.html")
                else:
                    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                    pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
                    path = "/static/Images/" + date + '.jpg'
                    qry = db.update("UPDATE `entrepreneur` SET entrepreneur_name='" + name + "', date_of_birth='" + date_of_birth + "', phone_no='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', group='" + group + "', profile_image='" + str(path) + "' WHERE entrepreneur_id='"+str(session["logid"])+"'")
                    return render_template("Entrepreneur/entrepreneur_home.html")
            else:
                date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
                path = "/static/Images/" + date + '.jpg'
                qry = db.update("UPDATE `entrepreneur` SET entrepreneur_name='" + name + "', date_of_birth='" + date_of_birth + "', phone_no='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', group='" + group + "', profile_image='" + str(path) + "' WHERE entrepreneur_id='"+str(session["logid"])+"'")
                return render_template("Entrepreneur/entrepreneur_home.html")
    else:
        return login()


@app.route('/entrepreneur_profile_update1/<id>', methods=['post'])
def entrepreneur_profile_update1(id):
    if session["lo"] == "lin":
        db = Db()
        btn = request.form['ersubmit']
        if btn == "Save":
            name = request.form['ertextfield']
            date_of_birth = request.form['erdate']
            contact_number = request.form['ernumber']
            address = request.form['ertextarea']
            district = request.form['ertextfield4']
            pin = request.form['ernumber2']
            group = request.form['eRadioGroup1']
            pic = request.files['erfileField']
            if request.files is not None:
                if pic.filename=="":
                    qry = db.update("UPDATE `entrepreneur` SET entrepreneur_name='" + name + "', date_of_birth='" + date_of_birth + "', phone_no='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', `group`='" + group + "' WHERE entrepreneur_id='" + str(id) + "'")
                    return redirect('/admin')
                else:
                    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                    pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
                    path = "/static/Images/" + date + '.jpg'
                    qry = db.update("UPDATE `entrepreneur` SET entrepreneur_name='" + name + "', date_of_birth='" + date_of_birth + "', phone_no='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', group='" + group + "', profile_image='" + str(path) + "' WHERE entrepreneur_id='"+str(id)+"'")
                    return redirect('/admin')
            else:
                date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
                path = "/static/Images/" + date + '.jpg'
                qry = db.update("UPDATE `entrepreneur` SET entrepreneur_name='" + name + "', date_of_birth='" + date_of_birth + "', phone_no='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', group='" + group + "', profile_image='" + str(path) + "' WHERE entrepreneur_id='"+str(id)+"'")
                return redirect('/admin')
    else:
        return login()


@app.route('/uedit_profile1', methods=['post'])
def uedit_profile1():
    if session["lo"] == "lin":
        db = Db()
        btn = request.form['ursubmit']
        if btn == "Save":
            name = request.form['urtextfield']
            date_of_birth = request.form['urdate']
            contact_number = request.form['urnumber']
            address = request.form['urtextarea']
            district = request.form['urtextfield4']
            pin = request.form['urnumber2']
            state=request.form['urtextfield5']
            pic = request.files['urfileField6']
            if request.files is not None:
                if pic.filename=="":
                    qry = db.insert("UPDATE `customer` SET customer_name='" + name + "', date_of_birth='" + date_of_birth + "', phoneno='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', state='" + state + "' WHERE customer_id='" + str(session["logid"]) + "'")
                    return render_template("User/user_home.html")
                else:
                    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                    pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
                    path = "/static/Images/" + date + '.jpg'
                    qry = db.insert("UPDATE `customer` SET customer_name='" + name + "', date_of_birth='" + date_of_birth + "', phoneno='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', state='" + state + "', profile_image='" + str(path) + "' WHERE customer_id='"+str(session["logid"])+"'")
                    return render_template("User/User_home.html")
            else:
                date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
                path = "/static/Images/" + date + '.jpg'
                qry = db.insert("UPDATE `customer` SET customer_name='" + name + "', date_of_birth='" + date_of_birth + "', phoneno='" + contact_number + "', place='" + address + "', pin='" + pin + "', district='" + district + "', state='" + state + "', profile_image='" + str(path) + "' WHERE customer_id='"+str(session["logid"])+"'")
                return render_template("User/user_home.html")
    else:
        return login()


@app.route('/uview_products')
def uview_products():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `product`"
        res=db.select(qry)
        return render_template("User/uview_products.html",data=res)
    else:
        return login()


@app.route('/uview_products1/<id>')
def notifications1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `product` WHERE product_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template("User/uview_product.html",data=res)
    else:
        return login()


@app.route('/add_to_cart/<i>',methods=['post'])
def add_to_cart(i):
    if session["lo"] == "lin":
        db = Db()
        q=request.form['text1']
        cid=session['logid']

        y=0;
        x=db.selectOne("select max(bill_no) as n from cart where customer_id='"+str(cid)+"' AND order_status='cart'")
        if x['n'] is not None:
            y=x['n']

        if y==0:
            z = db.selectOne("select max(bill_no) as n,count(bill_no) as cnt from cart ")
            if z["cnt"] >0:
                y = z['n']+1
            else:
                y=1

        qry=db.insert("INSERT INTO cart(`product_id`,`customer_id`,`quantity`,`order_status`,bill_no,date) VALUES('"+i+"','"+str(cid)+"','"+q+"' ,'cart','"+str(y)+"',now())")
        return uview_products()
    else:
        return login()


@app.route('/delete_cart_item/<id>')
def delete_cart_item(id):
    if session["lo"] == "lin":
        db = Db()
        qry=db.delete("DELETE FROM `cart` WHERE product_id='"+id+"' ")
        return '<script>alert("Item Deleted");window.location="/cart_items"</script>'
    else:
        return login()


@app.route('/search_product',methods=['post'])
def search_product():
    if session["lo"] == "lin":
        db = Db()
        btn=request.form['textfield']
        qry="SELECT * FROM `product` WHERE product_name like '%"+btn+"%'"
        res=db.selectOne(qry)
        return render_template("User/uview_products.html",data=res)
    else:
        return login()


@app.route('/cart_items')
def cart_items():
    if session["lo"] == "lin":
        db = Db()
        id=session['logid']
        b=str(id)
        qry="SELECT *,quantity*product_prize as p FROM `cart`,`customer`,`product` WHERE `cart`.`product_id`=`product`.`product_id` AND `customer`.`customer_id`=`cart`.`customer_id` and `cart`.`order_status`='cart'  and `cart`.`customer_id`='"+b+"' GROUP BY `cart`.`product_id` "
        res=db.select(qry)

        if res is None:
            return 'err'
        else:
            re=len(res)
            if re>0:
                billno = res[0]['bill_no']
                qr2 = db.selectOne("SELECT SUM(quantity*product_prize) as s FROM cart,product WHERE `cart`.`product_id`=`product`.`product_id`AND bill_no='" + str(billno) + "' ")
                q = qr2['s']
                return render_template("User/cart_items.html", data=res, day=b, sum=q)
            else:
                return '<script>alert("There is no products added into cart...!!!");</script>'
    else:
        return login()


@app.route('/check_out/<id>')
def check_out(id):
    if session["lo"] == "lin":
        db=Db()
        qry1=db.selectOne("SELECT * FROM `product` WHERE `product_id`='"+id+"'")
        id2=qry1['product_stock']
        qry="SELECT COUNT(`no_of_sales`) as v FROM `sales_done`,`product` WHERE `sales_done`.`product_id`=`product`.`product_id` and `sales_done`.`product_id`='"+id+"'"
        res=db.selectOne(qry)
        count1=res['v']
        a=int(id2)-int(count1)
        if a>0:
            return render_template("User/checkout.html",data=qry1,data1=a)
        else:
            return '<script>alert("Out of stock.....");window.location="/cart_items"</script>'
    else:
        return login()


@app.route('/payment/<i>',methods=['post'])
def payment(i):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `cart` WHERE `customer_id`='"+i+"' and order_status='cart'"
        res=db.select(qry)
        q=[]
        for i in res:
            q.append(i['product_id'])
        # for i in str(qry1):
        #     print(i)
        print(q)
        sum=0

        for i2 in q:
            j=db.selectOne("SELECT * FROM `product`,`cart` WHERE  `product`.`product_id`=`cart`.`product_id` AND `product`.`product_id`='"+str(i2)+"' ")
            t=j['product_prize']*j['quantity']
            sum=sum+t
            session['amount']=sum
        print(sum)
        return render_template("User/pay.html")
    else:
        return login()


@app.route('/user_registeration')
def user_registeration():
    if session["lo"] == "lin":
        return render_template("User/user_registeration.html")
    else:
        return login()


@app.route('/user_registeration1', methods=['post'])
def user_registeration1():
    if session["lo"] == "lin":
        db=Db()
        btn6=request.form['ursubmit']
        if btn6=="Submit":
            name=request.form['urtextfield']
            date_of_birth=request.form['urdate']
            emailid=request.form['urtextfield3']
            contact_number=request.form['urnumber']
            address=request.form['urtextarea']
            district=request.form['urtextfield4']
            pin=request.form['urnumber2']
            state=request.form['urtextfield5']
            password=request.form['upwd']
            pic = request.files['urfileField']
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
            path = "/static/Images/" + date + '.jpg'
            qry = db.insert("INSERT INTO `login` VALUES(NULL,'" + emailid + "','" + password + "','user')")
            qry1=db.insert("INSERT INTO `customer` VALUES('"+ str(qry) +"','"+ name +"','"+ emailid +"','"+ date_of_birth +"','"+ contact_number +"','"+ address +"','"+ state +"','"+ district +"','"+ pin +"','"+ str(path) +"')")
            return render_template("Admin/login.html")
    else:
        return login()


@app.route('/entrepreneur_registeration')
def entrepreneur_registeration():
    if session["lo"] == "lin":
        return render_template("Entrepreneur/entrepreneur_registeration.html")
    else:
        return login()


@app.route('/entrepreneur_registeration1', methods=['post'])
def entrepreneur_registeration1():
    if session["lo"] == "lin":
        db=Db()
        btn7=request.form['ersubmit']
        if btn7=="Submit":
            name=request.form['ertextfield']
            date_of_birth=request.form['erdate']
            emailid=request.form['ertextfield3']
            contact_number=request.form['ernumber']
            address=request.form['ertextarea']
            district=request.form['ertextfield4']
            pin=request.form['ernumber2']
            group=request.form['eRadioGroup1']
            password=random.randint(0000,9999)
            pic = request.files['erfileField']
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
            path = "/static/Images/" + date + '.jpg'
            qry=db.insert("INSERT INTO `login` VALUES(NULL,'"+ emailid +"','"+ password +"','ent')")
            qry1=db.insert("INSERT INTO `entrepreneur` VALUES('"+ str(qry) +"','"+ name +"','"+ emailid +"','"+ date_of_birth +"','"+ contact_number +"','"+ address +"','"+ pin +"','"+ district +"','"+ group +"','"+ str(path) +"' )")
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('adwaithrajeev@gmail.com', 'AdwaithEzio')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your Password is " + str(password))

            msg['Subject'] = 'Verification'

            msg['To'] = emailid

            msg['From'] = 'adwaithrajeev@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))

            return admin()
    else:
        return login()


@app.route('/entrepreneur_comments')
def entrepreneur_comments():
    if session["lo"] == "lin":
        db=Db()
        qry="SELECT * FROM `comments`,entrepreneur where comments.entrepreneur_id=entrepreneur.entrepreneur_id"
        res=db.select(qry)
        return render_template("Admin/entrepreneur_comments.html",data=res)
    else:
        return login()


@app.route('/b')
def b():
    if session["lo"] == "lin":
        return render_template("User/pay.html")
    else:
        return login()


@app.route('/account')
def hello_world():
    if session["lo"] == "lin":
        session['toaccount']=2
        return render_template("accoundeatails.html")
    else:
        return login()


@app.route('/addacnt',methods=['post'])
def addacnt():
    if session["lo"] == "lin":
            a=session['amount']
            dcno=request.form['textfield']
            Name = request.form['textfield2']
            cvv = request.form['textfield3']
            db=Db()
            qry=db.selectOne("select * from bank where debit_creditcardno='"+dcno+"' and name='"+Name+"' and cvv='"+cvv+"'")
            balance=qry['balance']
            id = session['logid']
            qry1=db.selectOne("SELECT * FROM `customer` WHERE `customer_id`='"+str(id)+"'")
            email=qry1['emailid']
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

                        gmail.login('adwaithrajeev@gmail.com', 'AdwaithEzio')

                    except Exception as e:
                        print("Couldn't setup email!!" + str(e))

                    msg = MIMEText("Your OTP is " + str(otpvalue))

                    msg['Subject'] = 'Verification'

                    msg['To'] =email

                    msg['From'] = 'adwaithrajeev@gmail.com'

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
    else:
        return login()


@app.route('/upiid')
def upiid():
    if session["lo"]=="lin":
        return render_template("upiid.html")
    else:
        return login()


@app.route('/upiidpost',methods=['post'])
def upiipost():
    if session["lo"] == "lin":
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

                gmail.login('', '')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your OTP is " + str(otpvalue))

            msg['Subject'] = 'Verification'
            # email=session['email']

            msg['To'] = 'adwaithrajeev@gmail.com'

            msg['From'] = 'riss.haritha@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))

            qry=db.insert("insert into otp(otpvalue,upiid) values('"+str(otpvalue)+"','"+str(upi)+"')")
            return redirect('/otp')
        else:
            return  "<script>alert('invalid upiid details');window.location='/upiid'</script>"
    else:
        return login()


@app.route('/otp')
def otp():
    if session["lo"] == "lin":
        return render_template("otp.html")
    else:
        return login()


@app.route('/otppost',methods=['post'])
def otppost():
    if session["lo"] == "lin":
        db = Db()
        otp1=session['otp']
        otp2=request.form['textfield']
        print(type(otp2),type(otp1))
        if otp1==int(otp2):
            fromaccount=session['account_id']
            Toaccount = session['toaccount']
            print(Toaccount)
            amount1=session['amount']
            print(fromaccount)
            a=session['logid']
            db=Db()
            qry1=db.update("update bank set balance=balance-'"+str(amount1)+"' where Acid='"+str(fromaccount)+"' ")
            qry2=db.update("update bank set balance=balance+'"+str(amount1)+"' where Acid='"+str(Toaccount)+"' ")
            qry3=db.update("UPDATE `cart` set order_status='booked' where `cart`.`customer_id`='"+str(a)+"'")
            return "<script>alert('Payment Successfull.');window.location='/'</script>"
        else:
            return "<script>alert('Invalid OTP details.');window.location='/otp'</script>"
    else:
        return login()


@app.route('/customer_orders')
def customer_orders():
    if session["lo"] == "lin":
        db=Db()
        a=session['logid']
        qry="SELECT product_name,product.product_id FROM `product`,`cart` WHERE cart.product_id=product.product_id AND order_status='booked' AND cart.customer_id='"+str(a)+"'"
        res=db.select(qry)
        return render_template("User/customer_orders.html",data=res)
    else:
        return login()


@app.route('/customer_order_details/<id>')
def customer_order_details(id):
    if session["lo"] == "lin":
        db=Db()
        a=session['logid']
        qry="SELECT product.*,cart.quantity FROM `product`,`cart` WHERE cart.product_id=product.product_id and  cart.product_id='"+id+"' AND order_status='booked' AND cart.customer_id='"+str(a)+"'"
        res=db.selectOne(qry)
        return render_template("User/customer_order_details.html",data=res)
    else:
        return login()


@app.route('/give_your_feedback1/<id>',methods=['post'])
def give_your_feedback1(id):
    if session["lo"] == "lin":
        db=Db()
        a=session['logid']
        rev=request.form['textarea']
        qry="insert into customer_feedback values(null,'"+str(a)+"','"+id+"','"+rev+"',curdate())"
        res=db.insert(qry)
        return '<script>alert("Feedback added successfully...!!");window.location="/user"</script>'
    else:
        return login()


@app.route('/add_materials')
def add_materials():
    if session["lo"] == "lin":
        return render_template("Admin/add_material.html")
    else:
        return login()


@app.route('/add_materials1',methods=['post'])
def add_materials1():
    if session["lo"] == "lin":
        db = Db()
        mat=request.form['mat']
        desc=request.form['desc']
        stock=request.form['stock']
        pic=request.files['file']
        date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        # pic.save(r"C:\Users\adwai\PycharmProjects\eWe\static\Images\\" + date + '.jpg')
        path = "/static/Images/" + date + '.jpg'
        qry="insert into material values(null,'"+mat+"','"+desc+"','"+str(path)+"','"+stock+"')"
        res=db.insert(qry)
        return '<script>alert("Added successfully.....!!!");window.location="/admin"</script>'
    else:
        return login()


@app.route('/view_material')
def view_material():
    if session["lo"] == "lin":
        db = Db()
        qry="select * from material"
        res=db.select(qry)
        return render_template("Admin/view_material.html",data=res)
    else:
        return login()


@app.route('/edit_stock/<id>')
def edit_stock(id):
    if session["lo"] == "lin":
        db = Db()
        qry="select * from material where materialid='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/edit_stock.html",data=res)
    else:
        return login()


@app.route('/update_stock/<id>',methods=['post'])
def update_stock(id):
    if session["lo"] == "lin":
        db = Db()
        st=request.form['stock']
        qry="update material set stock='"+st+"' where materialid='"+id+"'"
        res=db.update(qry)
        return view_material()
    else:
        return login()


@app.route('/view_material_req')
def view_material_req():
    if session["lo"] == "lin":
        db = Db()
        qry="select * from material_request,material,entrepreneur where material_request.material_id=material.materialid and material_request.status='pending' and entrepreneur.entrepreneur_id=material_request.entrepreneur_id"
        res=db.select(qry)
        return render_template("Admin/view_material_request.html",data=res)
    else:
        return login()


@app.route('/approve_material/<id>/<stk>/<qu>/<ii>')
def approve_material(id,stk,qu,ii):
    if session["lo"] == "lin":
        db = Db()
        print(stk,qu)
        qry="update material_request set status='accept' where material_req='"+id+"'"
        res=db.update(qry)
        stock=int(stk)-int(qu)
        print(stock,ii)
        qry1="update material set stock='"+str(stock)+"' where materialid='"+ii+"'"
        res1=db.update(qry1)
        return '<script>alert("Request Approved .....!!!");window.location="/view_material_req_approved"</script>'
    else:
        return login()


@app.route('/reject_material/<id>')
def reject_material(id):
    if session["lo"] == "lin":
        db = Db()
        qry="update material_request set status='reject' where material_req='"+id+"'"
        res=db.update(qry)
        return '<script>alert("Request Rejected ....!!!");window.location="/view_material_req"</script>'
    else:
        return login()


@app.route('/view_material_req_approved')
def view_material_req_approved():
    if session["lo"] == "lin":
        db = Db()
        qry="select * from material_request,material,entrepreneur where material_request.material_id=material.materialid and material_request.status='accept' and entrepreneur.entrepreneur_id=material_request.entrepreneur_id"
        res=db.select(qry)
        return render_template("Admin/view_ap_material_request.html",data=res)
    else:
        return login()


@app.route('/add_materials_req')
def add_materials_req():
    if session["lo"] == "lin":
        db = Db()
        qry="select * from material"
        res=db.select(qry)
        return render_template("Entrepreneur/view_material.html",data=res)
    else:
        return login()


@app.route('/add_materials_reqmore/<id>')
def add_materials_reqmore(id):
    if session["lo"] == "lin":
        db = Db()
        qry="select * from material where materialid='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Entrepreneur/view_material_more.html",data=res)
    else:
        return login()


@app.route('/add_materials1_req/<mid>',methods=['post'])
def add_materials1_req(mid):
    if session["lo"] == "lin":
        db = Db()
        a=session['logid']
        qua=request.form['quantity']
        stk=request.form['ll']
        if int(stk)>=int(qua):
            qry="insert into material_request values(null,'"+str(a)+"',curdate(),'"+qua+"','pending','"+mid+"')"
            res=db.insert(qry)
            return '<script>alert("Inserted ....!!!");window.location="/ent"</script>'
        else:
            return '<script>alert("Out of stock. ....!!!");window.location="/add_materials_req"</script>'
    else:
        return login()


@app.route('/trainingg')
def trainingg():
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training`"
        res=db.select(qry)
        return render_template("Entrepreneur/trainingg.html",data=res)
    else:
        return login()


@app.route('/trainingg1/<id>')
def trainingg1(id):
    if session["lo"] == "lin":
        db = Db()
        qry="SELECT * FROM `training` where session_no='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Entrepreneur/view_trainingg.html",data=res)
    else:
        return login()


@app.route('/giv_fed/<id>',methods=['post'])
def giv_fed(id):
    if session["lo"] == "lin":
        db = Db()
        a=session['logid']
        fed=request.form['textarea']
        rat=request.form['sel']
        qry="insert into training_feedback values(null,'"+str(a)+"','"+id+"','"+fed+"','"+rat+"',curdate())"
        res=db.insert(qry)
        return '<script>alert("Feedback Added successfully ....!!!");window.location="/ent"</script>'
    else:
        return login()


@app.route('/view_tr_fed')
def view_tr_fed():
    if session["lo"] == "lin":
        db = Db()
        a=session['logid']
        qry="SELECT * FROM `training`,training_feedback where training_feedback.session_no=training.session_no and training_feedback.entrepreneur_id='"+str(a)+"'"
        res=db.select(qry)
        return render_template("Entrepreneur/view_feedback.html",data=res)
    else:
        return login()


if __name__ == '__main__':
    app.run()

