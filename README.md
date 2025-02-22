# YouTube Video Downloader

## Overview

This project is a YouTube Video Downloader built using Python with a graphical user interface (GUI) created using the `customtkinter` library. I created this app because other methods of downloading YouTube videos are always sketchy but this is the fastest way
and most efficient. Below is how you can turn it into a .exe to use anywhere and not have to open your text editor each time.

## Disclaimer

I am not condoning the download of other people's content. This tool should be used responsibly with copyright in mind. 

## Features

- Easy-to-use graphical interface
- Downloads videos in the highest available resolution
- Progress indicator during download
- Notifications on download completion or errors

## Requirements

- Python 3.x
- `customtkinter` library
- `pytube` library

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. **Install dependencies:**
    You can install the required dependencies using `pip` and the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```sh
    python downloader.py
    ```

2. **Using the GUI:**
    - Enter the YouTube video URL in the provided text box.
    - Click on the "Download Video" button.
    - Select the destination folder where you want to save the video.
    - The application will display a progress bar and notify you upon completion or in case of an error.

## Creating an Executable

To create an executable file of the application, you can use `pyinstaller`:

1. **Install PyInstaller:**
    ```sh
    pip install pyinstaller
    ```

2. **Create the executable:**
    ```sh
    pyinstaller --onefile downloader.py
    ```
    The executable file will be generated in the `dist` folder.

