from flask import Blueprint

auth = Blueprint('auth',__name__)

# 这段引用必须在蓝本定义的下面~~不懂为什么
from . import views