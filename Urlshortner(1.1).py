#!usr/bin/env python3
import os
import requests

os.system("clear")

print("""                                   
--.--o                        |    
  |  .,---.,   .    .   .,---.|    
  |  ||   ||   |    |   ||    |    
  `  ``   '`---|    `---'`    `---'
           `---'                   """)
           
print("<--------Coded By Copycat-------->")
print("")

site = input("[+] Site Name: ")
apiurl = "https://tinyurl.com/api-create.php?url="
result = apiurl + site

def tinyurl():
	try:
		r = requests.get(result)
		r.raise_for_status()
		print("[+] " +r.text)
	except:
		print("[-] oops..!! Error Or Invalid Site")
	
tinyurl()
