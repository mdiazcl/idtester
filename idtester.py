# ----------------------- #
# IDTester.py
# 
# The idea behind this plugin is to quickly hijack accounts using
# the actual Username and Password of an user. I need a better explanation...
# god...I suck at this
# ----------------------- #

from Modules.LoginMechanize import LoginMechanize
from termcolor import colored
import os, sys

print " - IDTester v0.1 - MultiSite credential tester"
print " --------------------------------------------------------"
print " "
print " The idea behind this tool is to test the same credential in multiple sites"
print " for now, it only does that, I pretend in futher versions to be able to change"
print " passwords or update account details."
print " "
print " This software is intended for personal use (your own credentials), if you use"
print " this for other purposes is not of my concern."
print " "
print "                    # By mdiazcl - [miguel.diaz{at}mdiazlira.com]"
print " --------------------------------------------------------"
print " "


# Get information from the user
# If someone wants to make an Argparse, go ahead, you are free to do it
# please do it...
user = str(raw_input("What is the username to test? [Required]:  "))
if not user:
	print "The software needs an username to work :( sorry."

password = str(raw_input("What is the password of that username? [Required]:  "))
if not password:
	print "The software needs a password to work :( sorry."

print " --------------------------------------------------------"
test_all = False
sites_question = str(raw_input("Do you want me to test all the sites on the Sites/ folder? [Y/n] "))
if not sites_question or sites_question.lower() == "y" or sites_question.lower() == "yes":
	test_all = True

print " --------------------------------------------------------"
print "So let's go..."
print " --------------------------------------------------------"
# Get Site list
print "Reading local site databases..." #Maybe on future we will have an Online one, with all the jsons available
sites_to_test = []
for filename in os.listdir("Sites"):
    if filename.endswith(".json"):
        sites_to_test.append(filename)

# Lets test our credentials!
lm = LoginMechanize()

for jsonsite in sites_to_test:
	# Test the site?
	if not test_all:
		test_site = str(raw_input("Do you wish to test [{0}]? [Y/n] ".format(jsonsite[:-5])))
		if test_site.lower() == "n" or test_site.lower() == "no":
			continue

	# Do the testing...
	print "Testing {0} ... ".format(jsonsite[:-5]),
	sys.stdout.flush()

	result = lm.test_credential(jsonsite, user, password)
	if result:
		print colored('Works!', 'green')
	else:
		print colored('Not working :(', 'red')