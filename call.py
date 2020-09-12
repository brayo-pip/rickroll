from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_number = ""
target_number = ""
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://handler.twilio.com/twiml/EHe4538560b8607e2e94153a72b0661720",
    to=target_number,
    from_=twilio_number,
)

print(call.sid)
