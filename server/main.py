from flask import Flask, render_template, request, Response

import zipfile as z
from io import BytesIO
import warnings


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    args = list(request.args)[1:]

    in_memory_file = BytesIO()
    zips = [f"patches/{patch}.zip" for patch in args] + ["new_default_textures.zip"]

    with z.ZipFile(in_memory_file, "w") as z1:
        for fname in zips:
            with z.ZipFile(fname, "r") as zf:
                for name in zf.namelist():
                    if name not in z1.namelist():
                        z1.writestr(name, zf.open(name).read())

    return Response(
        in_memory_file.getvalue(),
        mimetype="application/zip",
        headers={
            "Content-Disposition": "attachment;filename=Vanilla_Tweaks_for_1.8.9.zip"
        },
    )


if __name__ == "__main__":
    app.run(debug=True)
