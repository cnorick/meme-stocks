import urllib
from urllib import request

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "I am the ghost of Harambe. I am here to share with you " \
                    "my extensive knowledge of memes and their value. Go ahead, ask me about memes!" \
                    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Go ahead, ask me about memes."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Shot down again! Ha!"
                    
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_top_meme():
    return {"name": "harambe", "points": "420"}
    
def get_dankmeme ():
    dank_index = 40000
    url = "https://www.reddit.com/r/dankmemes/"
    req = urllib.request.Request (url, headers = {'User-agent': 'Harambe'})
    with urllib.request.urlopen (req) as response:
        page = response.read ().decode ('utf-8')
        
        begining_index = (page.find ('<a class="title may-blank " data-event-action="title" href=', dank_index))
        dank_index = begining_index
        # print(page [begining_index + 100 : begining_index + 150])
        begining_index = (page.find ('data-inbound-url', dank_index))
        dank_index = begining_index
        # print(page [begining_index : begining_index + 10])
        begining_index = (page.find ('rel="" >', dank_index));
        dank_index = begining_index
        # print(page [begining_index : begining_index + 10])
        begining_index = (page.find ('>', dank_index) + 1);
        dank_index = begining_index
        # print(page [begining_index : begining_index + 10])
        
        ending_index = (page.find ("<", dank_index))
        
        memeName = page [begining_index : ending_index]
        return memeName
        
def get_dankscore ():
    dank_index = 40000
    url = "https://www.reddit.com/r/dankmemes/"
    req = urllib.request.Request (url, headers = {'User-agent': 'Harambe'})
    with urllib.request.urlopen (req) as response:
        page = response.read ().decode ('utf-8')
        
        begining_index = (page.find ('<div class="score unvoted" title=', dank_index))
        dank_index = begining_index
        # print(page [begining_index : begining_index + 100])
        begining_index = (page.find ('>', dank_index) + 1)
        dank_index = begining_index
        # print(page [begining_index: begining_index + 10])
        
        ending_index = (page.find ("<", dank_index))
        
        memeScore = page [begining_index : ending_index]
        return memeScore

def get_dankest_meme(intent, session):
    card_title = intent["name"]
    session_attributes = {}
    should_end_session = True
    
    meme = get_top_meme()
    
    speech_output = "Right now, " + get_dankmeme() + " is the dankest meme with " + get_dankscore() + " points"
    reprompt_text = ""
    should_end_session = True
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetDankest":
        return get_dankest_meme(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
