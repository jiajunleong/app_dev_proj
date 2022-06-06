from flask import Flask, render_template,request, redirect, url_for, flash
from forms import CreateUserForm,LoginForm,AdminForm,CreateAdminForm,AdminLoginForm,ContactUsForm,CreateRepairForm,UpdateUserForm,UpdateAdminForm,UpdateRepairForm,RepairForm,RepairLoginForm,UserReviewForm
import shelve, User, Admin, Repair,UserReview
import smtplib
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    return render_template('homePage.html')

@app.route("/Userhomepage")
def Userhomepage():
    return render_template('Userhomepage.html')

@app.route("/AdminPage")
def adminpage():
    return render_template('AdminPage.html')

@app.route('/Product')
def Product():
    return render_template('Product.html')

@app.route('/service1')
def service1():
    return render_template('service1.html')

@app.route('/service2')
def service2():
    return render_template('service2.html')

@app.route('/service3')
def service3():
    return render_template('service3.html')

@app.route('/Product2')
def Product2():
    return render_template('Product2.html')

@app.route('/Product3')
def Product3():
    return render_template('Product3.html')

@app.route('/Product4')
def Product4():
    return render_template('Product4.html')

@app.route('/Product5')
def Product5():
    return render_template('Product5.html')

@app.route('/Accounts')
def Accounts():
    repairmen_dict = {}
    db = shelve.open('repairmen.db', 'r')
    repairmen_dict = db['Repair']
    db.close()

    repair_list = []
    for key in repairmen_dict:
        repair = repairmen_dict.get(key)
        repair_list.append(repair)
    return render_template('Accounts.html',count=len(repair_list),repair_list=repair_list)

@app.route('/shoppingCart')
def shoppingCart():
    return render_template('shoppingCart.html')

@app.route('/shoppingCart2')
def shoppingCart2():
    return render_template('shoppingCart2.html')

@app.route('/UserReview', methods=['GET', 'POST'])
def userReview():
    userReview = UserReviewForm(request.form)
    if request.method == 'POST' and userReview.validate():
        UserReview_dict = {}
        db = shelve.open('UserReview.db', 'c')
        try:
            UserReview_dict = db['Review']
        except:
            print("Error in retrieving Review from userReview.db.")

        review = UserReview.UserReview(userReview.name.data, userReview.repairmen_name.data, userReview.review.data)
        UserReview_dict[review.get_user_id()] = review
        db['Review'] = UserReview_dict
        userReview_dict = db['Review']
        review = userReview_dict[review.get_user_id()]
        print(review.get_name(), review.get_repairmen_name(), "was stored in user.db successfully with user_id ==", review.get_user_id())


        db.close()

        return redirect(url_for('Userhomepage'))
    return render_template('createReviews.html', form=UserReview)

@app.route('/retrieveUserReviews')
def retrieveUserReviews():
    UserReview_dict = {}
    db = shelve.open('UserReview.db', 'r')
    UserReview_dict = db['Review']
    db.close()

    Reviews_list = []
    for key in UserReview_dict:
        review = UserReview_dict.get(key)
        Reviews_list.append(review)

    return render_template('retrievereviews.html',count=len(Reviews_list),Reviews_list=Reviews_list)


@app.route('/Admincode',methods=['GET', 'POST'])
def Admincode():
    Admincode = AdminForm(request.form)
    if request.method == 'POST' and Admincode.validate():
        if Admincode.password.data == "12342495":
            print("Login successfully")
            return redirect(url_for('create_Admin'))
        else:
            flash("Wrong access code", "danger")
    return render_template('Admin-code.html', form=Admincode)

@app.route('/Repairmencode',methods=['GET', 'POST'])
def Repairmencode():
    Repairmencode = RepairForm(request.form)
    if request.method == 'POST' and Repairmencode.validate():
        if Repairmencode.password.data == "55438988":
            print("Login successfully")
            return redirect(url_for('createrepair'))
        else:
            flash("Wrong access code", "danger")
    return render_template('Repairmen-code.html', form=Repairmencode)

@app.route('/contactUs',methods=['GET', 'POST'])
def contactUs():
    contactUs =ContactUsForm(request.form)
    if request.method == 'POST' and contactUs.validate():
        email = "joshuagan2002@gmail.com"
        message = """
            Hello there,
            You just received a contact form.
            Name: Jane Tan
            Email: Jtan3224@gmail.com
            Message: hello,there
            regards,
            Webmaster
            """
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("hardwarenbusniess@gmail.com", "TLHSSALES02")
        server.sendmail("hardwarenbusniess@gmail.com", email, message)

    return render_template('contactUs.html', form=contactUs)
