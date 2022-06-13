irxnlvl
======

Es un programa para dibujar fácilmente diagramas de niveles de energía de reacciones químicas y es una versión simplificada del paquete [rxnlvl](https://github.com/eutactic/rxnlvl), que corre nativamente en notebooks de Jupyter. Para usarlo necesitas clonar o descargar `irxnlvl` y tener instalado Python 3.4 o superior o puedes [probar irxnvl en Binder](https://mybinder.org/v2/gh/qcuaeh/irxnlvl.git/HEAD) sin necesidad de instalar nada en tu computadora.

![diagrama 2](diagrama2.png)

Crea tu primer diagrama
------

Para crear diagramas requerirás escribir código de Python, pero incluso si no sabes Python puedes aprender rápidamente explorando los siguientes ejemplos:

- [Abrir el ejemplo 1 en Binder](https://mybinder.org/v2/gh/qcuaeh/irxnlvl.git/HEAD?labpath=example1.ipynb)
- [Abrir el ejemplo 2 en Binder](https://mybinder.org/v2/gh/qcuaeh/irxnlvl.git/HEAD?labpath=example2.ipynb)

Los pasos utilizados en los ejemplos se explican a continuación.

### Importa todo el contenido del módulo

    from irxnlvl import *

### Crea un diagrama vacío para poder agregar elementos

    p = plot(10.0, vbuf=10.0, hbuf=5.0, bgcolour=None, zero=energy(0.0, 'kjmol'), units='kjmol', digits=1)
    
`plot` toma los siguientes argumentos:
- `size` - El tamaño vertical del gráfico en cm.
- `bgcolour` - el color de fondo de la imagen, como un entero hexadecimal de 24 bits, o `None`. Si `None`, el fondo será transparente.
- `zero` - un objeto `energy` que representa el cero de las energías relativas. El objeto `energy` tiene dos argumentos: la energía como un número de punto flotante y las unidades, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcalmol'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `units` - Las unidades de energía del diagrama, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcalmol'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `digits` - Los dígitos después del punto decimal que se usarán para mostrar las energías del diagrama.
- `qualified` - Si es `True`, las unidades en las que cada energía es especificada serán impresas en la imagen. Si es `False`, sólo imprimirá los valores numéricos. Si se especifica *cualquier* valor de cadena, sólo imprimirá las unidades en el nivel de energía de extrema izquierda, que es útil cuando quieres dar las unidades en tu gráfica pero no quieres atiborrarla.


Ahora podemos empezar a agregar elementos al gráfico.

### Agrega una línea base

    p + baseline(colour=0x0, mode='dashed', opacity=0.1)

Sólo puedes tener una línea de base que representa el cero de las energías relativas y toma los siguientes argumentos:
- `colour` - un entero hexadecimal de 24 bits representando el color de la arista.
- `mode` - elije entre `'normal'` o `'dashed'`. Controla la apariencia de la arista en términos de la discontinuidad de la línea.
- `opacity` - un flotante entre 0.0 y 1.0 representando la opacidad de la arista.

### Agrega los niveles de energía

    p +  level(energy(0, 'kjmol'),  1,  '1',  0x0)

Cada objeto `level` toma los siguientes argumentos:
- `energy` - un objeto que representa la energía relativa del nivel. El objeto `energy` tiene dos argumentos: la energía como un número de punto flotante y las unidades, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcalmol'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `location` - la ubicación ordinal del nivel en el esquema. Éste debe ser un entero positivo diferente de cero. Diferentes niveles pueden compartir la misma ubicación.
- `name` - el nombre del nivel en el esquema. Los niveles no deberían compartir el mismo nombre.
- `colour` - un entero hexadecimal de 24 bits representando el color del nivel.

### Une los niveles de energía

    p +  edge(  '1',  'EC1', 0x0, 0.4, 'normal')

Cada `edge` toma los siguientes argumentos:
- `start` - el `name` del nivel del que se origina la arista.
- `end` - el `name` del nivel en el que termina la arista. Éste tiene que ser diferente de `start`.
- `colour` - un entero hexadecimal de 24 bits representando el color de la arista.
- `opacity` - un flotante entre 0.0 y 1.0 representando la opacidad de la arista.
- `mode` - elije entre `'normal'` o `'dashed'`. Controla la apariencia de la arista en términos de la discontinuidad de la línea.

### Visualiza el diagrama

    p.render()

### Y si es correcto guárdalo

    p.write('diagrama.svg')

Creará un archivo `diagrama.svg` de tu gráfica en la misma carpeta donde se abrió el notebook.
