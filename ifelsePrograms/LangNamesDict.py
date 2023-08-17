# a program to find the values in dict

langs = {"Java":"James Gosling", "Python":"Rossum", "C":"Dennis Ritche", "C++":"Stroustrup"}

lang = input("Enter ur Fav language: ")

if (lang in langs.keys()):
    print("{} developed by {}".format(lang, langs.get(lang)))
else:
    print("{} is Another language".format(lang))