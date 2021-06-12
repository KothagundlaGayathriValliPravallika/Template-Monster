import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
	m=int(request.form.get("m"))
	n=int(request.form.get("n"))
	files = request.files.getlist('files[]')
	file_names = []
	for file in files:
		filename = secure_filename(file.filename)
		file_names.append(filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	width=100/n
	height=500/m
	return render_template('display.html', filenames=file_names,m=m,n=n,height=height,width=width)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True,port=5000)