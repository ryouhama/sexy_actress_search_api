from django.shortcuts import render
from django.http import HttpResponse
from .search import SearchActress


def get_sexy_actress(request):
    searcher = SearchActress()
    search_result = searcher.search_actress()
    return HttpResponse(search_result)
