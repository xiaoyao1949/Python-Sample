import re
str4 = r'imooc:c c++ java python ,php JavaScript'
words = re.split(r':| |,', str4)
print(words)
