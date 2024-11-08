import moviepy
import moviepy.editor

def Conventer():
    file_pach = input("Enter File Path : ")
    if file_pach:
        print(f"You choose file : {file_pach} ")
    else:
        print("File dont choosed! ")

    video = moviepy.editor.VideoFileClip(file_pach)
    audio = video.audio
    audio.write_audiofile('new_audio.mp3')
