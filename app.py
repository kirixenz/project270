import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':
        account_sid = 'ACbe15c1aed29b918133b8570cb7e6ab1e'
        auth_token = 'a870ef8eee207865847e9c29324b899c'

        client = Client(account_sid, auth_token)

        service_sid = 'VAbce09f8c1ca4cb1e7c5c7593b51f1a87'

        verification = client.verify \
            .services(service_sid) \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)

        return render_template('otp_verify.html')
    else:
        return "Entered User ID or Password is wrong"

if __name__ == "__main__":
    app.run()
