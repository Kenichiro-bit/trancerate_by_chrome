import text_to_list
import translate_on_chrome

english_text = text_to_list.text_list
translate_text = translate_on_chrome.translate_result_list
translate_class = translate_on_chrome.translate_on_ChromeWeb()

for i in range(len(english_text)):
    if len(english_text[i]) < 100:
        pass
    elif len(english_text[i]) > 300:
        pass
    else:
        translate_class.search_on_chrome(english_text[i])


translate_class.close_chrome_file()
print(translate_text)