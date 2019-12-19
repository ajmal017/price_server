# HOW TO RUN

- Checkout the repository from git.
- Make sure you have a distribution python 3.8 or python 3.7 installed. In case
of doubt, download Python 3.8 from python.org.
- Go the directory price_server where the repo is downloaded do the following

## On Linux or MacOS or Windows WSL
<path_to_python> -m venv ./venv 
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install fastapi[all]
cd src
python ./run.py

Please ensure you are calling the python you installed. MacOS has an old version
of Python 2.7 installed by default. Various Linux distros may have various old
versions of Python installed by default. If you installed python from python.org
on Macos it will usually be installed in /usr/local/bin

One way to ensure you are calling the right one is to do <path_to_python> --version
and look at the output.

## On Windows (using Powershell)
<path_to_python> -m venv .\venv
.\venv\Scripts\activate.ps1
python -m pip install --upgrade pip
python -m pip install fastapi[all]
cd src
python .\run.py

Please ensure you are calling the right version of Python. Python 3.8 from python.org
will install in C:\Program Files\Python38

One way to ensure you are calling the right one is to do <path_to_python> --version
and look at the output.


