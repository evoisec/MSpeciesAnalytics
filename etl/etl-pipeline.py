import sys
#import swifter
import pandas as pd
#import psycopg2
import numpy as np
from sqlalchemy import create_engine

#Note: the ref data dictionories can be initialized/loaded from file/db for increased config flexibility
translDictCapShape = {'b': 'bell', 'c': 'conical', 'x': 'convex','f': 'flat', 'k': 'knobbed', 's': 'sunken'}
translDictCapColor = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
translDictOdor = {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty', 'n': 'none', 'p': 'pungent', 's': 'spicy'}
translDictGillSize = {'b': 'broad', 'n': 'narrow'}
translDictGillColor = {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray', 'r': 'green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red',
                       'w': 'white', 'y': 'yellow'}
translDictstalkColorAboveRing = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
translDictVeilColor = {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'}
translDictRingType = {'c': 'cobwebby', 'e': 'evanescent', 'f': 'flaring', 'l': 'large', 'n': 'none', 'p': 'pendant', 's': 'sheathing', 'z': 'zone'}
translDictSporePrintColor = {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green', 'o': 'orange', 'u': 'purple', 'w': 'white', 'y': 'yellow'}
translDictPopulation = {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered', 'v': 'several', 'y': 'solitary'}
translDictHabitat = {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}


columnDict = {'cap_shape': translDictCapShape}
columnDict['cap_color'] = translDictCapColor
columnDict['odor'] = translDictOdor
columnDict['gill_size'] = translDictGillSize
columnDict['gill_color'] = translDictGillColor
columnDict['stalk_color_above_ring'] = translDictstalkColorAboveRing
columnDict['veil_color'] = translDictVeilColor
columnDict['ring_type'] = translDictRingType
columnDict['spore_print_color'] = translDictSporePrintColor
columnDict['population'] = translDictPopulation
columnDict['habitat'] = translDictHabitat


# Pluggable (in any ETL workflow step) Data Engine for Validates and Translates of Data according to specific algo
def dataEngineVT(x, dict):
    #print(x)
    #note: the data validation occurs by  default due to the use of dictionaries which return None of the key doesnt exist
    # i.e. if the data is not valid
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

# Validate abd Convert All Categorical Columns

for colName in mushroomsPDF.columns:
    print(colName)

    # validates and translates only one column so far, on purpose
    if colName != 'lat' and colName != 'lon' and colName != 'Time':
        #with Swifter, this ETL step runs on multiple cores in parallel
        mushroomsPDF[colName] = mushroomsPDF[colName].swifter.apply(dataEngineVT, dict=columnDict.get(colName))

# Convert the Python None to the Pandas NaN
mushroomsPDF = mushroomsPDF.fillna(value=np.nan)

# Validate and convert the Time column. Converts invalid data to NaT
mushroomsPDF['Time'] = pd.to_datetime(mushroomsPDF['Time'], format='%I:%M:%S %p', errors='coerce').dt.time

# Validate and convert the lon and lat columns. Converts invalid data to NaN
mushroomsPDF['lat'] = pd.to_numeric(mushroomsPDF['lat'],errors='coerce')
mushroomsPDF['lon'] = pd.to_numeric(mushroomsPDF['lon'],errors='coerce')

#print(mushroomsPDF[mushroomsPDF.Time.isnull()])
#print(mushroomsPDF.dtypes)

#################################################
# Persist the ETL pipeline output to file dataset
#################################################

# writes NaN and Nat as empty string (zero characters) in the csv file
mushroomsPDF.to_csv("c:\\Users\evo\mushrooms-processed.csv", index = True, header=True)
# writes NaN and Nat as NaN in the csv file
#mushroomsPDF.to_csv("c:\\Users\evo\mushrooms-processed.csv", index = True, header=True, na_rep='NaN')

sys.exit()

#################################################
# Bulk Insert in e.g. PostgressSQL DB. Using the Alchemy SQL frameowrk provides ORM like functionality for Pandas dataframes
#################################################

engine = create_engine('postgres+psycopg2://dbserver:mypassword@db.com:5432/mydatabase', echo=False)
mushroomsPDF.to_sql('mushrooms', con=engine)