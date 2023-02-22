import sys
from pytube import YouTube
def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('--> |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

while True:
    try: 
        link = str(input("Enter the link of YouTube video you want to download or enter exit to quit the program: "))
        if link == "exit":
            print("Exiting the program...")
            break
        filesize = YouTube(link).streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().filesize
        print("Getting YouTube Video...")
        yt = YouTube(link, on_progress_callback=progress_function)
        yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()
        print("Download completed!!\n")
    except:
        print("Invalid link!")
        continue
   
    
    
