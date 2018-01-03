from twilio.rest import Client
from credentials import account_sid,auth_token,my_cell,my_twilio

client = Client(account_sid,auth_token)

message_to_send = ''.join(['Your Uber Is Arriving Soon.\n Sorry Your Ride Has Been Cancelled!'])

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=message_to_send)