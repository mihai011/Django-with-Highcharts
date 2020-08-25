# Django-with-Highcharts
A Django project that uses it's own default Django auth package and Highcharts for some data visualizations.

### Instructions for running the server

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 
python manage.py runserver
```


### Structure

```
/assessments/assesments: project directory
/assessments/graphs: app directory
/assessments/templates: some basic templates for project
/assessments/graphs/data: directory for csv files
```

### Internal workings


The main goal of the project is the visualization of the data collected from the internet, stored in csv files, using the defined models and the HighCharts package.

The process through which the data is shown to the user is the following:

1. The data is stored in csv format and models are defined accordingly for each file, since a model defines a different type of data.
2. Once the user is logged in the database is populated using the check_create_objects function. Here I exploited the fact that Django register the fields in the database in the order that they are defined in the model class. So i defined the rows of the model class in the exact order as they are defined in the csv files.
Like this we can populate the database without writing an explicit mapping between the columns of the csv files and the fields of the model class.
3.  After the database is populated, the data that can be shown to the user is being constructed by the model class and put in a list that will be sent to the frontend.
I have chosen to do this because i wanted to encapsulate functionality specifically for each class: each class should decide what data should calculate and what to send to the user.This is the role of the class method "create_data" from each model. For now the class will return only simple things, but in this method can be constructed much more complicated statistics, if they are desired.
4. The list of data is sent to the template where a table is defined and the specifical chart is created automatically with some random parameters added.


Things to improve:
1. Better looking templates, table to be done automatically with the help of the template engine.
2. Error handling.
3. Better logging.
4. Better highcharts.

