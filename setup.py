import setuptools
from setuptools import setup, find_packages

setup(
    name="MakeDjango",
    version="1.0.0",
    install_requires=[
        "setuptools",
        "wheel",
        "asgiref==3.4.1",
        "pytz==2021.3",
    ],
    packages=["MakeDjango"],
    package_data={'MakeDjango': ["core/*.py", "template/*.py"]},
    include_package_data=True,
    zip_safe=False
)
