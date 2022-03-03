# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 23:11:33 2022

@author: jerem
"""

from flask import Flask

app = Flask(__name__)


@app.route('/CryptoVelo/CryptoAdoptionMap')
def hello():
    return 'Hello, World!!!!!'