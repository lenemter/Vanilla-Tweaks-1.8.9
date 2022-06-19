import zipfile as z
from io import BytesIO
import warnings

in_memory_file = BytesIO()
zips = [in_memory_file, "patches/vibrant_bed.zip", "new_default_textures.zip"]


with z.ZipFile(zips[0], "a") as z1:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for fname in zips[1:]:
            with z.ZipFile(fname, "r") as zf:
                for name in zf.namelist():
                    if name not in z1.namelist():
                        z1.writestr(name, zf.open(name).read())


with open("output.zip", "wb") as f:
    f.write(in_memory_file.getbuffer())
