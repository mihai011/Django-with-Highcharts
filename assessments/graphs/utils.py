import csv
import os


import logging
logger = logging.getLogger('app_info')

def check_int_float(s):

    if s in ['','.']:
        return 0
    try:
        s = float(s)
        return s
    except Exception:
        pass
    try:
        s = int(s)
        return s
    except Exception:
        pass
    
    return s

"""
Function for simple database population from csv files.
"""


def check_create_objects(data_dir, classes):
    
    for c in classes:

        if c.objects.all().count() == 0:
        
            fields = c._meta.get_fields()[1:]

            df = csv.reader(open(os.path.join(data_dir, c.source()), 'r' ))
            next(df, None)
            
            for row in df:
                f_dict = {}
                for i in range(len(fields)):
                    f_dict[fields[i].column] =  check_int_float(row[i])

                obj = c(**f_dict)
                obj.save()
    logger.info("Database populated!") 

            
