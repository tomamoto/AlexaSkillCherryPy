# AlexaSkillCherryPy
Illustrates a very simple (and egotistical) Amazon Alexa skill using CherryPy's very helpful JSON in/out decorators.

Amazon directory contains intent schema and sample utterances that would normally be entered in your Amazon Developer Console and is not a part of the actual code in use here.  It is meant to give a better idea of what we're actually doing here.

Before testing, please copy **config.py.example** to a new file called **config.py** and update your **app_id** within to reflect to reflect the actual application ID assigned to you by Amazon.  If this is not correct, the validation (required by Amazon for security purposes) will fail and you will be accused of tomfoolery.
