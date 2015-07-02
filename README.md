# AlexaSkillCherryPy
Illustrates a very simple (and egotistical) Amazon Alexa skill using CherryPy's very helpful JSON in/out decorators.

Amazon directory contains intent schema and sample utterances that would normally be entered in your Amazon Developer Console and is not a part of the actual code in use here.  It is meant to give a better idea of what we're actually doing here.

Note:  As of now this is still in very early stage and is not compliant with Alexa's regulations as it does not validate the source of the query.  This is deliberate for the time being as its much more efficient to simulate Amazon's requests in SOAPUI to work out the kinks.  Especially because the exact formatting of the JSON requests did not seem to be clearly documented.
