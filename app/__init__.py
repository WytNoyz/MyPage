#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Module init file"""

from flask import Flask

app = Flask(__name__)

from mypage import aboutme
from app import aboutme

