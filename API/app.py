import os
import pafy
import subprocess
import unicodedata
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/down/id=<link>&req=<requisition>&type=<typearq>')
def download_youpa(link, requisition, typearq):
    video = pafy.new(link)
    filepath="e:\\"+requisition
    
    if not os.path.exists(filepath):
        os.makedirs(filepath)
        
    if(typearq== "mp4"):
        best = video.getbest(preftype="mp4")
    
    if(typearq== "mp3"):
        best = video.getbestaudio(preftype="m4a")
    
    filename = best.download(filepath)
    return link

@app.route('/convert/req=<requisition>')    
def converting_audio(requisition):
    arqpath = "e:\\"+requisition
    arqnames = [
        arqnames
        for arqnames
        in os.listdir(arqpath)
        if arqnames.endswith('.m4a')
        ]
     
    for filename in arqnames:
        novo_nome = unicodedata.normalize('NFKD', filename.replace(" ", "_")).encode('ascii', 'ignore')
        os.rename(arqpath+"\\"+filename, arqpath+"\\"+novo_nome)
        
        subprocess.call(["ffmpeg.exe",
                         "-i",
                         arqpath+"\\"+novo_nome,
                         "-acodec", "libmp3lame", "-ab", "128k",
                         arqpath+"\\"+novo_nome.replace(".m4a","")+".mp3"])
        os.remove(arqpath+"\\"+novo_nome)            
    return requisition
    
if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("80"),
        debug=True
    )