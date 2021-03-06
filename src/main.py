from flask import Flask, render_template, request, Response

from functools import cache
from io import BytesIO
import json
import logging
from os import getenv
from pathlib import Path
from zipfile import ZipFile


app = Flask(__name__)


CATEGORIES = [
    "Aesthetic",
    "Terrain",
    "Variation",
    "Connected Textures",
    "Utility",
    "Unobtrusive",
    # "HUD",
    # "GUI",
    # "Options Backgrounds",
    # "Menu Panoramas",
    # "Retro",
    # "Fun",
    # "Parity",
    "Fixes",
    "Hypixel",
]

# @cache
def index_template():
    TWEAKS_FOLDER = Path("./src/static/tweaks/")
    folders = [f for f in TWEAKS_FOLDER.glob("*") if f.is_dir()]
    tweaks = []
    for folder in folders:
        filename = folder.absolute() / "data.json"
        try:
            with open(filename) as file:
                data = json.load(file)
                tweaks.append(data)
        except Exception:
            logging.error(f"TWEAKS: {filename} not found.")

    return render_template("index.html", tweaks=tweaks, categories=CATEGORIES)


# @cache
def create_zip(args: list) -> bytes:
    in_memory_file = BytesIO()
    zips = [f"src/static/tweaks/{tweak}/tweak.zip" for tweak in args] + [
        "new_default_textures.zip"
    ]

    with ZipFile(in_memory_file, "w") as z1:
        for fname in zips:
            with ZipFile(fname, "r") as zf:
                for name in zf.namelist():
                    if name not in z1.namelist():
                        z1.writestr(name, zf.open(name).read())

    return in_memory_file.getvalue()


@app.route("/", methods=["GET"])
def index():
    return index_template()


@app.route("/download", methods=["GET"])
def download():
    args = list(request.args)
    data = create_zip(args)
    return Response(
        response=data,
        mimetype="application/zip",
        headers={
            "Content-Disposition": "attachment;filename=Vanilla_Tweaks_for_1.8.9.zip"
        },
    )


if __name__ == "__main__":
    port = getenv("PORT", default=5000)
    app.run(port=port, debug=True)
