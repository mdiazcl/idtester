# ----------------------- #
# LoginMechanize.py
# 
# This class is intenteded to simulate all logins and get results if the login
# was correct or not. The idea behind this is to be able to code easily new sites or
# update outdated ones.
#
# If someone has a better (well written) description for this class PLEASE do a RFP
# My native language is Spanish and I'm doing my best to comment everything in english
# ----------------------- #
import json
import mechanize

# Fix Mechanize
from MechanizeFix import *
monkeypatch_mechanize()

class LoginMechanize():
	def test_credential(self, site_json, _user, _passwd):
		# Load Site Data
		site_json_file = open("Sites/{0}".format(site_json))
		site_data = json.loads(site_json_file.read())

		self.site_login_url = site_data['site_login_url']
		self.site_test_url = site_data['site_test_url']
		self.regex_match_success = site_data['regex_match_success']
		self.regex_match_fail = site_data['regex_match_fail']
		self.form_number = site_data['form_number']

		self.username_field = site_data['username_field']
		self.password_field = site_data['password_field']

		# Load Credentials
		self.user = _user
		self.passwd = _passwd

		# Setting the browser
		br = mechanize.Browser()
		br.set_handle_robots(False)

		# User-Agent
		br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
		br.open(self.site_login_url)

		# Test that we can see something
		assert br.viewing_html()

		# Do the actual login on "form_number" form
		br.select_form(nr=int(self.form_number))
		br.form[self.username_field] = self.user
		br.form[self.password_field] = self.passwd
		br.submit()

		# Test the response
		response = br.open(self.site_test_url)
		html_response = unicode(response.read(), 'utf-8')

		# Let's use our regex to test the result
		# OPTION 1) We know what to "expect" if we have a success or a fail
		if self.regex_match_success and self.regex_match_fail:
			if self.regex_match_success in html_response and self.regex_match_fail not in html_response:
				# We found our "success regex" on the response
				# login is successfull... I guess
				return True
			else:
				return False
		
		# OPTION 2) We just know if we have a success, but not a clear fail, so we asume that
		# 			if we have this we are in
		if self.regex_match_success:
			if self.regex_match_success in html_response:
				return True
			else:
				return False

		# OPTION 3) We just know if we have a fail, and, for some reason, thats enough
		#			If we don't see this fail, it means that we are in
		if self.regex_match_fail:
			if self.regex_match_fail in html_response:
				return False
			else:
				return True