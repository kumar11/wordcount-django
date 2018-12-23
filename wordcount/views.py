from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return HttpResponse("Hello world i am learning")

def homepage(request):
	return render(request,"home.html")

def count(request):
	fulltext = request.GET['fulltext']
	 #print (fulltext)

	#split the text on space
	wordlist = fulltext.split(' ')
	#print (wordlist)

	worddic = {}
	for word in wordlist:
		if word in worddic:
			worddic[word] += 1
		else:
			worddic[word] = 1

	wordsorted = {}
	wordsorted = sorted(worddic.items(),key = operator.itemgetter(1),reverse = True)

	#print (worddic)
	return render(request,"count.html",{'fulltext':fulltext,'count':len(wordlist),'worddic':wordsorted})

def about(request):
	return render(request,"about.html")
