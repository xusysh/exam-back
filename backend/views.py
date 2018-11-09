# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from backend.models import UserList
import json
import os

def notfound(request):
  status = {'code': 404, 'info': 'not found' }
  return HttpResponse(json.dumps(status), content_type="application/json")
