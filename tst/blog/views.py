from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404


def index(request):
	return render(request, 'index.html', {})