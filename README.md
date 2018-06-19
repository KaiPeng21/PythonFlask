
# Learning Python Flask

## Intall Python Flask

Check the python3 version and ensure that a python 3.5 or newer version has been installed.
```
python3 --version
```

Check if virtualenv is installed
```
sudo pip3 install virtualenv
virtualenv --version
```

Create and activate an virtual environment
```
virtualenv flask_project
cd flask_project
source bin/activate
```

Install Python Flask
```
pip install Flask
```

Start a Hello World script

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return "<h1>Hello World!</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()
```

Run your hello world script and 
enter ** localhost:5000 ** in your browser.


## Hello World

p1_hello.py
