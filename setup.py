import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter", "json", "ttkthemes"], "include_files": ["YokaiData.json", "icon.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("GUI.py", base=base, target_name="Blasters3dbEditor.exe")
]


setup(
    name="YKWB3 Editeur de BDD",
    version="1.0",
    description="L'éditeur de base de données pour Yo-kai Watch Blasters 3 : un fangame tah les ouf créé par Liska !",
    options={"build_exe": build_exe_options},
    executables=executables
)
