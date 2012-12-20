#!/usr/bin/python

import sys
from spotify import SpotifyAPI, SpotifyUtil

def track_callback(sp, tracks):
	for track in tracks:
		print track.name
	sp.disconnect()

def album_callback(sp, album, userdata):
	print userdata
	print album.name+" - "+album.artist[0].name+"\n"
	uris = [SpotifyUtil.gid2uri("track", track.gid) for track in album.disc[0].track]	
	sp.metadata_request(uris, track_callback)

def login_callback(sp, logged_in):
	if logged_in:
		uri = sys.argv[3] if len(sys.argv) > 3 else "spotify:album:3OmHoatMS34vM7ZKb4WCY3"
		sp.metadata_request(uri, [album_callback, "foo"])
	else:
		print "There was an error logging in"

if len(sys.argv) < 3:
	print "Usage: "+sys.argv[0]+" <username> <password> [track URI]"
else:
	sp = SpotifyAPI(login_callback)
	sp.connect(sys.argv[1], sys.argv[2])
