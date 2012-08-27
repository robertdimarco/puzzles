#!/usr/bin/env python
#
# sha1 padding/length extension attack class
# by rd@vnsecurity.net
#

import sha
import struct 
import base64

class shaauth:
	def __init__(self, secret, verbose=1):
		self.secret = secret

	def sign(self, msg):
		data = self.secret + msg
		m = sha.new()
		m.update(data)
		sig = m.hexdigest()
		return sig

	def verify(self, msg, sig):
		data = self.secret + msg
		m = sha.new()
		m.update(data)
		sig2 = m.hexdigest()
		return sig2 == sig

# attack class on sha1 length-extension
class shaext:
	def __init__(self, origtext, keylen, origsig):
		self.origtext = origtext 
		self.keylen = keylen
		self.origsig = origsig
		self.addtext = ''
		self.init()

	def init(self):

		count = (self.keylen + len(self.origtext)) * 8
		index = (count >> 3) & 0x3fL
		padLen = 120 - index
        	if index < 56:
            		padLen = 56 - index
	        padding = '\x80' + '\x00' * 63
	        
        	self.input = self.origtext + padding[:padLen] + struct.pack('>Q', count)
        	count = (self.keylen + len(self.input)) * 8
		self.m = sha.new()	
        	self.m.count = [0, count]
        	     
        	_digest = self.origsig.decode("hex")
        	(self.m.H0, self.m.H1, self.m.H2, self.m.H3, self.m.H4) = struct.unpack(">IIIII", _digest)
		
	def add(self, addtext):
		self.addtext = self.addtext + addtext
		self.m.update(addtext)
		
	def final(self):
		new_sig = self.m.hexdigest()
		new_msg = self.input + self.addtext			
		return (new_msg, new_sig)

def testattack():
	key = "topsecret"
	keylen = len(key)
		
	auth = shaauth(key)

	# sign the msg		
	orig_msg = "this is orig test message"
	orig_sig = auth.sign(orig_msg)

	# test the length extension attack		
	add_msg = "this is addition message"
	ext = shaext(orig_msg, keylen, orig_sig)
	ext.add(add_msg)
	(new_msg, new_sig)= ext.final()
		
	# verify the new msg
	assert auth.verify(new_msg, new_sig)

if __name__=="__main__":
	testattack()