#main.py
from base_de_conocimiento import construir_red
from motor_de_inferencia import inferir_probabilidades
from interfaz_de_usuario import obtener_evidencia, mostrar_resultados

def main():
    red = construir_red()
    evidencia = obtener_evidencia()
    resultados, probabilidades = inferir_probabilidades(red, evidencia)
    mostrar_resultados(resultados, probabilidades)

if __name__ == "__main__":
    main()
