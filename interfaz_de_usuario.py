#interfaz_de_usuario.py
import matplotlib.pyplot as plt

def obtener_evidencia():
    evidencia = {}
    while True:
        lluvia = input("¿Está lloviendo? (si/no): ").strip().lower()
        if lluvia in ['si', 'no']:
            evidencia['Lluvia'] = 1 if lluvia == 'si' else 0
            break
        else:
            print("Por favor, responde con 'si' o 'no'.")

    while True:
        accidente = input("¿Hay un accidente? (si/no): ").strip().lower()
        if accidente in ['si', 'no']:
            evidencia['Accidente'] = 1 if accidente == 'si' else 0
            break
        else:
            print("Por favor, responde con 'si' o 'no'.")
    
    return evidencia

def mostrar_resultados(resultados, probabilidades):
    print("\nResultados de la inferencia:")
    for variable, valor in resultados.items():
        probabilidad = probabilidades[variable]
        print(f"{variable}: {'sí' if valor == 1 else 'no'} (Probabilidad: {probabilidad:.2f})")

    graficar_probabilidades(resultados, probabilidades)

def graficar_probabilidades(resultados, probabilidades):
    variables = list(probabilidades.keys())
    valores = list(probabilidades.values())
    respuestas = ['sí' if resultados[var] == 1 else 'no' for var in variables]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(variables, valores, color='skyblue')
    plt.xlabel('Variables')
    plt.ylabel('Probabilidades')
    plt.title('Probabilidades de las Variables')
    plt.ylim(0, 1)

    for bar, probabilidad, respuesta in zip(bars, valores, respuestas):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{respuesta} ({probabilidad:.2f})', ha='center', va='bottom')

    plt.show()
