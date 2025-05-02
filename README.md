# Cyberpunk Video Downloader (YouTube and TikTok)

This is a web-based application that allows users to download videos from YouTube and TikTok. It features a cyberpunk-themed user interface with a matrix-style falling code effect.

## Features

- Download YouTube videos in high-quality MP4 format
- Download TikTok videos without requiring ffmpeg
- Simple and intuitive web interface
- Cyberpunk-styled frontend with animated canvas background
- Built using Python Flask and yt_dlp

## Clone the Repository

```bash
git clone https://github.com/ankeman/downloadvideo.git
cd downloadvideo
```

## Setup Instructions

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 2. Install dependencies

```bash
pip install Flask yt-dlp
```

## Run the Application

```bash
python server.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

## Project Structure

```
downloadvideo/
├── server.py               # Flask backend
├── templates/
│   └── index.html          # Frontend HTML with form and animation
├── static/
│   └── mystyle.css         # Cyberpunk-styled CSS
├── downloads/              # Folder for downloaded videos (auto-created)
└── README.md               # Project documentation
```

## Notes

- No ffmpeg is needed; progressive MP4 formats are used.
- yt_dlp is more reliable than pytube and supports both platforms out of the box.

## Author

Developed by ankeman (Manish Dawadi)
