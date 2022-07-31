import pandas as pd
dataset = pd.read_csv('db.csv', sep=';')

pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 50)


print(dataset)

print(dataset.dtypes)
'''[258 rows x 7 columns]
Nombre          object
Motor           object
Año              int64
Kilometraje    float64
Cero_km           bool
Accesorios      object
Valor          float64
dtype: object 
'''