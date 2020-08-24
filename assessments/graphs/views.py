
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render, redirect
import pandas as pd

import os 
import pathlib


from graphs.utils import check_create_objects
import graphs.models as models
# Create your views here.

def login(request):

    return redirect("/login")


@login_required
def logged_in(request):

    abs_path = pathlib.Path(__file__).parent.absolute()
    data_dir = os.path.join(abs_path,"data")
    classes = [cls for _, cls in models.__dict__.items() if isinstance(cls, type)]

    check_create_objects(data_dir, classes)

    
    # graphs = []
    # for f in os.listdir(data_dir):

    #     graph = {}
        
    #     file_path = os.path.join(data_dir,f)

    #     df = pd.read_csv(file_path)
    #     rs = df.groupby(df.columns[0])[df.columns[2]].agg("sum")
    #     graph["categories"] = list(rs.index)
    #     graph["values"] = list(rs.values)
    #     graph["name_y"] = df.columns[1]
    #     graph["series_name"] = df.columns[0]
    #     graph["name"] = f

    #     graphs.append(graph) 

    graphs = []

    for c in classes:
        
        graph = {}

        categories, values, name_y, series_name = c.create_data()

        graph["categories"] = categories
        graph["values"] = values
        graph["name_y"] = name_y
        graph["series_name"] = series_name
        graph["name"] = c.source()

        graphs.append(graph)

        c.objects.all().delete()

    context = {"graphs":graphs}
    return render(request, 'index.html', context=context)
