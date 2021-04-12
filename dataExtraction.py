import os
from flask import Flask, render_template, url_for, request
import trimesh
import flask_wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'C:/DEV/Plain_Cuboid/Plain_Cuboid/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

posts = [
	{
		'author': 'Osheen Saxena',
		'title': 'Data Extraction Application',
		'content': 'Application for Data Engineering Test',
		'date_created': 'February 25, 2021'

	}


]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

	

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		# filename = secure_filename(file.filename)
		# file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		# fileName = os.path.join(app.config['UPLOAD_FOLDER'],filename)
		# return readfile(file)
		# return 'file save succesfully'
		return findingMeshAttributes(file)

def meshshow(file):
	mesh = trimesh.load(file ,file_type = 'stl' ,force='mesh')
	return mesh.show()

def findingMeshAttributes(file):
	mesh = trimesh.load(file ,file_type = 'stl' ,force='mesh')
	print("Here are the required information")
	dimensions = mesh.bounding_box.extents
	x = dimensions[0]
	y = dimensions[1]
	z = dimensions[2]
	# print("x = {0}".format(x), "y = {0}".format(y), "z = {0}".format(z))
	# print("Mesh's Volume = {0}".format(mesh.volume),
	# "Mesh's Bounding Box Oriented Volume  = {0}".format(mesh.bounding_box_oriented.volume),
	# "Mesh's Bounding Cylinder Volume  = {0}".format(mesh.bounding_cylinder.volume),
	# "Mesh's Bounding Sphere Volume  = {0}".format(mesh.bounding_sphere.volume),
	# "Mesh's Area  = {0}".format(mesh.area))
	return 'x = {} y = {} z = {} Mesh Volume = {} Mesh Bounding Box Oriented Volume  = {} Mesh Bounding Cylinder Volume  = {} Mesh Bounding Sphere Volume  = {} Mesh Area  = {}'.format(x, y, z, mesh.volume, mesh.bounding_box_oriented.volume, mesh.bounding_cylinder.volume, mesh.bounding_sphere.volume, mesh.area)

	

	# return meshshow(file)
	# return mesh.show()

if __name__ == '__main__':
	app.run(debug=True)





