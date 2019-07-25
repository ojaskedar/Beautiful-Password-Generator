#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def random_password_genertor():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size,20))

def random_password_genertor_ico():
	random_password_genertor_ico = """
	#############################################################
	# PYTHON - BEAUTIFUL PASSWORD GENERATOR - CHUTIYA S0FTWARE  #
	############################################################# 
	#                         CONTACT                           #
	#############################################################
	#               DEVELOPER : OJAS KEDAR                      #
	#          Mail Address : ojaskedar00@gmail.com             #
	#							    #
	#              Whatsapp : + 91 9767213400                   #
	#############################################################
	"""
	print random_password_genertor_ico

random_password_genertor_ico()
print("Password : " + random_password_genertor())
