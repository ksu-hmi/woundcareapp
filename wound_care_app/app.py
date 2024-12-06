from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Path for saving uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure that the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        # If no file is selected
        if file.filename == '':
            return redirect(request.url)
        # If a file is selected and it's allowed
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            # Return the result (you could replace this with your AI model logic)
            return render_template('result.html', image_file=filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
flask run
