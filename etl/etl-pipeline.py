import pandas as pd
#import psycopg2
import numpy as np


translDictCapShape = {'b': 'bell', 'c': 'conical', 'x': 'convex','f': 'flat', 'k': 'knobbed', 's': 'sunken'}
columnDict = {'cap_shape': translDictCapShape}

def dataEngineVT(x, dict):
    print(x)
    return dict.get(str(x))

#####################################################################################33
# Load the dataset in a Pandas dataframe - Pandas offers easier data manipulation
#######################################################################################

mushroomsPDF = pd.read_csv("c:\\Users\evo\mushrooms.csv")

# get a sample of the loaded data frame, including the column names
print(mushroomsPDF.head(5))

####################################################################
# Rename dataframe columns (facilitates intuitive SQL statements later on)
####################################################################
mushroomsPDF.rename(columns={'1': 'cap_shape', '3': 'cap_color', '5': 'odor', '8': 'gill_size', '9': 'gill_color', '14': 'stalk_color_above_ring',
                             '17': 'veil_color', '19': 'ring_type','20': 'spore_print_color', '21': 'population', '22': 'habitat'}, inplace=True)

#validate the rename operation during debugging
pd.set_option('display.max_columns', None)
print(mushroomsPDF.head(5))

#################################################
# Validate and Transform Dataframe Data (in a single operation)
#################################################

for colName in mushroomsPDF.columns:
    print(colName)

    # validates and translates only one column so far, on purpose
    if colName == 'cap_shape':
        mushroomsPDF[colName] = mushroomsPDF[colName].apply(dataEngineVT, dict=columnDict.get(colName))




print(mushroomsPDF.head(5))

#################################################
# Bulk Insert in e.g. PostgressSQL DB
#################################################