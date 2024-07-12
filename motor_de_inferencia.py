#motor_de_inferencia.py
from pgmpy.inference import VariableElimination

def inferir_probabilidades(red, evidencia):
    inferencia = VariableElimination(red)
    
    variables_red = red.nodes()
    
    variables_consulta = [var for var in variables_red if var not in evidencia]
    
    resultado = inferencia.map_query(variables=variables_consulta, evidence=evidencia)
    
    probabilidades = {}
    for variable in variables_consulta:
        prob = inferencia.query(variables=[variable], evidence=evidencia).values
        probabilidades[variable] = prob[resultado[variable]]
    
    return resultado, probabilidades
