from flask import render_template, flash, redirect, url_for, request, current_app, send_from_directory
from app import app
import os
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from .util import validate_image
from PIL import Image


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        basedir = os.getcwd()
        uploaded_file = request.files['file']
        image_size_y = request.form['image_size_y']
        image_size_x = request.form['image_size_x']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream): 
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            img = Image.open(f'uploads/{filename}') # Open image
            img = img.resize((int(image_size_y), int(image_size_x)), Image.ANTIALIAS) # Resize image
            img.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            directory=os.path.join(basedir, app.config['UPLOAD_PATH'])
            return send_from_directory(directory=directory, path=filename, as_attachment=True)
        return redirect(url_for('index'))
    return render_template('index.html')






