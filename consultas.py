import numpy as np
import pandas as pd
import json


# Año con mas carreras
def Anio_con_mas_carreras():
    races = pd.read_csv('Datasets/races.csv')

    año = races.value_counts('year').idxmax()
    cant = races.value_counts('year').max()

    return {'Año con mas carreras fue':int(año), 'cantidad':int(cant)}

# Piloto con mayor cantidad de primeros puestos
def Piloto_con_mayor_cantidad_de_primeros_puestos():
    results = pd.read_json("./Datasets/results.json")
    drivers = pd.read_csv('Datasets\drivers.csv', delimiter= ';')

    # Filtro solo los de primeros puestos
    puesto1 = results[results['positionOrder'] == 1]

    # Union de dataframes
    driv_1 = pd.merge(drivers, puesto1, on='driverId', how='outer')

    cant =driv_1.value_counts("driverRef").max()
    nombre = driv_1.value_counts("driverRef").idxmax()

    return {'Piloto con mayor cantidad de primeros puestos': str(nombre), 'Cantidad de 1°': int(cant)}

# Nombre del circuito mas corrido
def Nombre_del_circuito_mas_corrido():
    circuits = pd.read_csv('Datasets\circuits_cambiado.csv', delimiter= ';')
    races = pd.read_csv('Datasets/races.csv')

    # Union de dataframes
    circu_carre = pd.merge(circuits, races, on='circuitId', how='outer')

    # Quito columnas
    circu_carre = circu_carre.drop(['lat','lng','alt','url_x','url_y','name_y','date','time','circuitRef','location','country'],axis= 1)
    
    circuito = circu_carre.value_counts('name_x').idxmax()
    cant = circu_carre.value_counts('circuitId').max()

    return {'Circuito con mas carreras':str(circuito) , 'total de carreras': int(cant)}

# Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
def Piloto_con_mas_ptos_con_contructor_de_nacionalidad_American_o_British():
    constr = pd.read_json("./Datasets\constructors.json")
    results = pd.read_json("./Datasets/results.json")
    drivers = pd.read_csv('Datasets\drivers.csv', delimiter= ';')

    # Quito columnas
    results= results.drop(['number', 'grid','position','positionText','positionOrder','laps','time','milliseconds','fastestLap','rank','fastestLapTime','fastestLapSpeed','statusId'], axis=1)
    constr = constr.drop(['constructorRef','url'], axis=1)

    # Union dataframes
    const_result = pd.merge(constr, results, on= 'constructorId', how= 'outer')
    final= pd.merge(const_result, drivers, on= 'driverId', how= 'outer')

    final = final.drop(['dob', 'number', 'code','url', 'nationality_y'], axis=1)

    filtro_final = final[(final['nationality_x'] == 'British') | (final['nationality_x'] == 'American')]

    driv_pts = filtro_final.groupby("driverId")[["points"]].sum()
    driv_ptos = driv_pts.sort_values('points', ascending=False)

    ptos = int(driv_ptos.max())
    nombreId = int(driv_ptos.idxmax())
    
    # Cual es la nacionalidad de piloto con mas ptos
    nom = drivers[drivers['driverId']== nombreId]


    return {'Piloto con mas puntos en total': nom.iloc[0,4]+' '+ nom.iloc[0,5], 'Total de puntos':ptos, 'Nacionalidad': nom.iloc[0,7]}
