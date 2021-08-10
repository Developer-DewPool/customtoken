A) Installations

this is a Django separate module App for Custom Token generate for APIs with custom token key and token value as Authorization.
Example: Headers: { <CUSTOMTOKENKEY>: <token value> }

You can add as a additional along with basic Authorization in Headers (it's optional).
Example: Headers: { Authorization: Bearer token, <CUSTOMTOKENKEY>: <token value> }

It will make more secure in middleware.

1. git clone the source destination from https://github.com/DpDew/customtoken

	git clone https://github.com/DpDew/customtoken.git

2. add 'customtoken' in your project and add to INSTALLED_APPS in setting.py

	INSTALLED_APPS = [
			    '....', 
			    'customtoken'
			 ]

3. add middleware in setting.py
	MIDDLEWARE = [
			'customtoken.customaccessmiddleware.CustomMiddleware', 
			'....'
		     ]

4. add your own custom key name (<CUSTOMTOKEN>)

	CUSTOMTOKENKEY = <CUSTOMTOKEN> ('Capital Letter')

5.then finally make migration and migrate

	python3 manage.py makemigrations
	and
	python3 manage.py migrate

6. then run 

	python3 manage.py runserver


B) control to apitoken key
when user open django admin panel there it will show APIUSERS and APIKEYS

1. create user from APIUSERS

2. create Api key from APIKEYS according to user created from APIUSERS

after this admin can control apikey Activate or Deactivate or Delete on API ENDPOINT anytime.

It is tested using postman and as well as in curl request where it added to Headers

