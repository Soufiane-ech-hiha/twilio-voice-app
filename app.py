from twilio.rest import Client
from dotenv import load_dotenv
import os

Load environment variables,
load_dotenv()

Twilio credentials,
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

Initialize Twilio Client,
client = Client(account_sid, auth_token)

def make_call(to_number):
    """
    Function to make a voice call using Twilio.
    Args:
        to_number (str): The recipient's phone number (with country code).
    """
    try:
        call = client.calls.create(
            to=tonumber,
            from=twilio_number,
            url="http://demo.twilio.com/docs/voice.xml"  # Twilio demo XML for voice response
        )
        print(f"Call initiated successfully! Call SID: {call.sid}")
    except Exception as e:
        print(f"Failed to make call: {e}")

if name == "main":
    print("Twilio Voice Call App")
    recipient = input("Enter the recipient's phone number (with country code): ")
    make_call(recipient)