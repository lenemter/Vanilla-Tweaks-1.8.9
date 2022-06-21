from flask import Flask, render_template, request, Response

from io import BytesIO
from os import getenv
import zipfile as z


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/download", methods=["GET"])
def download():
    args = list(request.args)[1:]

    in_memory_file = BytesIO()
    zips = [f"patches/{patch}.zip" for patch in args] + ["new_default_textures.zip"]

    blacklist = set()

    with z.ZipFile(in_memory_file, "w") as z1:
        for fname in zips:
            with z.ZipFile(fname, "r") as zf:
                for name in zf.namelist():
                    if name not in z1.namelist() and name not in blacklist:
                        z1.writestr(name, zf.open(name).read())

    return Response(
        response=in_memory_file.getvalue(),
        mimetype="application/zip",
        headers={
            "Content-Disposition": "attachment;filename=Vanilla_Tweaks_for_1.8.9.zip"
        },
    )


if __name__ == "__main__":
    port = getenv("PORT", default=5000)
    app.run(port=port, debug=True)
