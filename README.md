# AlexaSkillCherryPy
Illustrates a very simple (and egotistical) Amazon Alexa skill using CherryPy's very helpful JSON in/out decorators.

Amazon directory contains intent schema and sample utterances that would normally be entered in your Amazon Developer Console and is not a part of the actual code in use here.  It is meant to give a better idea of what we're actually doing here.

##Dependencies

**Python** (obviously)
All testing done with Python 2.7, but should work with any version that's compatible with CherryPy.
Ubuntu example:
```apt-get install python```

**CherryPy Python Module**
```pip install cherrypy```

**nginx** (or some other HTTP proxy that can handle your TLS/SSL)
Ubuntu example:
```apt-get install nginx```

## Usage

Before testing, please copy **config.py.example** to a new file called **config.py** and update your **app_id** within to reflect to reflect the actual application ID assigned to you by Amazon.  If this is not correct, the validation (required by Amazon for security purposes) will fail and you will be accused of tomfoolery.

The file server.conf is currently set up to host the web interface on all localhost (127.0.0.1) at TCP port 9090.  Feel free to customize this. 

To test the actual app, you'll have to run a proxy server (I use nginx) that already has a valid cerificate that you've set up Alexa services to respect.  In nginx, a simple proxy pass to your configured URL with the path **/alexa** should allow it to hand off to our CherryPy service here once it's started.  

Example of what I would place under my **location /** in the nginx config file (which itself should be setup using proper SSL configuration):
```
proxy_pass http://127.0.0.1:9090/alexa;
```

Finally, to run the Alexa skill service itself, we simply execute `alexa_fatlad.py` from the command line and presto, we should have our web service up and running.  Now we should be able to point Amazon at our server's domain and start testing.
