import requests as rq
from bs4 import BeautifulSoup

thai = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด'
        'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส'
        'ห', 'ฬ', 'อ', 'ฮ'
        ]

def detect_word(word, lastword=None, arr_output=None):
    status_output = []
    remove_word = ''
    new_word = ''
    count_new_word = 0 
    if word != '':
        if arr_output == None:
            arr_output = []
        if lastword != None:
            count_lastword = len(lastword)
            for number in range(len(word)) :
                if number >= count_lastword :
                    new_word = new_word + word[number]
                    count_new_word = count_new_word + 1
            word = new_word
        arr_word = []
        text_word = ''
        if len(word) > 0:
            for string in word:
                text_word = str(text_word) + str(string)
                arr_word.append(text_word)
                send_data = {
                    'word': text_word,
                    'funcName': 'lookupWord',
                    'status': 'lookup'
                }
                response = rq.post(
                    'https://dictionary.orst.go.th/func_lookup.php', data=send_data, verify=True)
                if (response.status_code == 200 and 'content-type' in response.headers):
                    soup = BeautifulSoup(response.text, "lxml")
                    output = soup.find("div", {'class': 'panel-body'})
                    if output.text[:57] != 'ไม่พบคำศัพท์ที่ต้องการค้นหา ท่านต้องการเสนอคำศัพท์หรือไม่':
                        if text_word not in thai :
                            arr_output.append(str(text_word))
                            remove_word = text_word
                            status_output.append(True)
                    else:
                        status_output.append(False)
            if True in status_output:
                return detect_word(word, remove_word, arr_output)
        else:
            for num in range(len(arr_output)) :
                if num + 1 < len(arr_output) :
                    if arr_output[num] in arr_output[num + 1] :
                        arr_output.remove(arr_output[num])
            return arr_output

