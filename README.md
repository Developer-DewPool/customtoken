A) Installations

this is a Django separate module App for Custom Token generate for different Api User with custom token key as custom name

1. install customtoken or git clone the source destination from bitbucket.org
	"git clone https://DpDew@bitbucket.org/DpDew/customtokengenerator.git"

2. add 'customtoken' to INSTALLED_APPS in setting.py

	INSTALLED_APPS = [
			'....', 
			'customtoken'
			]

3. add middleware in setting.py
	MIDDLEWARE = 	[
			'customtoken.customaccessmiddleware.CustomMiddleware', 
			'....'
			]

4. add custom key name in capital to variable after middleware

	CUSTOMTOKENKEY = <CUSTOMTOKEN> ('Capital Letter')

5.then finally make migration and migrate

	python3 manage.py makemigrations
	and
	python3 manage.py migrate

6. then run 

	python3 manage.py runserver


B) control to apitoken key
when user open django admin panel there it will show APIUSERS and APIKEYS

1. create user from Api users

2. create Api keys according to user

after this admin can control apikey Activate or Deactivate or Delete on API ENDPOINT anytime

