#Post answers via Typeform 
import random
from random import getrandbits
import requests

url = "https://oki-ni.typeform.com/app/form/submit/Dl5m5y"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

emails = []

for i in range(1,8000):
	email = "emailaddress+{}@gmail.com".format(getrandbits(40))
	emails.append(email)

unique_email = list(set(emails))

def submit_request(*args):
	for email in unique_email:
		
		token = requests.post("https://websitename.typeform.com/app/form/result/token/Token_id/default", headers = headers).content# replace websitename and Token_id to generate tokens
		
		postdata = {"form[language]":"en",
					"form[textfield:42353001]":"",#name
					"form[textfield:42353002]":email,#email address
					"form[dropdown:42353005]":"",#Country for delivery
					"form[dropdown:42353006]":"UK ",#Shoe size
					"form[textfield:42353003]":"",#ins
					"form[textfield:42353004]":"",#twtter
					"form[token]":token 
					}

		response = requests.post(url, headers = headers, data = postdata)
		print response.text, response.status_code
		print "{}/{} registered.".format(unique_email.index(email)+1, len(unique_email))

if __name__ == '__main__':
	submit_request()		