# coding=gb2312
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
# Create your views here.

from jhs.models import Insure


def get_insure_by_code(request, code=''):
    try:
        insures = Insure.objects.get(code=code)
    except Insure.DoesNotExist:
        raise Http404
    return insures


