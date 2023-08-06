import shutil
import json, os
from pathlib import Path

from .lib import FileLib
from .parser.meta import MetaParser

def generate(path: str = '', property_file: str = "pack.json", gen_dir: str = "generated"):
    gen_path = FileLib.regenerate_dir(os.path.join(path, gen_dir))

    parsed_prop = MetaParser(property_file).parse()
    with open(gen_path.as_posix() + "/pack.mcmeta", "w") as pack_meta:
        json.dump(parsed_prop, pack_meta)

    pack_img = Path(os.path.join(path, "pack.png"))
    if pack_img.exists(): shutil.copyfile(pack_img.as_posix(), "generated/pack.png")

    working_directory = os.getcwd()
    for (path, dir, files) in os.walk(os.path.join(working_directory, "data")):
        for file in files:
            current_file_path = Path(os.path.join(path, file))
            if current_file_path.suffix == '.ds':
                print(current_file_path)
                print(path)
                print(file)

    FileLib.zip_dir("generated", "generated.zip")