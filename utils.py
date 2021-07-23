import secrets
import os
import bs4
import urllib, re
from PIL import Image
# from . import app
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
    send_from_directory,
)
from flask import current_app

# image upload handler

def upload_img(post_img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(post_img.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/img/spares", picture_filename
    )
    post_img.save(picture_path)
    return picture_filename

# redirects
def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)
           