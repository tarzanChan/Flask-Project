# -*- coding: utf-8 -*-
# author by : GoogleSmile

from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views
