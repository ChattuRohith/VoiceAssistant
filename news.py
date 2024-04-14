from newsapi import NewsApiClient
import pycountry
import speech_recognition as sr
from wakeWord_detect import speak
import sounddevice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 10, 10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if len(query.strip()) == 0:
            speak("Empty command")
            print("Try saying...\nPlay songs\nOpen youtube\nTell jokes")

    except Exception as e:
        print(e)
        print("Linux Assistant: I am sorry, I am Unable to Recognize your voice.")
        speak("I am sorry, I am Unable to Recognize your voice.")

    return query

# you have to get your api key from newapi.com and then paste it below
newsapi = NewsApiClient(api_key='04b548362d2d46ec920c68c3f15277ff')

# now we will take name of country from user as input
input_country = 'India'
input_countries = [f'{input_country.strip()}']
countries = {}

# iterate over all the countries in
# the world using pycountry module
for country in pycountry.countries:

	# and store the unique code of each country
	# in the dictionary along with it's full name
	countries[country.name] = country.alpha_2

# now we will check that the entered country name is
# valid or invalid using the unique code
codes = [countries.get(country.title(), 'Unknown code')
		for country in input_countries]

# now we have to display all the categories from which user will
# decide and enter the name of that category
print("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
option = takeCommand()
# now we will fetch the new according to the choice of the user
top_headlines = newsapi.get_top_headlines(

	# getting top headlines from all the news channels
	category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

# fetch the top news under that category
Headlines = top_headlines['articles']
c = 0
# now we will display the that news with a good readability for user
if Headlines:
		for articles in Headlines:
			b = articles['title'][::-1].index("-")
			if "news" in (articles['title'][-b+1:]).lower():
				print(
					f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
				speak(f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
			else:
				print(
					f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
				speak(f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
			c= c+1
			if c==5:
				break

else:
	print(	f"Sorry no articles found for {input_country}, Something Wrong!!!")
	speak(f"Sorry no articles found for {input_country}, Something Wrong!!!")