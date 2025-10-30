import sqlite3
con = sqlite3.connect("youtune.db")

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS channels")
cur.execute("DROP TABLE IF EXISTS videos")
cur.execute("DROP TABLE IF EXISTS categories")
cur.execute("DROP TABLE IF EXISTS channelVideos")
cur.execute("DROP TABLE IF EXISTS userChannels")
cur.execute("DROP TABLE IF EXISTS channelCategories")
cur.execute("DROP TABLE IF EXISTS userConfigurations")
cur.execute("DROP TABLE IF EXISTS categoryConfigurations")
cur.execute("DROP TABLE IF EXISTS userWatchHistory")

cur.execute("CREATE TABLE users(username, email, password)")
cur.execute("CREATE TABLE channels()")
cur.execute("CREATE TABLE videos()")
cur.execute("CREATE TABLE categories()")
cur.execute("CREATE TABLE channelVideos()")
cur.execute("CREATE TABLE userChannels()")
cur.execute("CREATE TABLE channelCategories()")
cur.execute("CREATE TABLE userConfigurations()")
cur.execute("CREATE TABLE categoryConfigurations()")
cur.execute("CREATE TABLE userWatchHistory()")


"""
TABLES:
Users:
- id: int
- username: string
- email: email
- password: SHA256

Channels:
- id: int
- channel_id: string
- uploads_id: string 
- title: string
- picture: string (reference to file system or url)

Videos:
- id: int
- video_id: string
- title: string
- description: string
- duration: time
- published: datetime
- thumbnail: string (reference to file system or url)

Categories:
- id: int
- name: string
- user_id: fk to users_id

Channel_Videos:
- channel_id: fk to channels_id
- video_id: fk to videos_id

User_Channels:
- user_id: fk to users_id
- channel_id: fk to channels_id

Channel_Categories:
- channel_id: fk to channels_id
- category_id: fk to categories_id

User_Configurations:
- user_id: fk to users_id
- is_kids: bool
- timer: bool
- duration: time(minutes)
- is_tv: bool
- passcode: SHA256
- last_synced: timedate

Category_Configurations:
- category_id: fk to categories_id
- theme: path
- locked: bool
- timer: bool
- duration: time(minutes)
- is_tv: bool

User_Watch_History:
- id: int
- user_id: fk to users_id
- duration: time
- watched: bool

"""