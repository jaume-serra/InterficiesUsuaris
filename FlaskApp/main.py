
# coding: utf-8
# #!/usr/bin/python

from flask import Flask
app = Flask(__name__)
from DATABASE.db import set_up

set_up()

from routes import *


app.run(host="0.0.0.0")
