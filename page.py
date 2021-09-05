from flask import Blueprint, render_template, request
from pytube import YouTube
import utils

page = Blueprint('page', __name__)

@page.route("/")
def home():
    data = {}
    url = request.args.get("v")

    if url:
        try:
            yt = YouTube(url)
            data['author'] = yt.author
            data['rating'] = yt.rating
            data['views'] = yt.views
            data['length'] = yt.length
            data['date'] = yt.publish_date
            data['image'] = yt.thumbnail_url
            data['title'] = yt.title
            data['embed'] = yt.embed_url
            data['mime_types'] = [
                {
                    'name': "Videos",
                    'streams': yt.streams.filter(progressive=True)
                },
                {
                    'name': "Audios",
                    'streams': yt.streams.filter(only_audio=True)
                },   
            ]
        except Exception as e:
            print(e)
            data['error'] = "Video not found"

    return render_template('home.html', yt=data, utils=utils, url=url)