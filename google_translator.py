### pip install googletrans
from googletrans import Translator
sentence = input("Let's type: ")
translator = Translator()
translated = translator.translate(sentence, src="en", dest="es")
print(translated.text)