import pandas as pd

mushroomsPDF = pd.read_csv("c:\\Users\evo\mushrooms.csv")

# get a sample of the loaded data frame, including the column names
print(mushroomsPDF.head(5))

#rename columns (facilitates intuitive SQL statements)
mushroomsPDF.rename(columns={'1': 'cap_shape', '3': 'cap_color', '5': 'odor', '8': 'gill_size', '9': 'gill_color', '14': 'stalk_color_above_ring',
                             '17': 'veil_color', '19': 'ring_type','20': 'spore_print_color', '21': 'population', '22': 'habitat'}, inplace=True)

pd.set_option('display.max_columns', None)
print(mushroomsPDF.head(5))