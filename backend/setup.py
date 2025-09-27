from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("getinfo", ["getinfo.py"]),
    Extension("main", ["main.py"]),
]

setup(
    ext_modules=cythonize(
        extensions,
        force=True,
        compiler_directives={"language_level": "3"},
        build_dir="CythonOut",   # ensure C files go here
    )
)