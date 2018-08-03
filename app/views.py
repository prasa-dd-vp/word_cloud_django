from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.shortcuts import render_to_response
from django.http import JsonResponse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import time

def displayHomePage(request):
    return render(request,'app/index.html')

def new(request):
    if request.method == "POST":
        words = request.POST.get('words')
        wordcloud = WordCloud(relative_scaling = 1.0,
                              stopwords = {'to', 'of'} # set or space-separated string
                              ).generate(words)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.savefig(r'E:\word_cloud\app\static\app\figure.png')
        #html = '''<html><body><h2>Here is the world cloud...</h2><img src="E:\word_cloud\figure.png" alt="image not found" width="500" height="333"></body></html>'''
        #time.sleep(5)
        return render_to_response('app/second.html')








        #plt.show()
        #return JsonResponse({"success": words})
        




def test(request):
    print("sucess")
    return JsonResponse({"success": "asdfasdd"})



def word_cloud(request, words):
    if request.method == "GET":
        words.replace('_', ' ')
        wordcloud = WordCloud(relative_scaling = 1.0,
                              stopwords = {'to', 'of'} # set or space-separated string
                              ).generate(words)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.savefig('figure')
        plt.show()
        return JsonResponse({"success": words})

