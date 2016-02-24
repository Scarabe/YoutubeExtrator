import os
from pytube import YouTube
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/down/<link>')
def download_video(link):
    yt = YouTube("https://www.youtube.com/watch?v=" + link)
    video = yt.get('mp4', '720p')
    video.download('F:\\PROJETOS\\API-OCR\\uploads\\')
    return link
    
if __name__ == '__main__':
    app.run(
        host="192.168.2.139",
        port=int("80"),
        debug=True
    )
