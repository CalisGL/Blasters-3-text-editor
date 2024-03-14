import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter", "json", "ttkthemes"], "include_files": ["dialogues.json", "icon.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("GUI.py", base=base, target_name="Blasters3txtEditor.exe")
]


setup(
    name="YKWB3 Editeur de dialogues",
    version="1.0",
    description="L'éditeur de dialogeus pour Yo-kai Watch Blasters 3 : un fangame tah les ouf créé par Liska !",
    options={"build_exe": build_exe_options},
    executables=executables
)
