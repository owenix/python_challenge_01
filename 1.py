#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
import re

formatted = []

def shift_chars(message):
	print(message)
	for mess in message:
		formatted.append(chr(ord(mess)+2))

shift_chars(message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
print(' '.join(formatted))
