
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render, redirect
import pandas as pd

import os 
import pathlib


from graphs.utils import check_create_objects
import graphs.models as models

import logging
logger_info = logging.getLogger("app_info")
logger_debug = logging.getLogger("app_debug")
# Create your views here.

"""
Main Function after logging in
"""
@login_required
def logged_in(request):

    logger_debug.debug("User Logged in")

    abs_path = pathlib.Path(__file__).parent.absolute()
    data_dir = os.path.join(abs_path,"data")
    classes = [cls for _, cls in models.__dict__.items() if isinstance(cls, type)]

    check_create_objects(data_dir, classes)

    graphs = []

    for c in classes:
        
        graph = {}

        categories, values, series_name, name_y = c.create_data()

        graph["categories"] = categories
        graph["values"] = values
        graph["name_y"] = name_y
        graph["series_name"] = series_name
        graph["name"] = c.source()

        graphs.append(graph)

        c.objects.all().delete()

    logger_debug.debug("Database cleaned up!")

    context = {"graphs":graphs}
    logger_debug.debug("Data sent to front-end!")
    return render(request, 'index.html', context=context)
