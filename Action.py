import datetime
import webbrowser
import os
import pyjokes
import wikipedia
import subprocess
import random
import socket
import pyperclip
import requests
import weather
from newsapi import NewsApiClient
import Speech_to_Text
from speak import speak
import pyautogui
import psutil
import ctypes
import platform
import pygetwindow as gw
import screen_brightness_control as sbc
import pycaw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from PyDictionary import PyDictionary
from PIL import Image
from tkinter import filedialog  # For file upload dialog
from calendar_event import create_event
from deep_translator import GoogleTranslator


# Initialize tools
newsapi = NewsApiClient(api_key='fbec855841074ab99454fef205423c4e')  # Replace with your News API key
dictionary = PyDictionary()

def change_wallpaper():
    try:
        # Open a file dialog to select the image file
        speak("Please select the wallpaper image file.")
        filepath = filedialog.askopenfilename(
            title="Select Wallpaper Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )

        if filepath and os.path.exists(filepath):
            # SPI_SETDESKWALLPAPER = 20
            # Update INI file = 1
            # Send change event = 2
            ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 3)
            speak("Wallpaper changed successfully.")
            return "Wallpaper changed successfully."
        else:
            speak("No file was selected or file does not exist.")
            return "No file was selected or file does not exist."

    except Exception as e:
        speak("Sorry, I couldn't change the wallpaper.")
        return f"Failed to change wallpaper: {str(e)}"


# ===== Action Function =====

def Action(send):
    data_btn = send.lower()

    if "what is your name" in data_btn:
        speak("My name is Virtual Assistant.")
        return "My name is Virtual Assistant."

    elif "who made you" in data_btn or "about you" in data_btn:
        info = "I was created by Team APT using Python, to help you with tasks."
        speak(info)
        return info
        

    elif "hello" in data_btn or "hi" in data_btn:
        speak("Hey sir, how can I help you!")
        return "Hey sir, how can I help you!"

    elif "how are you" in data_btn:
        speak("I am doing great these days sir.") 
        return "I am doing great these days sir."

    elif "thank you" in data_btn or "thanks" in data_btn:
        speak("It's my pleasure sir to stay with you.")
        return "It's my pleasure sir to stay with you."

    elif "good morning" in data_btn:
        speak("Good morning sir, I think you might need some help.")
        return "Good morning sir, I think you might need some help."
    
    elif "Lets see you again" in data_btn or "Lets see you tomorrow" in data_btn:
        speak("Ok, It was nice meeting you, See you soon")
        return "Ok, It was nice meeting you, See you soon."

    # Return current time
    elif "time now" in data_btn or "time" in data_btn:
        now = datetime.datetime.now()
        time = f"{now.hour} Hour and {now.minute} Minute"
        speak(time)
        return time

    # Return today's date
    elif "date today" in data_btn or "today's date" in data_btn:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
        return f"Today's date is {today}"

    # Return current day of the week
    elif "day today" in data_btn:
        day = datetime.datetime.today().strftime("%A")
        speak(f"Today is {day}")
        return f"Today is {day}"

    # Respond with a joke
    elif "joke" in data_btn:
        joke = pyjokes.get_joke()
        speak(joke)
        return joke

    # Respond with a random fun fact
    elif "fun fact" in data_btn:
        facts = [
            "Did you know? Honey never spoils.",
            "Bananas are berries, but strawberries are not.",
            "Octopuses have three hearts.",
            "A group of flamingos is called a flamboyance."
            "Why chicken is soo funny? Becauuuuuuuuuusee"
        ]
        fact = random.choice(facts)
        speak(fact)
        return fact

    # Get Wikipedia summary for a topic
    elif "wikipedia" in data_btn:
        try:
            topic = data_btn.replace("wikipedia", "").strip()
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
            return summary
        except Exception:
            speak("Sorry, I couldn't find anything.")
            return "No result found."

    # Open Notepad
    elif "open notepad" in data_btn:
        subprocess.Popen("notepad.exe")
        speak("Opening Notepad.")
        return "Opening Notepad."

    # Open Camera app
    elif "open camera" in data_btn:
        subprocess.run("start microsoft.windows.camera:", shell=True)
        speak("Opening Camera.")
        return "Opening Camera."

    # Perform Google search
    elif "search" in data_btn:
        search_query = data_btn.replace("search", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_query}")
        return f"Searched: {search_query}"

    # Provide motivational quotes
    elif "motivate me" in data_btn or "motivation" in data_btn:
        quotes = [
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            "Success doesn’t just find you. You have to go out and get it.",
            "Dream it. Wish it. Do it.",
            "Stay focused and never give up."
        ]
        quote = random.choice(quotes)
        speak(quote)
        return quote

    # Return the user's IP address
    elif "ip address" in data_btn:
        ip = socket.gethostbyname(socket.gethostname())
        speak(f"Your IP address is {ip}")
        return f"Your IP address is {ip}"

    # Read clipboard content
    elif "clipboard" in data_btn or "read clipboard" in data_btn:
        try:
            data = pyperclip.paste()
            speak(f"You copied: {data}")
            return f"Clipboard: {data}"
        except:
            speak("Clipboard is empty or not accessible.")
            return "Clipboard empty or not accessible."

    # Open File Explorer
    elif "file explorer" in data_btn or "open explorer" in data_btn:
        subprocess.run("explorer")
        speak("File Explorer opened.")
        return "File Explorer opened."

    # Flip a coin
    elif "flip a coin" in data_btn:
        result = random.choice(["Heads", "Tails"])
        speak(f"It's {result}")
        return f"It's {result}"

    # Roll a dice
    elif "roll a dice" in data_btn:
        result = random.randint(1, 6)
        speak(f"You rolled a {result}")
        return f"You rolled a {result}"

    # Open Google in the browser
    elif "open google" in data_btn:
        webbrowser.open("https://google.com/")
        speak("Google opened.")  
        return "Google opened."

    # Open YouTube in the browser
    elif "open youtube" in data_btn:
        webbrowser.open("https://youtube.com/")
        speak("YouTube opened.") 
        return "YouTube opened."

    # Fetch weather information
    elif "tell me weather" in data_btn:
        speak(f"please tell me the name of city")
        city = Speech_to_Text.Speech_to_Text().strip().lower()
        ans = weather.Weather(city)

        speak(ans) 
        return ans


