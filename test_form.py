import base64
import os
from flask import Flask, jsonify, request, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'picture')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    return redirect('/test_form')


@app.route('/test_form')
def test_form():
    return render_template('/test_form.html')


@app.route('/test', methods=['POST'])
def test():
    if 'file' in request.files:
        file = request.files['file']
        # filename = secure_filename(file.filename)
        # file_path = os.path.join('/picture/', filename)
        # file.save(file_path)
        pic = 'abcdef' + '.' + file.filename.split('.')[-1]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], pic)
        file.save(file_path)
        file.close()
        with open(file_path, 'rb') as f:
            file_content = f.read()
            base64_string = base64.b64encode(file_content).decode()

        return jsonify({'base64_string': base64_string})

    return 'No file part in the request.', 400


if __name__ == '__main__':
    app.run()
