import sys
import time
import pafy
import sys
import youtube_dl


# 1.Grab playlist from youtube
# 2.For each song in playlist, download
# 3.Save to local directory
# 4.Spotify will automatically detect from local file folder to saved songs

def grabPlaylist():
    print("Playlist url: ")
    url = input()
    print("\nDirectory location: ")
    location = input()
    myPlaylist = pafy.get_playlist(url)
    print("Downloading...\n")
    for item in myPlaylist['items']:
        url = item['pafy'].getbest(preftype="mp4")
        url.download(location)

grabPlaylist()
