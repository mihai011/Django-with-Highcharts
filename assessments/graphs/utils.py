
import pandas as pd
import graphs.models as models
import csv
import os

def check_int_float(s):

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
    if s in ['','.']:
        return 0
    return s

def check_create_models(data_dir):
    
    classes = [cls for _, cls in models.__dict__.items() if isinstance(cls, type)]

    for c in classes:
        
        fields = c._meta.get_fields()[1:]

        df = csv.reader(open(os.path.join(data_dir, c.source()), 'r' ))
        next(df, None)
        
        for row in df:
            f_dict = {}
            for i in range(len(fields)):
                f_dict[fields[i].column] =  check_int_float(row[i])

            print(f_dict)
            obj = c(**f_dict)
            obj.save()
        

            
