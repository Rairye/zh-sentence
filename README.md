# zh-sentence

A light-weight sentence tokenizer for Chinese languages.

## Installation

```python
pip install zh-sentence
```

## Sample

```python
from zh_sentence.tokenizer import tokenize

paragraph_str = "你好吗？你快乐吗？"

sentence_list = tokenize(paragraph_str)

for sentence in sentence_list:
	print(sentence)
```
