from setuptools import setup, find_packages
from src.core.processor import __version__

setup(
    name="MakeDjango",
    version=__version__,
    install_requires=[
        "asgiref==3.4.1",
        "pytz==2021.3",
    ],
    packages=find_packages(),
    zip_safe=False

)
