import panasonic_viera

# Get id and key from register-app.py
rc = panasonic_viera.RemoteControl("<ip>", app_id="<appid>", encryption_key="<key>")

rc.send_key(panasonic_viera.Keys.epg)
# print(rc.get_apps())
# print(rc.get_mute())
# print(rc.get_volume())

