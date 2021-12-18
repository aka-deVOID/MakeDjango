from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="MakeDjango",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="1.1.1",
    install_requires=[
        "setuptools",
        "wheel",
        "asgiref==3.4.1",
        "pytz==2021.3",
        "prompt-toolkit==1.0.14",
        "pyfiglet==0.8.post1",
        "PyInquirer==1.0.3"
    ],
    packages=["MakeDjango"],
    package_data={'MakeDjango': ["core/*.py", "template/*"]},
    include_package_data=True,
    zip_safe=False
)
