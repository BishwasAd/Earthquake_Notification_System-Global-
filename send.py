from twilio.rest import Client

account_sid = 'AC******************************'
auth_token = '10*******************************'

client = Client(account_sid, auth_token)

def send_sms(message):
    try:
        message = client.messages.create(
            body=message,
            from_='+************',   
            to='+***********'      
        )
        print(f"SMS sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")
