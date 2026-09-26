# Ecuación separable y método de Euler

Este proyecto resuelve una ecuación diferencial separable de primer orden de dos maneras: analíticamente, mediante separación de variables, y numéricamente, mediante el método de Euler.

## Problema

Consideramos la ecuación

```text
dy/dt = -2y,    y(0) = 1
```

Separamos las variables e integramos:

```text
dy/y = -2 dt
ln|y| = -2t + C
```

Por tanto, `y(t) = C exp(-2t)`. Al aplicar la condición inicial `y(0) = 1`, se obtiene la solución exacta:

```text
y(t) = exp(-2t)
```

## Aproximación de Euler

En el intervalo `[0, 1]` usamos el paso `h = 0.2`. La fórmula de Euler es

```text
y_(n+1) = y_n + h f(t_n, y_n)
```

Como `f(t, y) = -2y`, cada paso queda `y_(n+1) = 0.6 y_n`. Se realizan cinco pasos para llegar de `t = 0` a `t = 1`. El programa muestra en cada punto la aproximación, el valor exacto y el error absoluto.

## Ejecutar

Se requiere Python 3 y no hacen falta paquetes externos.

```bash
python main.py
```
