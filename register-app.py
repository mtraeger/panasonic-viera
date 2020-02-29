import panasonic_viera

rc = panasonic_viera.RemoteControl("192.168.1.45")
# Make the TV display a pairing pin code
rc.request_pin_code()
# Interactively ask the user for the pin code
pin = input("Enter the displayed pin code: ")
# Authorize the pin code with the TV
rc.authorize_pin_code(pincode=pin)
# Display credentials (application ID and encryption key)
print(rc._app_id)
print(rc._enc_key)
# We can now start communicating with our TV
# Send EPG key
rc.send_key(panasonic_viera.Keys.epg)
