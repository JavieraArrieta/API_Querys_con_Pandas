def Datasets():
    import pandas as pd
    import json
    races = pd.read_csv('Datasets/races.csv')
    circuits = pd.read_csv('Datasets\circuits_cambiado.csv', delimiter= ';')
    drivers = pd.read_csv('Datasets\drivers.csv', delimiter= ';')
    constr = pd.read_json("./Datasets\constructors.json")
    results = pd.read_json("./Datasets/results.json")