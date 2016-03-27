from .base import *

try:
	from .local import *
except ImportError:
	print("Can't find module settings local! Make if from local.py.skeleton")