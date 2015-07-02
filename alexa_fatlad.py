#!/usr/bin/python

import cherrypy
import random
import json
import sys
import logging

logging.basicConfig(filename='cherry.log',level=logging.DEBUG)


def JoshTomar():
	phrases = ["Joshua Tomar", "Joshua Tomar, of course.", "That guys who lives in this house.  I think his name is Joshua Tomar.", "Obviously my main man, Joshua Tomar", "That one's easy.  Joshua Tomar"]
	phrase = random.choice(phrases)
	print(phrase)
	return phrase	
	  
class AlexaModel(object):
	def index(self):
		return "Web Service is Up"
	index.exposed = True

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def alexa(self):
		try:
			body = cherrypy.request.json
			logging.debug("JSON REQUEST:")
			logging.debug(body)
			intent = body["request"]["intent"]["name"]
			if intent == u'GetTheMan':
				message = JoshTomar()
				output =  {"outputSpeech": message , }
			else:
				message = "This is an unrecognized intent. Fix it."
				output = {"outputSpeech": message }
			return output
		except:
			return {"outputSpeech": "An Unhandled Exception occured.  Go fix it, numb nuts." }
			raise


cherrypy.config.update("server.conf")
cherrypy.quickstart(AlexaModel())
