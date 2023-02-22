from pytube import YouTube

link  = input("enter here: ")
youtube_1 = YouTube(link)

print("'''''''''''TITLE''''''''''")
print(youtube_1.title)

# print("'''''''''thumbnail'''''''''")
# print(youtube_1.thumbnail_url)

print("''''''''DOWNLOADING'''''''")
youtube_1 = youtube_1.streams.get_highest_resolution()
youtube_1.download()
print("########################################################")