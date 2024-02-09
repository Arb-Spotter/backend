run: 
	python manage.py runserver

inspectdb: 
	@python manage.py inspectdb > models.py

setup:
	pip3 install -r requirements.txt