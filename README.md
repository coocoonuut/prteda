# Planificador de Rutas Óptimas de Grafos

Este programa forma parte de un proyecto universitario sujeto a errores y sugerencias 
posibles, enfocado en aplicar conceptos de matemáticas discretas para resolver problemas 
reales en logística y distribución automática.

Este programa forma parte de un proyecto universitario sujeto a errores y suegerencias 
posibuleses una propuesta de solución al problema de planificación ineficiente de rutas 
en empresas de distribución automática, especialmente en sectores como alimentos, bebidas y 
bienes de consumo rápido. Estas empresas a menudo enfrentan pérdidas por rutas mal diseñadas, 
lo cual genera mayores costos operativos, consumo excesivo de combustible y tiempos de entrega 
prolongados.

La herramienta, desarrollada en Python utilizando la librería `networkx`, permite al usuario ingresar:
- Una lista personalizada de puntos de entrega (vertices).
- Una Matriz de Adyacencia que representa las conexiones y costos entre dichos puntos.
- Un punto de partida y uno de destino.

Con esta información, el programa construye un grafo dirigido y ponderado y aplica el algoritmo 
de Dijkstra para calcular la ruta más corta entre los nodos seleccionados. El resultado es una 
secuencia paso a paso con el costo asociado de cada tramo, más el costo total del recorrido.

Esta solución está inspirada en los conceptos de matemáticas discretas (teoría de grafos) y 
busca demostrar cómo herramientas computacionales accesibles pueden ayudar a pequeñas y medianas 
empresas a optimizar sus rutas de distribución, mejorar la logística y reducir costos.

## Requisitos
- Python 3.9.x^ a Python 3.11
- Windows 1x^
- Git Bash 2.4x^

## Instalación
Para poder ejecutar correcamente el programa en tu computadora sigue los siguientes paso, cualquier
paso que hayas cumplido o hecho ya anteriormente salta al siguiente paso.

1. Instalar [Python](https://www.python.org/downloads/release/python-3110/).
2. Instalar [Git bash](https://git-scm.com/downloads).
3. Abre tu terminal favorito.
4. Clonar el repositorio `prteda`.
```sh
git clone https://github.com/coocoonuut/prteda.git
```
5. Cambia tu directorio actual por la ubicacion del proyecto.
```sh
cd ./prteda/
```
6. Para no contaminar tu computadora instala un Entorno Virtual.
```sh
python -m venv env
```
6. Activa tu Entorno Virtual.
```sh
.\env\Scripts\activate
```
7. Instalar todas las dependencias del programa.
```
pip install -r requirements.txt
```
8. Ejecuta el programa.
```
python ./main.py
```

_Nota:_ Para desactivar tu Entorno Virtual ejecuta el siguiente comando
```
deactivate
```
