from fastapi import FastAPI
import pandas as pd
import consultas
import Carga

app = FastAPI()


@app.get("/Pregunta 1")
def Año_con_mas_carreras():
    return consultas.Anio_con_mas_carreras()

@app.get("/Pregunta 2")
def Piloto_con_mayor_cantidad_de_primeros_puestos():
    return consultas.Piloto_con_mayor_cantidad_de_primeros_puestos()

@app.get("/Pregunta 3")
def Nombre_del_circuito_mas_corrido():
    return consultas.Nombre_del_circuito_mas_corrido()

@app.get("/Pregunta 4")
def Piloto_con_mas_ptos_con_contructor_de_nacionalidad_American_o_British():
    return consultas.Piloto_con_mas_ptos_con_contructor_de_nacionalidad_American_o_British()




