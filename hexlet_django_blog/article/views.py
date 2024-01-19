from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class ArticleView(View):
    def get(self, request, *a, **kw):
        return render(request, 'articles/index.html', context={'name': 'article'})
