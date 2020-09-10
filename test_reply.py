from twilio.rest import Client

account_sid = 'AC322fdc9777704712d006772efa8f9c38'
auth_token = '37b02f3a401e2b7d96ba7141d100c18c'
client = Client(account_sid, auth_token)

def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+919584685484'
        )

    print(message.sid)