# Translate a text to a different language
    elif "translate the text" in data_btn:
        try:
            speak("Please tell me the text to translate.")  
            text = Speech_to_Text.Speech_to_Text().strip()

            speak("Please tell me the language to translate this text into.")  
            language_input = Speech_to_Text.Speech_to_Text().strip().lower()

            # Expanded language mapping
            language_codes = {
                "english": "en",
                "urdu": "ur",
                "spanish": "es",
                "french": "fr",
                "german": "de",
                "italian": "it",
                "portuguese": "pt",
                "hindi": "hi",
                "korean": "ko",
                "japanese": "ja",
                "russian": "ru",
                "turkish": "tr",
                "arabic": "ar",
                "bengali": "bn",
                "persian": "fa"
            }

            if language_input in language_codes:
                target_language = language_codes[language_input]
                translated = GoogleTranslator(source='auto', target=target_language).translate(text)
                
                # Only speak if the target language is English (or add more support if needed)
                if target_language == "en":
                    speak(f"Translated text in {language_input}: {translated}")
                else:
                    speak(f"Translation complete. The translated text in {language_input} is displayed.")
                
                return f"Translated: {translated}"
            else:
                speak("Sorry, I can't translate to that language.")
                return "Sorry, I can't translate to that language."
        except Exception as e:
            speak("Sorry, I couldn't translate.")
            return f"Translation failed. Error: {str(e)}"

    # Convert currency
    elif "convert currency" in data_btn:
        try:
            speak("Please tell me the amount.")
            amount_text = Speech_to_Text.Speech_to_Text()
            amount = float(amount_text)

            speak("From which currency?")
            from_currency = Speech_to_Text.Speech_to_Text().strip().upper()

            speak("To which currency?")
            to_currency = Speech_to_Text.Speech_to_Text().strip().upper()

            API_KEY = "d03fbacbaccd6034ec2bec90"  
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and to_currency in data["conversion_rates"]:
                rate = data["conversion_rates"][to_currency]
                result = amount * rate
                speak(f"{amount} {from_currency} is {result:.2f} {to_currency}")
                return f"{amount} {from_currency} = {result:.2f} {to_currency}"
            else:
                speak("Conversion failed. Please check the currency codes and try again.")
                return "Conversion failed."

        except Exception as e:
            speak("Sorry, I couldn't convert the currency. Please try again.")
            return f"Error: {str(e)}"

    # Get the latest news headlines
    elif "news" in data_btn or "headlines" in data_btn:
        try:
            top_headlines = newsapi.get_top_headlines(language='en', country='us', page_size=3)
            news_list = [article['title'] for article in top_headlines['articles']]
            news_output = "Here are the top headlines:\n" + "\n".join(news_list)
            speak(news_output)
            return news_output
        except:
            speak("Unable to fetch news right now.")
            return "Unable to fetch news."

    # Adjust system brightness
    elif "adjust brightness" in data_btn:
        try:
            words = data_btn.split()
            if "to" in words:
                level_index = words.index("to") + 1
                level = int(words[level_index])
                if 0 <= level <= 100:
                    sbc.set_brightness(level)
                    speak(f"Brightness set to {level}.")
                    return f"Brightness set to {level}."
                else:
                    speak("Please provide a brightness level between 0 and 100.")
                    return "Brightness level must be between 0 and 100."
            else:
                speak("Please specify the brightness level, like 'adjust brightness to 50'.")
                return "Brightness level not specified."

        except Exception as e:
            speak(f"Sorry, I couldn't adjust the brightness. Error: {str(e)}")
            return f"Error: {str(e)}"

    # Adjust system volume
    elif "adjust volume" in data_btn:
        try:
            words = data_btn.split()
            if "to" in words:
                level_index = words.index("to") + 1
                level = int(words[level_index])
                if 0 <= level <= 100:
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
                    volume.SetMasterVolumeLevelScalar(level / 100.0, None)
                    speak(f"Volume set to {level} percent.")
                    return f"Volume set to {level} percent."
                else:
                    speak("Please provide a volume level between 0 and 100.")
                    return "Volume level must be between 0 and 100."
            else:
                speak("Please specify the volume level, like 'adjust volume to 40'.")
                return "Volume level not specified."

        except Exception as e:
            speak(f"Sorry, I couldn't adjust the volume. Error: {str(e)}")
            return f"Error: {str(e)}"
        

    elif "add event to calendar" in data_btn:
        try:
            speak("What is the event title?")
            title = Speech_to_Text.Speech_to_Text().strip()

            speak("Please tell me the year.")
            year = int(Speech_to_Text.Speech_to_Text().strip())

            speak("Now tell me the month by name, like January or February.")
            month_name = Speech_to_Text.Speech_to_Text().strip().lower()

            speak("Now the day.")
            day = int(Speech_to_Text.Speech_to_Text().strip())

            speak("Now the hour.")
            hour = int(Speech_to_Text.Speech_to_Text().strip())

            speak("Now the minute.")
            minute = int(Speech_to_Text.Speech_to_Text().strip())

            import calendar
            month = list(calendar.month_name).index(month_name.capitalize())
            if month == 0:
                raise ValueError("Invalid month name")

            # Format start time
            start_time_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"

            result = create_event(title, start_time_str)

            speak("Event has been added to your Google Calendar.")
            return result

        except Exception as e:
            speak("Failed to create the event.")
            return f"Error: {str(e)}"


        except Exception as e:
            speak("Failed to create the event.")
            return f"Error: {str(e)}"


    # Lock the system
    elif "lock system" in data_btn:
        ctypes.windll.user32.LockWorkStation()
        speak("System locked.")
        return "System locked."

    # Shutdown the system
    elif "shutdown system" in data_btn:
        speak("Shutting down the system.")
        subprocess.run(["shutdown", "/s", "/f", "/t", "0"])
        return "System shutting down."

    # Restart the system
    elif "restart system" in data_btn:
        speak("Restarting the system.")
        subprocess.run(["shutdown", "/r", "/f", "/t", "0"])
        return "System restarting."

    # Take a screenshot
    elif "take screenshot" in data_btn:
        screenshot = pyautogui.screenshot()
        screenshot.save(r"D:\University\Projects\ChatBot\Images\Screenshot.png")
        speak("Screenshot saved.")
        return "Screenshot saved."

    # Show system information (CPU, RAM, OS)
    elif "show system info" in data_btn:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        os_info = platform.system()
        sys_info = f"CPU Usage: {cpu}%\nRAM Usage: {ram}%\nOS: {os_info}"
        speak(sys_info)
        return sys_info

    # Get battery percentage
    elif "battery percentage" in data_btn:
        battery = psutil.sensors_battery()
        battery_percent = battery.percent
        speak(f"Battery percentage: {battery_percent}%")
        return f"Battery percentage: {battery_percent}%"

    # Open a website based on user input
    elif "open website" in data_btn:
        speak("Which website would you like to open?")
        website = Speech_to_Text.Speech_to_Text().strip().lower()
        
        if not website.endswith('.com'):
            website += '.com'
            
        url = f"https://{website}"
        webbrowser.open(url)
        speak(f"Opening {website}.")
        return f"Opening {website}."
    
    # Plays a song on youtube based on user command
    elif "play song" in data_btn:
        try:
            speak("Which song would you like me to play?")
            song = Speech_to_Text.Speech_to_Text().strip()
            import pywhatkit
            pywhatkit.playonyt(song + " song")  
            speak(f"Playing the song {song} on YouTube.")
            return f"Playing song: {song}"
        except Exception as e:
            speak("Sorry, I couldn't play the song.")
            return f"Error: {str(e)}"
        
    # Plays a song on youtube based on user command
    elif "play video" in data_btn:
        try:
            speak("What video do you want me to play?")
            video = Speech_to_Text.Speech_to_Text().strip()
            import pywhatkit
            pywhatkit.playonyt(video)
            speak(f"Playing the video {video} on YouTube.")
            return f"Playing video: {video}"
        except Exception as e:
            speak("Sorry, I couldn't play the video.")
            return f"Error: {str(e)}"
    
    # Provide meaning of different words
    elif "dictionary" in data_btn:
        try:
            speak("Which word do you want the meaning of?")
            word = Speech_to_Text.Speech_to_Text().strip().lower()
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                speak(f"{word} means: {definition}")
                return f"{word} means: {definition}"
            else:
                speak("Sorry, I couldn't find the meaning.")
                return "Meaning not found."

        except Exception as e:
            speak("There was an error finding the meaning.")
            return f"Error: {str(e)}"
    
    elif "change wallpaper" in data_btn or "set wallpaper" in data_btn:
        return change_wallpaper()

    # Handle unrecognized commands
    else:
        speak("Sorry, I didn’t understand that.")
        return "Sorry, I didn’t understand that."
