from pytube import YouTube
link=input("enter link\n")
vid=YouTube(link)
print("Title :", vid.title )
print("\n\n\n views : ",vid.views)

print("\n\n\n here are the itags \n\n\n")
print(vid.streams)
itag=int(input('\n\n\n enter itag.......'))
stream= vid.streams.get_by_itag(itag)
stream.download('./youtube')