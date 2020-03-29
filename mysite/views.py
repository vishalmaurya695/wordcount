from django.http import HttpResponse
from django.shortcuts import render
import operator


def index(request):
    return HttpResponse("Hello django this is homepage")


def wordcount(request):
    # return HttpResponse("<h1 >this is new blog page </h1>")
    return render(request, 'index.html')


def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    wordlength = len(word_list)
    worddictionary = {}


    for word in word_list:
        if word in worddictionary:
            # increase value by 1
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1


    sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1), reverse = True)

    
    return render(request, 'counted.html', {'text': data, 'len': wordlength, 'worddictionary':worddictionary, 'worddictionary':sorted_list})

