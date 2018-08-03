
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

from django.http import JsonResponse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

class HomePageView(TemplateView):
    template_name = "index.html"







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

