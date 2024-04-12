from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    full_text = request.GET['full_text']
    word_list = full_text.split()
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] +=1
        else:
            # add to dictionary
            word_dictionary[word]= 1
    sorted_words =  sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'full_text':full_text , 'count':len(word_list), 'word_dictionary':sorted_words })
def about(request):
    return render(request,'about.html')