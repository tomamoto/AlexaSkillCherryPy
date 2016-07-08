#!/usr/bin/python

import cherrypy
import random
import json
import sys
import logging

logging.basicConfig(filename='cherry.log',level=logging.WARNING)

#Define app version
version = ".01"

def JoshTomar():
	#This is just a strupid function wrote to return a random phrase to answer the any of the questions associated with the intent "GetTheMan"
	phrases = ["Joshua Tomar", "Joshua Tomar, of course.", "That guy who lives in this house.  I think his name is Joshua Tomar.", "Obviously my main man, Joshua Tomar", "That one's easy.  Joshua Tomar"]
	phrase = random.choice(phrases)
	return phrase

def WriteResponse(speech):
	#This function creates an object contains a valid Alexa response, which we will then return as a JSON string

	response = 	{ 'version': version,
			'response': {
				'outputSpeech': {
					'type': 'PlainText',
					'text': speech },
				'shouldEndSession': True }
			}
			

	#We need to do a final json.loads because cherrypy's decorators are already going to apply json.dumps to our output, which we don't want happening twice or we get ugly unusable output.
	return json.dumps(response)

class AlexaModel(object):
	def index(self):
		return "Web Service is Up"
	index.exposed = True

	#Here is where the actual Alexa stuff is defined.  Note the three decorators below.  I have SSL set up on nginx and a pass_proxy argument for http://127.0.0.1:9090/alexa to match the default config in server.conf
	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def alexa(self):
		try:
			#This takes advantage of the json_in decorator to convert the whole request body to dictionary
			body = cherrypy.request.json
			#We are logging the body of the json request because we needed to see what Amazon was actually sending.  It's surprising how there were no examples of a standard session in terms of JSON in the Alexa Skills Kit.
			logging.debug("JSON REQUEST:")
			logging.debug(body)
			#This next line should be all you need to grab the intent stated by Alexa
			if body["request"]["type"] == u'IntentRequest':
				intent = body["request"]["intent"]["name"]
				if intent == u'GetTheMan':
					message = JoshTomar()
					output =  WriteResponse(message)
					return output
				else:
					message = "This is an unrecognized intent. Fix it."
					output = WriteResponse(message)
					return output
			else:
				output = WriteResponse("We're done here.")
				return output
		except:
			message = "An Unhandled Exception occured.  Go fix it, numb nuts."
			output = WriteResponse(message)
			return output
			raise


cherrypy.config.update("server.conf")
cherrypy.quickstart(AlexaModel())
