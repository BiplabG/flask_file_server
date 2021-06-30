from flask import Flask, render_template, request
import os
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename
from flask import safe_join, send_from_directory

app = Flask(__name__)


@app.route("/")
def list():
    files = os.listdir("storage")
    return render_template("root.html", files=files)


@app.route("/upload", methods=["POST"])
def upload_files():
    file = request.files.get("file")
    assert file is not None, "No file sent in the upload."
    file.save(safe_join(os.getcwd(), "storage", secure_filename(file.filename)))
    return redirect("/")


@app.route("/download/<string:filename>")
def download_files(filename):
    safeFileName = safe_join(filename)
    dirname = safe_join(os.getcwd(), "storage")
    return send_from_directory(dirname, safeFileName, as_attachment=True)


app.run(debug=True, host="0.0.0.0")
