<a name="readme-top"></a>

<div align="center">

# __Text Extraction__

### Built Using
  
[![Python][python-shield]][python-url]
[![html-css-js][html-css-js-shield]][html-css-js-url]
[![Flask][flask-shield]][flask-url]
[![Tesseract][tesseract-shield]][tesseract-url]

</div>

## __About__
<p align="justify">
Web Application to extract text from images using <a href="https://pypi.org/project/pytesseract">pytesseract</a>.

Sample Image: https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220401160946/HTML-Basic-Format-768x534.png

See the implementation details with <a href="https://github.com/Pranav-Nagpure/Text-Extraction-NB.git">IPython Notebook</a>
</p>

## __Getting Started__

This Project is Built With [![Anaconda][anaconda-shield]][anaconda-url] [![VSCode][vscode-shield]][vscode-url] [![Render][render-shield]][render-url]

### __Installation__
To use the app on local machine, open Anaconda Prompt and run the following commands:

1. Clone the Repository
```sh
git clone https://github.com/Pranav-Nagpure/Text-Extraction.git
```

2. Change Working Directory
```sh
cd Text-Extraction
```

3. If needed create a Virtual Environment and activate it
```sh
conda create -n environment_name python=3.10
conda activate environment_name
```

4. Install the requirements
```sh
conda install -c conda-forge tesseract
python -m pip install -r requirements.txt
```

5. Run the App
```sh
python app.py
```

6. Open the URL generated in a browser to use the App

7. You can use image in the sample_images folder

<p align="right">
(<a href="#readme-top">back to top</a>)
</p>

[python-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/python-shield.png "Python"
[python-url]: https://www.python.org

[html-css-js-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/html-css-js-shield.png
[html-css-js-url]: https://html.spec.whatwg.org "HTML | CSS | JavaScript"

[anaconda-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/anaconda-shield.png
[anaconda-url]: https://www.anaconda.com "Anaconda"

[vscode-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/vscode-shield.png
[vscode-url]: https://code.visualstudio.com "VSCode"

[render-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/render-shield.png
[render-url]: https://render.com "Render"

[flask-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/flask-shield.png "Flask"
[flask-url]: https://flask.palletsprojects.com

[tesseract-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/tesseract-shield.png
[tesseract-url]: https://github.com/tesseract-ocr "Tesseract"