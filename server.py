from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

def download_video(url):
    downloads_folder = os.path.join(app.root_path, 'downloads')
    os.makedirs(downloads_folder, exist_ok=True)

    # Adjust format for TikTok (avoid format mismatch)
    is_tiktok = "tiktok.com" in url.lower()

    ydl_opts = {
        'format': 'best' if is_tiktok else 'best[ext=mp4][vcodec^=avc1][acodec^=mp4a]',
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        'quiet': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_youtube', methods=['POST'])
def download_youtube():
    url = request.form.get('url')
    if not url:
        return "Please provide a valid YouTube URL."
    try:
        file_path = download_video(url)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Error downloading YouTube video: {e}"

@app.route('/download_tiktok', methods=['POST'])
def download_tiktok():
    url = request.form.get('url')
    if not url:
        return "Please provide a valid TikTok URL."
    try:
        file_path = download_video(url)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Error downloading TikTok video: {e}"

if __name__ == '__main__':
    app.run(debug=True)
