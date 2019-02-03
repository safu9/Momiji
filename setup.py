import sys

from cx_Freeze import setup, Executable


packages = [
    "pygments",
]
include_files = [
    "i18n", "res"
]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Momiji",
    version = "0.1",
    description = "simple cross-platform text editor",
    author = "Safu9",
    url = "",
    options = {
        "build_exe": {
            "packages": packages,
            "include_files": include_files
        }
    },
    executables = [Executable("main.py", base=base, icon="res/icon.ico")]
)
