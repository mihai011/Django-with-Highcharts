
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.

@login_required
def logged_in(request):

    df = pd.read_csv("/home/mihai/Desktop/Repos/Django-with-Highcharts/assessments/graphs/data/cars.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")

    context = {"categories": categories, 'values': values, 'table_data':table_content}
    return render(request, 'index.html', context=context)
