#-*- coding:utf-8 -*-

import os
import datetime
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

now = datetime.now()

date_time = now.strftime("%Y%m%d%H%M%S")

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return '파일을 선택하지 않았습니다.'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], date_time + filename))
            return '업로드 완료'

    return '''
    <!doctype html>
    <html>
    <head>
    <title>테스트</title>
    </head>
    <body>
    <p>사용 방법: 원하는 이미지 파일을 찾아서 업로드를 클릭!</p>
    <p>서비스 시간: 내 맘대로</p>
    <p>파일 확장명: png, jpg, jpeg, gif만 지원</p>
    <p>파일 크기: 10MB 이하</p>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=업로드>
    </form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
