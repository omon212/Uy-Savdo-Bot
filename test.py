from googletrans import Translator

translator = Translator()


def translate_text(text, src='uz', dest='ru'):
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text


text_uz = "olmazor"
text_ru = translate_text(text_uz, src='uz', dest='ru')
print(text_ru)
