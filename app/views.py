from app import app
from flask import render_template, request
from PIL import Image
import pytesseract

app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # Get Uploaded Image
        file = request.files['file_upload']
        img = Image.open(file)

        # Convert Image to Grayscale
        img = img.convert('L')

        # Extract Text
        custom_config = r'-l eng --oem 3 --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)

        # Remove Special Characters
        text = ''.join(c for c in text if (
            c.isalnum() or c == ' ' or c == '\n'))

        return render_template('index.html', result=text)
