import tkinter as tk
from tkinter import messagebox as ms
from pytube import YouTube

# create Tkinter root
window = tk.Tk()
window.title('Youtube Video Downloader')
window.geometry('800x600')
window.config(background='#81005e')

def download_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Get the video title
        video_title = yt.title
        result_var1.set("Downloading:\n"+video_title)
        result_var2.set("Download complete!")

        # Download the video
        video_stream.download(output_path)
        
    except Exception as e:
        result_var1.set("Error: "+str(e))
        result_var2.set("Download failed.")

def download():
    try:
        # Get the URL from the entry widget
        video_url = entry.get()

        # Call the download_video function with the URL
        download_video(video_url)
    except Exception as e:
        result_var1.set("Error: "+str(e))
        result_var2.set("Download failed.")

# labels
tk.Label(window, text='Youtube Video Downloader', font=("Helvetica", 35, "bold"), fg="white", background='#81005e').place(x=400, y=300)

# Entry widget to get the YouTube video URL
entry = tk.Entry(window, width=90, fg='black', background='white', font=("Helvetica", 10, "bold"))
entry.place(x=400, y=400)

# Button to trigger the download function
tk.Button(window, width=10, text=" Download", command=download, font=("Helvetica", 15, "bold"), fg="red",
          background='#dbbc8a').place(x=650, y=450)

# Create StringVar for dynamic text updates
result_var1 = tk.StringVar()
result_var2 = tk.StringVar()

# Create a Label widget to display the result
result_label1 = tk.Message(window, textvariable=result_var1, font=("Helvetica", 10, "bold"), fg="white", background='#81005e')
result_label1.place(x=650, y=500)

result_label2 = tk.Message(window, textvariable=result_var2, font=("Helvetica", 10, "bold"), fg="white", background='#81005e')
result_label2.place(x=650, y=550)

# Start the Tkinter main loop
window.mainloop()
