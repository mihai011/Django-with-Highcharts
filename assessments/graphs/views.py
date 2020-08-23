
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

import os 
import pathlib


from graphs.utils import check_create_models

# Create your views here.


@login_required
def logged_in(request):


    abs_path = pathlib.Path(__file__).parent.absolute()
    data_dir = os.path.join(abs_path,"data")

    check_create_models(data_dir)

    graphs = []

    for f in os.listdir(data_dir):

        graph = {}
        
        file_path = os.path.join(data_dir,f)

        df = pd.read_csv(file_path)
        rs = df.groupby(df.columns[0])[df.columns[2]].agg("sum")
        graph["categories"] = list(rs.index)
        graph["values"] = list(rs.values)
        graph["name_y"] = df.columns[1]
        graph["series_name"] = df.columns[0]
        graph["name"] = f

        graphs.append(graph) 


    context = {"graphs":graphs}
    return render(request, 'index.html', context=context)
