dbhost = ''
dbport = ''
dbdatabase = ''
dbuser = ''
dbpass = ''

export FLASK_APP=start.py
export DATABASE_URI=mysql+pymysql://$(dbuser):$(dbpass)@$(dbhost):$(dbport)/$(dbdatabase)

server: 
	export APPLICATION_ENVIRONMENT=development
	python3 -m start

production:
	export APPLICATION_ENVIRONMENT=production
	python3 -m start