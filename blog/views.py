import json

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    posts = [
        {
            "id": 1,
            "title": "blog post 1",
            "description": "blog post reference",
            "content": "blog post content"
        },
        {
            "id": 2,
            "title": "blog post 2",
            "description": "blog post reference",
            "content": "blog post content"
        },
        {
            "id": 3,
            "title": "blog post 3",
            "description": "blog post reference",
            "content": "blog post content"
        },
        {
            "id": 4,
            "title": "blog post 4",
            "description": "blog post reference",
            "content": "blog post content"
        }
    ]

    return HttpResponse(json.dumps(posts))


def welcome(request):
    return HttpResponse("welcome to the blog")
