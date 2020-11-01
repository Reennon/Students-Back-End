ReadMeFile
Laboratory 4, variant 12 (pipenv + Python 3.6.*)
-------------


### ReadMeGuide

1. #### Pyenv
Ensure Pyenv installed correctly, typing a following command in the cloned folder
```
pyenv --version
```
If it outputs something else, but actual pyenv version, please make sure, Pyenv installed properly

2. #### Install Python 3.6.*
Personally, I've installed Python 3.6.8
```
pyenv install 3.6.8
```
Select pyenv local, and activate it
```
pyenv local 3.6.8
python -m venv env
.\env\Scripts\activate
```
Now console's prefix should look like
_(env)_ *someDirectory/etc/*

3. #### Install Flask 
To install Flask type a command from below
```
pip install flask
```
It should show the percents, and the current status of the total installation process
###### 100% |████████████████████████████████|
###### Successfully installed...etc

4. #### Install Gevent
To install Gevent complete a next line into your console
```
pip install gevent
```
It should show the percents, and the current status of the total installation process
###### 100% |████████████████████████████████|
###### Successfully installed...etc
> ######Should be the same as the previous step

5. #### Pycharm Initialization
Firstly, open recently cloned repo, as a folder in Pycharm
Then, manage python interpreter, to one in pyenv's folder:
###### env\scripts\Python.exe
and select it

6. #### Run a gevent py file
You might want to use pycharm, or simply run as a python executable file, but **_ensure_** that python interpreter you are about to run, has the needed libraries with comparable versions (Flask, Gevent)

7. #### Open tab in a browser
In an adress line type:
```
http://localhost/
```
or
```
http://localhost/api/v1/hello-world-12
```
The link above is identical to the needed in individual task for the laboratory, so here it is!
Enjoy)