@app.route('/payment')
def payment():
    email = "joshuagan2002@gmail.com"
    message = "Here is Your Receipt"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("hardwarenbusniess@gmail.com", "TLHSSALES02")
    server.sendmail("hardwarenbusniess@gmail.com",email, message)
    return render_template('payment.html')
@app.route('/Booking')
def Booking():
    return render_template('Booking.html')

@app.route('/productCategory')
def productCategory():
    return render_template('productCategory.html')

@app.route('/serviceCategory')
def serviceCategory():
    return render_template('serviceCategory.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.email.data, create_user_form.password.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==", user.get_user_id())


        db.close()

        return redirect(url_for('Userhomepage'))
    return render_template('createUser.html', form=create_user_form)

@app.route('/createAdmin', methods=['GET', 'POST'])
def create_Admin():
    create_admin_form = CreateAdminForm(request.form)
    if request.method == 'POST' and create_admin_form.validate():
        admin_dict = {}
        db = shelve.open('admin.db', 'c')
        try:
            admin_dict = db['Admin']
        except:
            print("Error in retrieving Admin from admin.db.")

        admin = Admin.Admin(create_admin_form.first_name.data, create_admin_form.last_name.data, create_admin_form.gender.data, create_admin_form.email.data, create_admin_form.Password.data)
        admin_dict[admin.get_user_id()] = admin
        db['Admin'] = admin_dict
        Admin_dict = db['Admin']
        admin = Admin_dict[admin.get_user_id()]
        print(admin.get_first_name(), admin.get_last_name(), "was stored in admin.db successfully with admin_id ==", admin.get_user_id())


        db.close()

        return redirect(url_for('adminpage'))
    return render_template('createAdmin.html', form=create_admin_form)

@app.route('/createrepair', methods=['GET', 'POST'])
def createrepair():
    create_repair_form = CreateRepairForm(request.form)
    if request.method == 'POST' and create_repair_form.validate():
        repairmen_dict = {}
        db = shelve.open('repairmen.db', 'c')
        try:
            repairmen_dict = db['Repair']
        except:
            print("Error in retrieving Repair from repairmen.db.")

        repair = Repair.repair(create_repair_form.first_name.data, create_repair_form.last_name.data, create_repair_form.Services.data, create_repair_form.gender.data, create_repair_form.email.data, create_repair_form.Password.data)
        repairmen_dict[repair.get_user_id()] = repair
        db['Repair'] = repairmen_dict
        repairmen_dict = db['Repair']
        repair = repairmen_dict[repair.get_user_id()]
        print(repair.get_first_name(), repair.get_last_name(), "was stored in repairmen.db successfully with user_id ==", repair.get_user_id())


        db.close()

        return redirect(url_for('Accounts'))
    return render_template('createrepair.html', form=create_repair_form)


@app.route('/Login', methods=['GET', 'POST'])
def Login_form():
    Login_form = LoginForm(request.form)
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

        break
    if request.method == 'POST' and Login_form.validate():
        if Login_form.email.data == user.get_email() and Login_form.password.data == user.get_Password():
            print("Login successfully")
            return redirect(url_for('Userhomepage'))
        else:
            return redirect(url_for('retrieve_users'))

    return render_template('Login.html', form=Login_form)
@app.route('/AdminLogin', methods=['GET', 'POST'])
def Admin_Login():
    AdminLogin_form = AdminLoginForm(request.form)
    admin_dict = {}
    db = shelve.open('admin.db', 'r')
    admin_dict = db['Admin']
    db.close()

    admin_list = []
    for key in admin_dict:
        admin = admin_dict.get(key)
        admin_list.append(admin)

        break
    if request.method == 'POST' and AdminLogin_form.validate():
        if AdminLogin_form.email.data == admin.get_email() and AdminLogin_form.password.data == admin.get_Password():
            print("Login successfully")
            return redirect(url_for('adminpage'))
        else:
            flash("Wrong access code", "danger")

    return render_template('Adminlogin.html', form=AdminLogin_form)

@app.route('/repairLogin', methods=['GET', 'POST'])
def repairLogin():
    repairLogin_form = RepairLoginForm(request.form)
    repairmen_dict = {}
    db = shelve.open('repairmen.db', 'r')
    repairmen_dict = db['Repair']
    db.close()

    repair_list = []
    for key in repairmen_dict:
        Repair = repairmen_dict.get(key)
        repair_list.append(Repair)

        break
    if request.method == 'POST' and repairLogin_form.validate():
        if repairLogin_form.email.data == Repair.get_email() and repairLogin_form.password.data == Repair.get_Password():
            print("Login successfully")
            return redirect(url_for('Accounts'))
        else:
            flash("Wrong access code", "danger")

    return render_template('repairlogin.html', form=repairLogin_form)

@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html',count=len(users_list),users_list=users_list)

@app.route('/retrieveAdmin')
def retrieve_Admin():
    admin_dict = {}
    db = shelve.open('admin.db', 'r')
    admin_dict = db['Admin']
    db.close()

    admin_list = []
    for key in admin_dict:
        admin = admin_dict.get(key)
        admin_list.append(admin)

    return render_template('retrieveAdmins.html',count=len(admin_list),admin_list=admin_list)

@app.route('/retrieveRepairs')
def retrieveRepairs():
    repairmen_dict = {}
    db = shelve.open('repairmen.db', 'r')
    repairmen_dict = db['Repair']
    db.close()

    repair_list = []
    for key in repairmen_dict:
        repair = repairmen_dict.get(key)
        repair_list.append(repair)

    return render_template('retrieveRepairs.html',count=len(repair_list),repair_list=repair_list)

@app.route('/updateRepair/<int:id>/', methods=['GET', 'POST'])
def updateRepair(id):
    update_repair_form = UpdateRepairForm(request.form)
    if request.method == 'POST' and update_repair_form.validate():
        repairmen_dict = {}
        db = shelve.open('repairmen.db', 'w')
        repairmen_dict = db['Repair']

        repair = repairmen_dict.get(id)
        repair.set_first_name(update_repair_form.first_name.data)
        repair.set_last_name(update_repair_form.last_name.data)
        repair.set_Services(update_repair_form.Services.data)
        repair.set_gender(update_repair_form.gender.data)
        repair.set_email(update_repair_form.email.data)

        db['Repair'] = repairmen_dict
        db.close()

        return redirect(url_for('retrieveRepairs'))
    else:
        repairmen_dict = {}
        db = shelve.open('repairmen.db', 'r')
        repairmen_dict = db['Repair']
        db.close()
        repair = repairmen_dict.get(id)
        update_repair_form.first_name.data = repair.get_first_name()
        update_repair_form.last_name.data = repair.get_last_name()
        update_repair_form.gender.data = repair.get_gender()
        update_repair_form.Services.data = repair.get_Services()
        update_repair_form.email.data = repair.get_email()

    return render_template('updateRepair.html', form=update_repair_form)

@app.route('/updateAdmin/<int:id>/', methods=['GET', 'POST'])
def update_Admin(id):
    update_admin_form = UpdateAdminForm(request.form)
    if request.method == 'POST' and update_admin_form.validate():
        admin_dict = {}
        db = shelve.open('admin.db', 'w')
        admin_dict = db['Admin']

        admin = admin_dict.get(id)
        admin.set_first_name(update_admin_form.first_name.data)
        admin.set_last_name(update_admin_form.last_name.data)
        admin.set_gender(update_admin_form.gender.data)
        admin.set_email(update_admin_form.email.data)

        db['Admin'] = admin_dict
        db.close()
        print("Updated")

        return redirect(url_for('retrieve_Admin'))
    else:
        admin_dict = {}
        db = shelve.open('admin.db', 'r')
        admin_dict = db['Admin']
        db.close()
        admin = admin_dict.get(id)
        update_admin_form.first_name.data = admin.get_first_name()
        update_admin_form.last_name.data = admin.get_last_name()
        update_admin_form.gender.data = admin.get_gender()
        update_admin_form.email.data = admin.get_email()

    return render_template('updateAdmin.html', form=update_admin_form)

@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = UpdateUserForm(request.form)
    print(update_user_form.validate())
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_email(update_user_form.email.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        user_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.email.data = user.get_email()



        return render_template('updateUser.html', form=update_user_form)



@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))

@app.route('/deleteAdmin/<int:id>', methods=['POST'])
def deleteAdmin(id):
    admin_dict = {}
    db = shelve.open('admin.db', 'w')
    admin_dict = db['Admin']

    admin_dict.pop(id)

    db['Admin'] = admin_dict
    db.close()

    return redirect(url_for('retrieve_Admin'))

@app.route('/deleteRepair/<int:id>', methods=['POST'])
def deleteRepair(id):
    repairmen_dict = {}
    db = shelve.open('repairmen.db', 'w')
    repairmen_dict = db['Repair']

    repairmen_dict.pop(id)

    db['Repair'] = repairmen_dict
    db.close()

    return redirect(url_for('retrieveRepairs'))

if __name__ == "__main__":
    app.run()
