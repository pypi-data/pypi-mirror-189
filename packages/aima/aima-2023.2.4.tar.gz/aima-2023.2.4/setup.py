# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aima', 'aima.hobs']

package_data = \
{'': ['*'], 'aima': ['images/*']}

install_requires = \
['nessvec>=0.0.18,<0.0.19']

entry_points = \
{'console_scripts': ['nessvec = nessvec.main:main']}

setup_kwargs = {
    'name': 'aima',
    'version': '2023.2.4',
    'description': 'Alias that redirects to nessvec',
    'long_description': '# Introduction\n\nThis file gives an overview of the Python code for the algorithms in the textbook Artificial Intelligence: A Modern Approach, also known as AIMA. The code is offered free for your use under the MIT License. As you may know, the textbook presents algorithms in pseudo-code format; as a supplement we provide this code. The intent is to implement all the algorithms in the book, but we are not done yet.\n\n# Prerequisites\n\nThe code is meant for Python 2.5 through 2.7.\n\n# How to Browse the Code\n\nYou can get some use out of the code here just by browsing, starting at the root of the source tree or by clicking on the links in the index on the project home page. The source code is in the .py files; the .txt files give examples of how to use the code.\n\n# How to Install the Code\n\nIf you like what you see, install the code using either one of these methods:\n\nFrom a command shell on your computer, execute the svn checkout command given on the source tab of the project. This assumes you have previously installed the version control system Subversion (svn).\nDownload and unzip the zip file listed as a "Featured download"on the right hand side of the project home page. This is currently (Oct 2011) long out of date; we mean to make a new .zip when the svn checkout settles down.\n\nYou\'ll also need to install the data files from the aima-data project. These are text files that are used by the tests in the aima-python project, and may be useful for yout own work.\n\nYou can put the code anywhere you want on your computer, but it should be in one directory (you might call it aima but you are free to use whatever name you want) with aima-python as a subdirectory that contains all the files from this project, and data as a parallel subdirectory that contains all the files from the aima-data project.\n\n# How to Test the Code\n\nFirst, you need to install Python (version 2.5 through 2.7; parts of the code may work in other versions, but don\'t expect it to). Python comes preinstalled on most versions of Linux and Mac OS. Versions are also available for Windows, Solaris, and other operating systems. If your system does not have Python installed, you can download and install it for free.\n\nIn the aima-python directory, execute the command\n\n    python doctests.py -v *.py\n\nThe "-v" is optional; it means "verbose". Various output is printed, but if all goes well there should be no instances of the word "Failure", nor of a long line of "". If you do use the "-v" option, the last line printed should be "Test passed."\n\n# How to Run the Code\n\nYou\'re on your own -- experiment! Create a new python file, import the modules you need, and call the functions you want.\n\n# Acknowledgements\n\nMany thanks for the bug reports, corrected code, and other support from Phil Ruggera, Peng Shao, Amit Patil, Ted Nienstedt, Jim Martin, Ben Catanzariti, and others.',
    'author': 'Peter Norvig (norvig)',
    'author_email': 'peter.norvig@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/tangibleai/community/aima',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
