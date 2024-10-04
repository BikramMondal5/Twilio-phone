from flask import Flask, render_template, redirect, url_for, request
from twilio.rest import Client
import os

app = Flask(__name__)

# Your Twilio credentials
auth_token = os.environ.get('twilio_auth_token')
account_sid = os.environ.get('twilio_account_sid')
client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_page', methods=['POST'])
def load_page():
    return render_template('phone-ui.html')
@app.route('/make_call', methods=['POST'])
def make_call():
    # Get the phone number from the form data
    phone_number = request.form.get('phone_number')

    # Ensure the phone number is in the correct format (E.164 format required by Twilio)
    if not phone_number.startswith('+91'):
        phone_number = '+91' + phone_number  
    
    # Twilio API to make the call
    call = client.calls.create(
        to=phone_number,  # Use the phone number from the form
        from_='',  # Your Twilio phone number
        url='http://demo.twilio.com/docs/voice.xml'  # TwiML URL for call actions
    )

    print(f"Call SID: {call.sid}")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
