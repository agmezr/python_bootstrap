# Python bootstrap

A simple python project used as a base to start working quickly. The base of the project doesn't use any frameworks but for convenience I have included sqlalchemy and a test to ensure everything is ready to go.

## How to use?

Simply cloning the project allows to start working right away but assuming that you use virtual environment (and you should!) the makefile helps you to setup the project. The commands that you can use for the makefile are:

* `make clean` will delete all `.pyc` files on the project

* `make build` will create the virtual environment with name specified on the make file and install the libraries specified on `requirements.txt`. By default the name of the folder is `venv` and the only library installed by pip will be sqlalchemy, please edit `requirements.txt` to suit your needs.

* `make test` will activate the virtual environment and run the `run_test.py` script. The output of the script helps to ensure that sqlalchemy and the logger are working fine.

## Requirements

* Pip
* Python 2
* python-setuptools
* make
* python-dev
