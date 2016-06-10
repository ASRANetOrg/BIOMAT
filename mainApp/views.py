# -*- coding: UTF-8 -*-

from django.shortcuts import render
from mainApp.models import InfoPage, Item


def index(request):

    story_list = Item.objects.filter(page__name="index").order_by('order')

    return render(request, 'index.html', {"story_list": story_list, "title": "Home"})


def venue(request):
    story_list = Item.objects.filter(page__name="venue").order_by('order')
    return render(request, 'venue.html', {"story_list": story_list, "title": "Venue"})


def author_instructions(request):
    story_list = Item.objects.filter(page__name="authorInstructions").order_by('order')
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": story_list,
                                                               "title": "Author Instructions"}, )


def accomodation(request):
    return render(request, 'accomodation.html')


def contactus(request):
    return render(request, 'contactUs.html')


def otherconferences(request):
    return render(request, 'otherconferences.html')


def travel(request):
    story_list = Item.objects.filter(page__name="travel").order_by('order')
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": story_list, "title": "Travel"})


def cookies(request):
    return render(request, 'cookies.html')


def robots(request):
    return render(request, 'robots.txt')
