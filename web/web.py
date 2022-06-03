import json
from flask import Flask, render_template, request
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from Logger.Logger import Logger
from ProjectParser.Parser import Parser

app = Flask(__name__)

@app.route('/project', methods=['GET', 'POST'])
def upload_project():
    if request.method == "POST":
        project = json.loads(request.files['projectFile'].read())
        data = Parser(file=project)
        data.load_project()
        return render_template('project.html', data=data.items())
    else:
        return render_template('upload_json.html')
