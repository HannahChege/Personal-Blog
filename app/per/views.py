from . import per

@per.route('/')
def index():
	return '<h1> Hello world </h1>'