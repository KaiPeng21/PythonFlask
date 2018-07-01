
# flask-login Example

1. Install the required libraries listed in `requirements.txt`

```
pip3.6 install -r requirements.txt
```

2. Add environment variables (Flask Secret Key, Database Parameters, ...) listed in `config.py` file using `export` command in the terminal.

3. Run `setup.py` to create the user table in your MySQL database 

```
python3.6 setup.py
```

4. Run `app.py` and go to `localhost:5000` in youor browser to navigate the login example

```
python3.6 app.py
```
