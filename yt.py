from pytube. innertube import _default_clients

_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pytube import YouTube
import threading

def on_download_complete(stream, file_path):
    messagebox.showinfo("Success", f"Downloaded '{stream.title}' successfully.")
    progress_bar.stop()
    download_button.configure(state=ctk.NORMAL)

def download_video():
    link = url_entry.get()
    folder = filedialog.askdirectory()

    if not link or not folder:
        messagebox.showwarning("Warning", "Please enter a YouTube link and select a download folder.")
        return

    download_button.configure(state=ctk.DISABLED)
    progress_bar.start()

    def download_thread():
        try:
            yt = YouTube(link, on_complete_callback=on_download_complete)
            ys = yt.streams.get_highest_resolution()
            ys.download(folder)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            download_button.configure(state=ctk.NORMAL)
            progress_bar.stop()

    threading.Thread(target=download_thread).start()

# Set up the main application window with a dark theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("YouTube Video Downloader")
root.geometry("500x300")

# URL Entry
url_label = ctk.CTkLabel(root, text="Enter YouTube Video URL:", font=("Helvetica", 14))
url_label.pack(pady=(20, 10))

url_entry = ctk.CTkEntry(root, width=400, height=40, placeholder_text="Enter the video URL here", font=("Helvetica", 12))
url_entry.pack(pady=(0, 20))

# Download Button
download_button = ctk.CTkButton(root, text="Download Video", command=download_video, width=200, height=50, fg_color="red", corner_radius=10, font=("Helvetica", 14, "bold"))
download_button.pack(pady=(0, 20))

# Progress Bar
progress_bar = ctk.CTkProgressBar(root, mode='indeterminate', width=400, height=20)
progress_bar.pack(pady=(0, 20))

# Run the application
root.mainloop()
