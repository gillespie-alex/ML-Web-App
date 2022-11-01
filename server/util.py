import json
import pickle
import numpy as np

# Global Variables
__workclass = None
__education = None
__marital_status = None
__data_columns = None
__model = None


def get_income(age, workclass, education, marital_status):
    workclass_index = __data_columns.index(workclass.lower())
    education_index = __data_columns.index(education.lower())
    marital_status_index = __data_columns.index(marital_status.lower())
    
    print(f'these are the vals {workclass_index}, {education_index}, {marital_status_index}')
    
    x = np.zeros(len(__data_columns))
    x[0] = age
    x[workclass_index] = 1
    x[education_index] = 1
    x[marital_status_index] = 1
    print("\n MADE IT TO THE PREDICTION PART \n")
    ans = __model.predict([x])[0] 
    print(f'answer is : {ans} \n')
    return int(ans)

# Each of these functions want to read from the columns.json file
def get_workclass_names():
    return __workclass
def get_education_names():
    return __education
def get_marital_status_names():
    return __marital_status

# This method will load the saved artifacts like the columns.json and the .picle object
def load_saved_artifacts():
    print('loading saved artifacts...start')

    global __data_columns
    global __workclass
    global __education
    global __marital_status

    global __model

    with open('./artifacts/columns.json', 'r') as f:
        # Whatever object is loaded will be converted into a dictionary
        __data_columns = json.load(f)['data_columns']
        __workclass = __data_columns[1:4]
        __education = __data_columns[4:9]
        __marital_status = __data_columns[9:]
    with open('./artifacts/income_predictor.pickle', 'rb') as f:
        __model =pickle.load(f)
    print('loading artifacts is now completed')
    pass

if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_income(50, 'workclass_Self Employed', 'education_Doctorate', 'marital-status_Single'))
    #print(get_income(60, 'workclass_unemployed', 'education_Doctorate', 'marital-status_widowed'))
    #print(get_income(30, 'workclass_Self Employed', 'education_other', 'marital-status_married'))

    a1 = get_income(50, 'workclass_Self Employed', 'education_Doctorate', 'marital-status_Single')
    a2 = get_income(60, 'workclass_unemployed', 'education_Doctorate', 'marital-status_widowed')
    a3 = get_income(30, 'workclass_Self Employed', 'education_other', 'marital-status_married')
    print('\nThe predictions are \n')
    print(a1, a2, a3)
