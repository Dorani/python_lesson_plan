from translate import Translator

#set the translater with a specific language
translator = Translator(to_lang='ja')

try:
    with open('text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        #put it in a new file
        with open('japanese.txt', mode='w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print('check your file path')