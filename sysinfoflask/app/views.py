from flask import render_template
from app import app
from getsysinfo import getsysinfo
@app.route('/')
def index():
	output = getsysinfo.main()
	returnDict = {}
	returnDict['systeminfo'] = output
	returnDict['title'] = 'Home'
	return render_template("index.html", **returnDict)
