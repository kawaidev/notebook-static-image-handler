import os
from os.path import join as pjoin

from jupyter_packaging import (
  ensure_python, get_version    
)
import setuptools

name="notebook_static_image_handler"

ensure_python(">=3.5")

version = get_version(pjoin(name, "_version.py"))

setup_args = dict(
    name=name,
    version=version,
    author="kawaidev",
    author_email="kawai.dev.py@gmail.com",
    url="https://github.com/kawaidev/notebook-static-image-handler",
    description="A notebook server extension for static image handler",
    packages=setuptools.find_packages(),
    install_requires=[
        "jupyterlab~=2.0",
    ],
    license="MIT"
)

if __name__ == '__main__':
    setuptools.setup(**setup_args)
