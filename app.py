from flask import *
import pymysql
# create an application
app = Flask(__name__)
app.secret_key = "dsjk2@f$xzdss3#&Vcj*"

# connection = pymysql.connect(
    # host="localhost", user="root", password="", database="maindb")


@app.route("/")
def main():
    # create connection to the database
   
    return render_template("main.html")

@app.route("/Purple")
def templates1():
    return render_template("template1.html")

@app.route("/Black")
def templates7():
    return render_template("template7.html")
@app.route("/Olive Green")
def templates3():
    return render_template("template3.html")
@app.route("/Red")
def templates4():
    return render_template("template4.html")
@app.route("/Yellow")
def templates5():
    return render_template("template5.html")
@app.route("/Grey")
def templates6():
    return render_template("template6.html")
@app.route("/Login")
def templates0():
    return render_template("loginsignin.html")
@app.route("/Signup")
def templates8():
    return render_template("signupmain.html")


# create a route that returns about.html template
# @app.route("/templates")
# def templates():
#     return render_template("about.html")
# create a single item route
@app.route("/Signup")
def Signup1():
    # create connection to the database
    connection = pymysql.connect(
        host="localhost", user="root", password="", database="mysql")


@app.route("/Signup", methods=['POST', 'GET'])
def Signup ():
    # check if user has posted details
    if request.method == 'POST':

        # get the columns in users table
        # receive the details posted by the user username,email,phone,password,confirm_password
        firstname = request.form['firstname']
        secondname = request.form['secondname']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        # validation checks
        # check if username is two words
        if " " in firstname:
            return render_template("signupmain.html", error="firstname must be one word")
        if " " in secondname:
            return render_template("signupmain.html", error="secondname must be one word")
        elif "@" not in email:
            return render_template("signupmain.html", error="Invalid email.Email must have @")
        elif len(password) < 8:
            return render_template("signupmain.html", error="Password must have 8 or more characters")
        elif password != confirmpassword:
            return render_template("signupmain6.html", error="passwords do not match")
        else:
            sql = 'insert into users (username,email,phone,password) values(%s,%s,%s,%s,%s)'
            # create cursor to execute the sql
            cursor = connection.cursor()
            # execute the sql
            cursor.execute(sql, (firstname,secondname, email,password,confirmpassword))
            connection.commit()
            # send sms to user after registration
            
            return render_template("signupmain.html", success="Registration successful")
    else:
        return render_template("signupmain.html")
        # TODO


@app.route("/Login", methods=['POST', 'GET'])
def loginsignin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # create sql
        sql = 'select * from users where email=%s and password=%s'
        # create a cursor to execute the sql
        cursor = connection.cursor()
        # execute the sql
        cursor.execute(sql, (email, password))
        # check if the above details are saved
        if cursor.rowcount == 0:
            return render_template("loginsignin.html", error="Invalid login credentials.Try again later")
        else:
            session['key'] = email
            return redirect("/")    # redirect to home page

    else:
        return render_template("loginsignin.html")


# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect('/signin')

#     # mpesa
# import requests
# import datetime
# import base64
# from requests.auth import HTTPBasicAuth

# @app.route('/mpesa', methods=['POST', 'GET'])
# def mpesa_payment():
#     if request.method == 'POST':
#         phone = str(request.form['phone'])
#         amount = str(request.form['amount'])
#         # GENERATING THE ACCESS TOKEN
#         # create an account on safaricom daraja
#         consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
#         consumer_secret = "amFbAoUByPV2rM5A"

#         api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
#         r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

#         data = r.json()
#         access_token = "Bearer" + ' ' + data['access_token']

#         #  GETTING THE PASSWORD
#         timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
#         passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
#         business_short_code = "174379"
#         data = business_short_code + passkey + timestamp
#         encoded = base64.b64encode(data.encode())
#         password = encoded.decode('utf-8')

#         # BODY OR PAYLOAD
#         payload = {
#             "BusinessShortCode": "174379",
#             "Password": "{}".format(password),
#             "Timestamp": "{}".format(timestamp),
#             "TransactionType": "CustomerPayBillOnline",
#             "Amount": "500",  # use 1 when testing
#             "PartyA": phone,  # change to your number
#             "PartyB": "174379",
#             "PhoneNumber": phone,
#             "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
#             "AccountReference": "account",
#             "TransactionDesc": "account"
#         }

#         # POPULAING THE HTTP HEADER
#         headers = {
#             "Authorization": access_token,
#             "Content-Type": "application/json"
#         }

#         url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

#         response = requests.post(url, json=payload, headers=headers)
#         print(response.text)
#         return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
#                '<a href="/" class="btn btn-dark btn-sm">Back to Products</a>'

# # vendor
# @app.route('/vendor', methods=['POST', 'GET'])
# def vendor():
#     # check if user has posted details
#     if request.method == 'POST':

#         # get the columns in users table
#         # receive the details posted by the user username,email,phone,password,confirm_password
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         county = request.form['county']
#         password = request.form['password']
#         confirm_password = request.form['confirm_password']
#         email = request.form['email']
#         # validation checks
#         # check if username is two words
#         if " " in firstname:
#             return render_template("vendor.html", error="firstname must be one word")
#         elif " " in lastname:
#             return render_template("vendor.html", error="lastname should be one word")
#         # elif not phone.startswith("+2547"):
#         #     return render_template("signup.html", error="Phone number must start with 254")
#         elif len(password) < 8:
#             return render_template("vendor.html", error="Password must have 8 or more characters")
#         elif password != confirm_password:
#             return render_template("vendor.html", error="passwords do not match")
#         elif "@" not in email:
#             return render_template("vendor.html", error="Invalid email.Email must have @")
#         else:
#             vendor_sql = 'insert into vendor (firstname,lastname,county,password,email) values(%s,%s,%s,%s,%s)'
#             # create cursor to execute the sql
#             cursor = connection.cursor()
#             # execute the sql
#             cursor.execute(vendor_sql, (firstname, lastname, county, password, email))
#             connection.commit()
#             # send sms to user after registration
#             # import sms
#             # sms.send_sms(
#             #     phone, f"Hello {username} thank you for registering with soko yetu")

#             return render_template("vendor.html", success="Registration successful")
#     else:
#         return render_template("vendor.html")



app.run(debug=True)