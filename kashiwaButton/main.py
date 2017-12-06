import tkinter
import tweepy

def kashiwaPush():
    api.update_status(status)

consumer_key = "%"
consumer_secret = "%"
access_token = "%"
access_secret = "%"

status = "かしわしわしわ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

width = 100
height = 30
gui = tkinter.Tk()
gui.geometry(str(width) + "x" + str(height))
gui.title("かしわボタン : ")

kashiwaButton = tkinter.Button(gui, text="かしわボタン",command=kashiwaPush).pack()
gui.mainloop()