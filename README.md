rxnplot
======
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/qcuaeh/rxnplot.git/HEAD?labpath=tests)

**rxnplot** es un paquete de Python 3 para dibujar diagramas de niveles de energía de reacciones químicas. Está basado en el paquete
[rxnlvl](https://github.com/eutactic/rxnlvl) pero tiene soporte para documentos de [Jupyter](https://jupyter.org) y opciones adicionales para ajustar las unidades de energía.

![graphic](graphic.png)

Instale rxnplot
------

Puede instalar **rxnplot** en su computadora con pip:

    pip install rxnplot

Pruebe rxnplot en Binder
------

También puede [Abrir rxnplot en Binder](https://mybinder.org/v2/gh/qcuaeh/rxnplot.git/HEAD?labpath=tests) sin necesidad de instalar nada en su computadora.

Construya un diagrama paso a paso
------

Para crear diagramas tendrá que escribir código de Python, pero incluso si nunca ha usado Python puede aprender a usar rxnplot rápidamente.

### Primero importe el módulo

    from rxnplot import *

### y cree un objeto de gráfico

    p = plot(10.0, zero=energy(0.0, 'kjmol'), units='kcalmol', digits=1True)
    
El objeto `plot` requiere los siguientes argumentos:

- `size` - El tamaño vertical del gráfico en cm.
- `bgcolour` - El color de fondo de la imagen, como un entero hexadecimal de 24 bits o `None`. Si es `None`, el fondo será transparente.
- `zero` - Un objeto `energy` que representa el cero de las energías relativas. Requiere dos argumentos: la energía como un número de punto flotante y las unidades que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcalmol'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `units` - Las unidades de energía del diagrama, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcalmol'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `digits` - Los dígitos después del punto decimal que se usarán para mostrar las energías en el diagrama.
- `qualified` - Si es `True`, se mostrarán las unidades de energía en el diagrama, de lo contrario sólo se mostrarán los valores numéricos.

Ahora puede empezar a agregar elementos al gráfico.

### Incluya una línea base (esto es opcional)

    p + baseline(colour=0x0, mode='dashed', opacity=0.1)

El objeto `baseline` es una línea que representa el cero de energía y requiere los siguientes argumentos:

- `colour` - Un entero hexadecimal de 24 bits quw representa el color de la arista.
- `mode` - Controla la apariencia de la arista, puede ser `'normal'` o `'dashed'`.
- `opacity` - Un flotante entre 0.0 y 1.0 que representan la opacidad de la arista.

### Defina los niveles de energía

    p + level(energy(0, 'kjmol'),  1,   '1',  0x0)
    p + level(energy(0, 'kjmol'),  2, 'TS1',  0x0)
    p + level(energy(0, 'kjmol'),  3,   '2',  0x0)

Cada objeto `level` requiere los siguientes argumentos:

- `energy` - Un objeto que representa la energía relativa del nivel. El objeto `energy` tiene dos argumentos: la energía como un número de punto flotante y las unidades, que pueden ser `'kjmol'`, `'eh'` (Hartrees), `'ev'` (electronvoltios), `'kcalmol'` (kilocalorías por mol termoquímicas) o `'wavenumber'`.
- `location` - La ubicación ordinal del nivel en el diagrama, debe ser un entero positivo diferente de cero. Diferentes niveles pueden compartir la misma ubicación.
- `name` - El nombre del nivel en el diagrama, que debe ser único.
- `colour` - Un entero hexadecimal de 24 bits quw representa el color del nivel.

### Conecte los niveles de energía

    p + edge(  '1', 'TS1',  0x0,  0.5,  'normal')
    p + edge('TS1',   '2',  0x0,  0.5,  'normal')

Cada objeto `edge` acepta los siguientes argumentos:

- `start` - El `nombre` del nivel del que se origina la arista.
- `end` - El `nombre` del nivel en el que termina la arista, tiene que ser diferente de `start`.
- `colour` - Un entero hexadecimal de 24 bits representando el color de la arista.
- `opacity` - Un flotante entre 0.0 y 1.0 representando la opacidad de la arista.
- `mode` - Controla la apariencia de la arista, puede ser `'normal'` o `'dashed'`.

### Finalmente visualice el diagrama

    p.render()

Mostrará el diagrama en una celda del documento.

### o guarde el diagrama en un archivo

    p.write('diagrama.png')

guardará el diagrama como PNG. Puede cambiar el tamaño de la imagen con la opción `scale`. Por ejemplo 

    p.write('diagrama.png', scale=2)

guardará el diagrama con el doble de la resolución por defecto. También puede guardar el diagrama como archivo PDF o SVG.
