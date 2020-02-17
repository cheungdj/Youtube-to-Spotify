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
    input()
    url = sys.argv[1]
    print("\n Directory location: ")
    location = input()
    myPlaylist = pafy.get_playlist(url)
    for item in myPlaylist['items']:
        url = item['pafy'].getbestaudio(preftype="m4a")
        url.download(location)
        time.sleep(2)

grabPlaylist()
