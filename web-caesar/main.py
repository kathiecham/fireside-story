from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 275px;
                height: 200px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 275px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form id="input_form" method="POST">
            <label> Rotate by: 
            <input type="text" name="rot" value="0" /> </label>
            <textarea name="text" placeholder="Enter text here to be encrypted"></textarea>
            <input type="submit" value="Submit Query"/>
        <form/>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form ['text']
    rot = request.form ['rot']
    rot = int(rot)
    rotated = rotate_string(text,rot)
    return rotated
    

# to be rendered in the browser.
app.run()