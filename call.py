from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_number = ""
target_number = ""
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://handler.twilio.com/twiml/EH91da20e497f50d15db994268e0c68cff",
    to=target_number,
    from_=twilio_number,
)

print(call.sid)
