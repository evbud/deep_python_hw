# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

data = str('Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code '
           'readability with the use of significant indentation via the off-side rule.\nPython is dynamically typed '
           'and garbage-collected. It supports multiple programming paradigms, including structured (particularly '
           'procedural), object-oriented and functional programming. It is often described as a "batteries included" '
           'language due to its comprehensive standard library.\nGuido van Rossum began working on Python in the '
           'late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. '
           'Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely '
           'backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of '
           'Python 2.\nPython consistently ranks as one of the most popular programming '
           'languages.\nPython was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & '
           'Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was '
           'inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system. '
           'Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, '
           'as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his '
           'responsibilities as Pythons "benevolent dictator for life", a title the Python community bestowed '
           'upon him to reflect his long-term commitment as the projects chief decision-maker. '
           'In January 2019, active Python core developers elected a five-member Steering Council to lead the '
           'project').lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '').split()

TOP_MENTIONED = 10
text = {}
for word in data:
    text[word] = data.count(word)
sorted_text = dict(sorted(text.items(), key=lambda item: item[1], reverse=1))
for word in range(TOP_MENTIONED):
    print(f'{list(sorted_text)[word]:<20} - упоминаний в тексте: {sorted_text.get(list(sorted_text)[word]):^4}')
