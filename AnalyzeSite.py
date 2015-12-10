# ----------------------- #
# LoginMechanize.py
# 
# This is a simple analize to make JSON for the sites, for now it only helps me
# but if someone wants to make something more functional please do it
# ----------------------- #

import json
import mechanize

# Fix Mechanize
from Modules.MechanizeFix import monkeypatch_mechanize
monkeypatch_mechanize()

def SetBrowser():
	# set browser
	br = mechanize.Browser()
	br.set_handle_robots(False)

	# User-Agent
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	return br

def DetectForm(br):
	response = br.open("")

	k = 0
	for form in br.forms():
		print "form_number: {0}".format(k)
		print "Form name:", form.name
		print form
		k = k + 1

def GetFormsControls(br, form_number):
	response = br.open("")

	br.select_form(nr = form_number)
	for control in br.form.controls:
	    print control
	    print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

def GetSuccessLoginPage(br, form_number, user, passwd, login_page, test_page):
	# Get TestPage Without login
	response = br.open(test_page)
	output_file = file("no_login.txt", "wb+")
	output_file.write(response.read())
	output_file.close()

	# So Let's go <Zohan> Login
	response = br.open(login_page)
	#login
	br.select_form(nr=int(form_number))
	br.form["username"] = user
	br.form["password"] = passwd
	br.submit()

	#test url
	response = br.open(test_page)
	output_file = file("yes_login.txt", "wb+")
	output_file.write(response.read())
	output_file.close()


if __name__ == "__main__":
    browser = SetBrowser()

    #DetectForm(browser)
    #GetFormsControls(browser, 2)
    #GetSuccessLoginPage(browser, 2, "", "", "", "")