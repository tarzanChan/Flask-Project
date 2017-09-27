# -*- coding: utf-8 -*-
# author by : GoogleSmile

from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views
