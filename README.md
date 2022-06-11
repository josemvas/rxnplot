irxnlvl
======

Es una versión interactiva del paquete rxnvl para dibujar atractivos diagramas de niveles de energía de reacciones químicas. Puede ejecutarse interactivamente en Jupyter Notebook o como un script de Python.

¿Qué necesito?
------
`irxnlvl` require Python 3.x o superior.

¿Cómo lo uso?
------
El paquete se puede ejecutar en un notebook de Jupyter o como un script de Python, pero incluso si no sabes python deberías poder crear gráficas fácilmente. Puedes ejecutar y modificar los siguientes ejemplos en Binder:

- [Ejemplo 1](https://mybinder.org/v2/gh/qcuaeh/irxnlvl.git/HEAD?labpath=example1.ipynb)
- [Ejemplo 2](https://mybinder.org/v2/gh/qcuaeh/irxnlvl.git/HEAD?labpath=example2.ipynb)

Los pasos utilizados en los ejemplos se explican a continuación.

### Importar el módulo

    from irxnlvl import *

### Creación del gráfico

    p = plot([25.0,10.0], vbuf=10.0, hbuf=5.0, bgcolour=None, qualified='sortof')
    
`plot` toma los siguientes argumentos:
- `dimensions` - el ancho y alto del gráfico en cm.
- `vbuf` - el margen vertical como un porcentaje de la altura total.
- `hbuf` - el margen horizontal como un porcentaje de la altura total.
- `bgcolour` - el color de fondo de la imagen, como un entero hexadecimal de 24 bits, o `None`. Si `None`, el fondo será transparente.
- `qualified` - Si `True`, las unidades en las que cada energía es especificada serán impresas en la imagen. Si `False`, sólo imprimirá los valores numéricos. Si se especifica *cualquier* valor de cadena, sólo imprimirá las unidades en el nivel de energía de extrema izquierda, que es útil cuando quieres dar las unidades en tu gráfica pero no quieres atiborrarla.

Ahora podemos empezar a agregar elementos al gráfico.

### Momento de agregar algunos niveles

    p +  level(energy(0, 'kjmol'),  1,  '1',  0x0)

Cada objeto `level` toma los siguientes argumentos:
- `energy` - un objeto `energy` que representa la energía relativa del nivel. Cada energía tiene dos argumentos - la energía como un número de punto flotante, y las unidades, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcal'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `location` - la ubicación ordinal del nivel en el esquema. Éste debe ser un entero positivo diferente de cero. Diferentes niveles pueden compartir la misma ubicación.
- `name` - el nombre del nivel en el esquema. Los niveles no deberían compartir el mismo nombre.
- `colour` - un entero hexadecimal de 24 bits representando el color del nivel.

### Momento de unir los niveles con aristas

    p +  edge(    '1',  'EC1', 0x0, 0.4, 'normal')

Cada `edge` toma los siguientes argumentos:
- `start` - el `name` del nivel del que se origina la arista.
- `end` - el `name` del nivel en el que termina la arista. Éste tiene que ser diferente de `start`.
- `colour` - un entero hexadecimal de 24 bits representando el color de la arista.
- `opacity` - un flotante entre 0.0 y 1.0 representando la opacidad de la arista.
- `mode` - elije entre `'normal'` o `'dashed'`. Controla la apariencia de la arista en términos de la discontinuidad de la línea.

### ¿Podemos tener una linea de base graduada en 0.0 kJ/mol? Si

    p + baseline(energy( 0.0, 'kjmol'), colour=0x0, mode='dashed', opacity=0.1)

Sólo puedes tener una línea de base. La sintaxis debe de ser bastante familiar:
- `energy` - un objeto `energy` que representa la energía relativa de la línea de base. Cada energía tiene dos argumentos - la energía como un número de punto flotante, y las unidades, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcal'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `colour` - un entero hexadecimal de 24 bits representando el color de la arista.
- `mode` - elije entre `'normal'` o `'dashed'`. Controla la apariencia de la arista en términos de la discontinuidad de la línea.
- `opacity` - un flotante entre 0.0 y 1.0 representando la opacidad de la arista.

### Visualicemos el resultado

    p.render()

### Y guardémoslo

    p.write('diagrama.svg')

Creará un archivo `diagrama.svg` de tu gráfica en la misma carpeta donde se abrió el notebook.
