import base64
from flask import Flask, render_template

app = Flask(__name__)


def convert_pic(image_pic):
    with open(image_pic, 'rb'):
        image_bytes = image_pic.read()
        return base64.b64encode(image_bytes).decode('utf-8')


@app.route('/')
def show_image():
    with open('picture/50beee25-6b74-4e34-9ef4-3f25c2ad12fd.JPG', 'rb') as image_file:
        image_bytes = image_file.read()

    # Mã hóa ảnh thành Base64
    base64_string = base64.b64encode(image_bytes).decode('utf-8')
    image_data = base64.b64decode(base64_string)
    with open('static/image.jpg', 'wb') as file:
        file.write(image_data)
    return render_template('test_image.html')


if __name__ == '__main__':
    app.run()