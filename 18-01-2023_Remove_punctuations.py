def removePunctuation(my_str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct=""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

my_str = "Hello!!!, he said ---and went."
print(removePunctuation(my_str))
