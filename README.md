# Overview

this is a Django separate module App for Custom Token generate for APIs with custom token key and token value as Authorization.

### Example 
You can add as basic Authorization in Headers
	`Headers: { 
			CUSTOMTOKENKEY: custom token value 
		  }`


### Example
You can also add as a additional along with basic Authorization in Headers (it's optional).
	`Headers: { 
			Authorization: Bearer token, 
			CUSTOMTOKENKEY: custom token value 
		  }`

It will make more secure in middleware.

## Requirements
* Python (3.5, 3.6, 3.7, 3.8, 3.9)
* Django (2.2, 3.0, 3.1, 3.2.*)
We highly recommend and only officially support the latest patch release of each Python and Django series.

## Installations

* git clone the source destination from https://github.com/DpDew/customtoken

	git clone https://github.com/DpDew/customtoken.git

* add `customtoken` in your project and add to `INSTALLED_APPS` in setting.py

	```python
	INSTALLED_APPS = [
			    '....', 
			    'customtoken'
			 ]
			 

* add middleware in setting.py
	```python
	MIDDLEWARE = [
			'customtoken.customaccessmiddleware.CustomMiddleware', 
			'....'
		     ]
		     

* add your own custom key name (<CUSTOMTOKEN>)

	CUSTOMTOKENKEY = <CUSTOMTOKEN> ('Capital Letter')

* then finally make migration and migrate

	`python3 manage.py makemigrations`
	and
	`python3 manage.py migrate`

* then run 

	`python3 manage.py runserver`


# Control to CUSTOMTOKEN App
when user open django admin panel there it will show APIUSERS and APIKEYS

* create user from APIUSERS

* create Api key from APIKEYS according to user created from APIUSERS

after this admin can control apikey Activate or Deactivate or Delete on API ENDPOINT anytime.

It is tested using postman and as well as in curl request where it added to Headers

