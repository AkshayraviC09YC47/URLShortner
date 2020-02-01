#!/usr/bin/env python3
#Url Shortner created by Akshay Ravi
import os
import subprocess
import urllib.request
from termcolor import colored

os.system("clear")

subprocess.call('figlet "TINY-URL"' , shell=True)
print("-" * 45)
print("  URL Shortner Coded By Akshay Ravi C09YC47")
print("-" * 45)
print("")

#Define the process (url)
def tiny_url(url):
	apiurl = "https://tinyurl.com/api-create.php?url="
	#url requests to open the given link to browser and give back the result
	tinyurl = urllib.request.urlopen(apiurl + url).read()
	#Return the process with utf encode & decode
	return tinyurl.decode("utf-8")
	
url = input("[+]Enter The URL: ")
print(colored("[+]" + tiny_url(url) , "yellow"))
	
