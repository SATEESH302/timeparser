from flask import *
from time_parser_old import main
import os
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='templates')
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
@app.route('/')
def upload():
    return render_template("upload_file.html")



@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        c = main('./uploads/'+f.filename)
        #c=main(f.filename)

        f.save(f.filename)
        return render_template("results.html", name=c)


if __name__ == '__main__':
    app.run(debug=True)