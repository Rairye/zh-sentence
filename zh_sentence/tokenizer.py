'''
Copyright 2021 Rairye
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''

breaks = set(["。", "！", "？", "．"])
closing_punctuation = set([")", "]", "}", "）", "」", "】", "』", "｝", "〕", ">", "＞", "》", "〉", "］", "﹂", "\""])

def is_break(char):
    return char in breaks

def is_closing_punct(char):
    return char in closing_punctuation

def tokenize(paragraph):

        if type(paragraph) != str:
            return []

        if len(paragraph) == 0:
            return []
    
        last_category = ""
        sentences = []
        i = 0
        j = 0
        length = len(paragraph)

        while j < length:
                current_char = paragraph[j]
                current_category = "BREAK" if is_break(current_char) else "NOTBREAK"

                if last_category == "BREAK" and current_category == "NOTBREAK":

                        if not is_closing_punct(current_char):
                                sentences.append("".join(paragraph[i:j]).strip())
                                last_category = current_category
                                i=j
                                j+=1
                                                             
                        else:
                                last_category = "BREAK"
                                j+=1
                        
                elif current_category == "BREAK" and j < length -1:
                        j+=1
                        last_category = current_category
                        
                elif j == length -1:
                     sentences.append("".join(paragraph[i:]).strip())
                     j+=1
                     
                else:
                     j+=1
                     last_category = current_category
        
        return sentences
