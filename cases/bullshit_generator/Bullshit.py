'''
唬爛產生器原始作者
Bill Hsu (徐子修)
https://github.com/StillFantastic/bullshit

Python 版本作者
Darren Yang (楊德倫)
https://github.com/telunyang/python_bullshit_generator
'''

import json
import random

class Bullshit:
    def __init__(self):
        with open("./data.json", "r", encoding='utf-8') as file:
            self.dict_data = json.loads(file.read())

    def isEnd(self, word):
        if word != "" & word[-1] in "。？！?!":
            return True
        return False
    
    def generate(self,param_topic, param_min_length):
        min_length = 0
        param_min_length = int(param_min_length)

        list_famous = self.dict_data['famous']
        random.shuffle(list_famous)

        list_bullshit = self.dict_data['bullshit']
        random.shuffle(list_bullshit)

        str_gen = ""

        while min_length < param_min_length:

            int_rand = random.randint(0,99)
            # int_rand 範圍:
            # 0 - 5 且 文字資料是句號、問號等作為結尾: 建立新段落
            # 0 - 27: 使用名人語錄
            # 28 - 99: 使用唬爛語錄

            if int_rand < 5 and self.isEnd(str_gen):
                str_gen += "\n\n"

            elif int_rand < 27:
                if len(list_famous) == 0:
                    break

                sentence_famous = list_famous.pop(0)

                # 用曾說過，曾講過來取代data.json中的a
                str_before = self.dict_data['before'][random.randint(0,len(self.dict_data['before']) - 1)]

                # 這啟發了我、這不禁讓我深思，用來取代名人語錄當中的b
                str_after = self.dict_data['after'][random.randint(0,len(self.dict_data['after']) - 1)]

                sentence_famous = sentence_famous.replace("a", str_before)
                sentence_famous = sentence_famous.replace("b", str_after)

                str_gen += sentence_famous
            
            else:
                if len(list_bullshit) == 0:
                    break

                sentence_bullshit = list_bullshit.pop(0)
                sentence_bullshit = sentence_bullshit.replace("x", param_topic)

                str_gen += sentence_bullshit
            
            min_length = len(str_gen)
    
        if param_topic not in str_gen:
            return self.generate(param_topic, param_min_length)
        
        return str_gen