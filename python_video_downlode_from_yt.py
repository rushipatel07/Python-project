from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=ixRLjjTRczE"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
video_filename = stream.default_filename
stream.download()

current_directory = os.getcwd()
video_path = os.path.join(current_directory, video_filename)
print("Video downloaded successfully at:", video_path)
