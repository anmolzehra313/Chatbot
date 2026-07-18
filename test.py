from googletrans import Translator

translator = Translator()
result = translator.translate("Hello, how are you?", dest='ur')
print(result.text)
