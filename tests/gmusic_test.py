from gmusicapi import Mobileclient

api = Mobileclient()
logged_in = api.login("joaohkfaria@gmail.com", "", "")

print(logged_in)