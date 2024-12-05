#Youtube Downloader

from pytube import YouTube
from pytube import Playlist
import os 
import subprocess
import re

#Laptop Username
#C:\Users\ASUS
username = "ASUS"

class Youtube_Downloader():
        
    def sanitize_filename(filename):
        # Remove characters that might cause issues in filenames
        return re.sub(r'[\/:*?"<>|]', '', filename)

    def download_video(url):
        try:
            yt = YouTube(url)

            print("----------------------------------------------------")
            print("| pls wait the video the video is still downloading |")
            print("----------------------------------------------------")
            
            video = yt.streams.filter(res="1080p").first().download()
            os.rename(video, "video_1080.mp4")
            audio = yt.streams.filter(only_audio=True).first().download()
            os.rename(audio, "audio_1080.mp4")
            
            sanitized_title = Youtube_Downloader.sanitize_filename(yt.title)
            file_location = fr"C:\\Users\\{username}\\Downloads\\vidio\\{sanitized_title}.mp4"

            command = f"ffmpeg -hide_banner -loglevel warning -i video_1080.mp4  -i audio_1080.mp4 -c copy \"{file_location}\""
            subprocess.run(command, shell=True)

            os.remove("audio_1080.mp4")
            os.remove("video_1080.mp4")

            print(f"{sanitized_title} has been downloaded.")
        
        except Exception as e:
            print("----------------------------------------------------")
            print(f"An error occurred: {str(e)}")
            print("----------------------------------------------------")


        # Rest of the code remains the same

        # Download Mp3 Files
    def Mp3(url):

        url = YouTube(url)

        video = url.streams.filter(only_audio=True).first()

        print("----------------------------------------------------")
        print("| pls wait the video the video is still downloading |")
        print("----------------------------------------------------")

        # check for destination to save file
        destination = str(fr"C:\Users\{username}\Downloads\Music")


        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print("\n" + url.title + " has been successfully downloaded.")

    #For Playlist
    def playlist(url,choices):

        url = Playlist(url)
        
        if choices == 1:

            
            print("----------------------------------------------------")
            print("| pls wait the video the video is still downloading |")
            print("----------------------------------------------------")
                    
            for video in url.videos:
                try:
                    
                    playlist_name = url.title

                    # Create the destination directory if it doesn't exist
                    destination_dir = os.path.join("C:\\Users\\{username}\\Downloads\\vidio", playlist_name)
                    os.makedirs(destination_dir, exist_ok=True)

                    # Loop through all the videos in the playlist
                    yt = YouTube(video.watch_url)
                    
                    stream = yt.streams.filter(res="1080p").first()
                    video_file = stream.download()
                    os.rename(video_file, "video_1080.mp4")

                    audio = yt.streams.filter(only_audio=True).first().download()
                    os.rename(audio, "audio_1080.mp4")

                    # Use double backslashes or forward slashes in file_location
                    file_location = f"C:/Users/{username}/Downloads/vidio/{playlist_name}/{yt.title}.mp4"

                    command = f'ffmpeg -hide_banner -loglevel warning -i video_1080.mp4 -i audio_1080.mp4 -c copy "{file_location}"'

                    subprocess.run(command, shell=True)

                    delete = ["del audio_1080.mp4", "del video_1080.mp4"]
                    for item in delete:
                        subprocess.run(item, shell=True)

                    print(f"{yt.title} has been downloaded.\n")

                    print("All Video Has Been Downloaded")


                except Exception as e:
                    print("----------------------------------------------------")
                    print(f"An error occurred: {str(e)}")
                    print("----------------------------------------------------")


        elif choices == 2:

            print("----------------------------------------------------")
            print("| pls wait the video the mp3 is still downloading |")
            print("----------------------------------------------------")
                    

            for video in url.videos:
                title = video.title
                p = video.streams.filter(only_audio=True).first()


                destination = str(r"C:\Users\{username}\Downloads\Music\." + url.title)

                out_file = p.download(output_path=destination)

                # save the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                print(title + " have been downloaded")
        
        else:
            print("PLS try again")
            exit

def main ():

    while True:

        try:
    
            print("----------------------------------------------------")
            print("|\t   YouTube Downloader program              |")
            print("----------------------------------------------------")
            print("1.Mp4\n2.Mp3\n3.Playlist")
            print("----------------------------------------------------")
            
            try:
                type = int(input("choice: "))

                os.system("cls")

            except(EOFError,ValueError,KeyboardInterrupt):
                os.system("cls")
                exit()

            url = (str(input("\nEnter the URL of the video you want to download: \n>> ")))
            print(url)

            os.system("cls")
            
            if type == 1:

                Youtube_Downloader.download_video(url)
            
            elif type == 2 :
                url = YouTube(url)
                Youtube_Downloader.Mp3(url)

            elif type == 3:

                print("----------------------------------------------------")
                print("|Which file you want to download                    |")
                print("----------------------------------------------------")
                print("1.mp4\n2.Mp3")
                print("----------------------------------------------------")
                choices = (int(input("choice:  ")))

                os.system("cls")

                Youtube_Downloader.playlist(url,choices)

            else:
                print("PLs try again")
                return 0 

            print("----------------------------------------------------")
            print("Notes:press ctrl + c to stop")
            print("----------------------------------------------------")
            user = input("press enter to continue: ")
            print(user)

            os.system("cls")

        except(EOFError,ValueError,KeyboardInterrupt):
            os.system("cls")

if __name__ == "__main__":
    main()