from GoogleNews import GoogleNews
import pyjokes
import pywhatkit
from datetime import datetime
from pyowm.owm import OWM
import wikipedia

googlenews = GoogleNews()
googlenews = GoogleNews('en','d')
googlenews.search('India')
googlenews.getpage(0)
googlenews.result()
new = googlenews.gettext()

def sample_responses(input_text):
    
    user_message = str( input_text ).lower()
    text = set( user_message.split(' ') )

    if len( text.intersection({'hello', 'hi', 'sup'}) ) != 0:
        return "Hello :)"

    if user_message in ('who are you?', 'who are you'):
        return "I am the bot!"

    if len( text.intersection({"time", "time?"}) ) != 0:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    
    if user_message in ('where are you from?'):
        return "i am from python"
    
    if user_message in ("open facebook"):
        return  pywhatkit.search('Facebook')
    
    if user_message in ("open youtube"):
        return pywhatkit.search("youtube")
    
    if user_message in ('open yahoo mail'):
        return pywhatkit.search("yahoo mail")
    
    if user_message in ('who made you?'):
        return "Aaqil and Monisha"
    
    if user_message in ('which country do u belong to?'):
        return "canada"
    
    if user_message in ('tell me about yourself'):
        return "Hi i am Grembot you can chat with me ask me the time ask me the news and ask me a joke and so much more!"

    if user_message in ('how are you today?','how are you') :
        return 'I am good if you are good'

    if user_message in ('news', 'tell me the news') :
        return new
    
    if user_message in ('joke','tell me a joke'):
        return pyjokes.get_joke()

    if len( text.intersection({'weather', 'weather?'}) ) != 0:
        owm = OWM('2e2abc5781ed9df22dd627dd7555ac43')
        mgr = owm.weather_manager()
        weather = mgr.weather_at_place('Chennai,IN').weather
        temp_dict_celsius = weather.temperature('celsius')
        return str("Today's weather forecast : " + str(weather.detailed_status))

    if len( text.intersection({'temp', 'temperature'}) ) != 0:
        owm = OWM('2e2abc5781ed9df22dd627dd7555ac43')
        mgr = owm.weather_manager()
        weather = mgr.weather_at_place('Chennai,IN').weather
        temp_dict_celsius = weather.temperature('celsius')
        return str("The current Temperature is " + str(temp_dict_celsius['temp']))

    if len( text.intersection({'google', 'Google', 'search', 'Search'}) ) !=0 :
        inp = user_message.replace("Google", "").replace("google", "").replace("search", "").replace("Search", "")
        out = wikipedia.summary(inp, sentences=2)
        return str(out)

    return "I do not understand you."
