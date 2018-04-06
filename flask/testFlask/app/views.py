from app import app
from flask import render_template
from werkzeug import secure_filename
from flask import request, flash, redirect, url_for, session, jsonify, send_from_directory, abort, make_response
import os
import logging

app.debug = True
handler = logging.FileHandler('myflask.log', encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logging_format = logging.Formatter(
    '%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)s: %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


fileDir = '/tmp/uploadDir/'

@app.route('/')
def index():
    # if 'username' in session:
        # app.logger.info("username")
        # app.logger.debug("username")
    app.logger.info(app.root_path)
    return make_response(render_template('index.html'), 200)

@app.route('/mercur.html')
def mercur():
    return render_template('mercur.html')

@app.route('/sun.html')
def sun():
    return render_template('sun.html')

@app.route('/venus.html')
def venus():
    return render_template('venus.html')

@app.route('/imageTest.html')
def imageTest():
    return render_template('imageTest.html')

@app.route('/jsTest.html')
def jsTest():
    return render_template('jsTest.html')

@app.route('/myScript.js')
def myScript():
    return render_template('../static/js/myScript.js')

@app.route('/uploadFile.html')
def uploadFile():
    return render_template('uploadFile.html')

@app.route('/uploadFile.html', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['myfile']
        #f.save(fileDir + secure_filename(f.filename))
        if f.filename:
            f.save(fileDir + f.filename)
        #return render_template('uploadFile.html')
        return redirect(url_for('uploadFile'))

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    if request.method == 'GET':
        if os.path.isfile(os.path.join(fileDir, filename)):
            # use make_response to escape Chinese error
            response = make_response(send_from_directory(fileDir, filename, as_attachment=True))
            response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
            return response
    abort(404)

@app.route('/filelist')
def showFileList():
    fileInfo = []
    for fileName in os.listdir(fileDir): 
        filePath = os.path.join(fileDir, fileName)
        mTime = os.path.getmtime(filePath)
        fileInfo.append(fileName+'|'+str(mTime))
    return '*'.join(fileInfo)

@app.route('/reactStudy.html')
def reactStudy():
    return render_template('reactStudy.html')

@app.route('/reactButtonStudy1.html')
def reactButtonStudy1():
    return render_template('reactButtonStudy1.html')

@app.route('/reactButtonStudy2.html')
def reactButtonStudy2():
    return render_template('reactButtonStudy2.html')

@app.route('/helloworldTemplate.html')
def helloworldTemplate():
    return render_template('helloworldTemplate.html')

# set the secret key.  keep this really secret:
# ramdom secret key producer
# import os
# os.urandom(24)
app.secret_key = '\x1fyT\x9a\xef\x82\xd46\x10y\x9c\xe6\xffW\xfec\x84.\xbe\xf8P\xb2\x82/'
#'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route('/cookieTest.html', methods=['GET', 'POST'])
def cookieTest():
    if request.method == 'POST':
        session['username'] = request.form['username'] 
        session['password'] = request.form['password'] 
        flash('You were successfully logged in')
        return redirect(url_for('index'))
    return render_template('cookieTest.html')

@app.route('/domStudy.html')
def domStudy():
    return render_template('domStudy.html')
