venv:
	virtualenv env
	bash -c 'source env/bin/activate'

install:
	pip2 install -t lib -r requirements.txt
