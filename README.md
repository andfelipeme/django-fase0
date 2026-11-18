# Fase 0 — El Python que necesita Django

> Verificado con **uv 0.13.9** y **Python 3.15.2** (noviembre 2026). Todas las salidas son reales.

---

## 0. Entorno de trabajo

**uv**: gestor de proyectos de Python. Instala la versión de Python, crea el entorno virtual y ejecuta el código.

### Revisar la versión de uv

```bash
uv --version        # debe decir 0.13.x
which uv            # muestra cómo se instaló
```

| `which uv` muestra | Instalado con | Actualizar con |
|---|---|---|
| `/opt/homebrew/bin/uv` | Homebrew | `brew upgrade uv` |
| `~/.local/bin/uv` | Instalador oficial | `uv self update` |

> No usar `uv self update` si se instaló con Homebrew.

### Crear el proyecto

Desde uv 0.12.0, `uv init` crea proyectos **empaquetados** por defecto (carpeta `src/`, sin `main.py`). Para scripts y para Django usamos el formato simple:

```bash
uv init --no-package --python 3.15 fase0
cd fase0
uv run main.py          # Hello from fase0!
```

- `--no-package`: proyecto simple, `main.py` en la raíz, sin sistema de build.
- `--python 3.15`: Python estable actual. Django lo soporta oficialmente desde la 6.1.3.

```
fase0/
├── .gitignore          ← ya excluye __pycache__/ y .venv
├── .python-version     ← 3.15
├── README.md
├── main.py
└── pyproject.toml      ← requires-python = ">=3.15"
```

Con el primer `uv run` aparecen `.venv/` y `uv.lock`. Cada archivo se ejecuta con `uv run archivo.py`.

---

## Clase 1 — Clases y objetos

| Concepto | Qué es |
|---|---|
| **Clase** | El molde o plano: define qué datos tiene algo y qué sabe hacer |
| **Objeto (instancia)** | Una cosa concreta hecha con ese molde |
| **`__init__`** | Método que Python ejecuta solo al crear el objeto; le da sus datos iniciales |
| **`self`** | El objeto mismo; con `self` cada objeto guarda y lee **sus propios** datos |
| **Atributo** | Variable que pertenece al objeto: `self.nombre` |
| **Método** | Función dentro de la clase; siempre recibe `self` primero |

> Analogía: el diseño CAD es la clase; cada pieza impresa es un objeto.
> En Django: cada tabla es una clase (modelo) y cada fila es un objeto.

```python
class Impresora:
    def __init__(self, nombre, tipo):
        self.nombre = nombre      # dato que se pasa al crearla
        self.tipo = tipo
        self.horas_uso = 0        # dato que arranca con valor fijo

    def imprimir(self, horas):    # método que CAMBIA datos
        self.horas_uso += horas

    def necesita_mantenimiento(self):   # método que DEVUELVE un resultado
        return self.horas_uso >= 200


principal = Impresora("Principal", "FDM")
principal.imprimir(210)
print(principal.necesita_mantenimiento())   # True
```

### PHP → Python

| PHP | Python |
|---|---|
| `__construct()` | `__init__()` |
| `$this->nombre` | `self.nombre` |
| `new Impresora(...)` | `Impresora(...)` |
| `$obj->metodo()` | `obj.metodo()` |

En Python **tú escribes `self`** como primer parámetro de cada método.

### Errores típicos

| Error | Mensaje |
|---|---|
| Olvidar `self` en el método | `TypeError: Impresora.imprimir() takes 1 positional argument but 2 were given` |
| `nombre = nombre` en vez de `self.nombre = nombre` | `AttributeError: 'Impresora' object has no attribute 'nombre'` |
| `_init_` con un solo guion bajo | `TypeError: Impresora() takes no arguments` |

---

## Clase 2 — `__str__` y atributos de clase

### `__str__`

- Método especial que Python llama solo al convertir el objeto en texto: `print()`, `str()` y f-strings.
- **Debe devolver (`return`) un `str`.**
- Sin él, `print(objeto)` muestra `<__main__.Impresora object at 0x...>`.
- En Django, el Admin muestra cada objeto con su `__str__`.

### Atributo de instancia vs. atributo de clase

| | Instancia | Clase |
|---|---|---|
| Dónde | Dentro de `__init__`, con `self.` | Directo en la clase, fuera de métodos |
| De quién | De cada objeto | Uno solo, compartido por todos |
| Ejemplo | `self.horas_uso = 0` | `HORAS_MANTENIMIENTO = 200` |

- Constantes en MAYÚSCULAS.
- Se **leen** con `self.X` o `Clase.X`; se **modifican** con `Clase.X`.
- `Clase.X = valor` cambia el valor para **todos**; `objeto.X = valor` solo para ese objeto.
- Listas y diccionarios **no** van como atributo de clase (se comparten); van en `__init__`.

```python
class Impresora:
    HORAS_MANTENIMIENTO = 200
    total = 0

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.horas_uso = 0
        Impresora.total += 1          # se modifica a través de la CLASE

    def necesita_mantenimiento(self):
        return self.horas_uso >= self.HORAS_MANTENIMIENTO

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.horas_uso} h"
```

### En Django

```python
class Filamento(models.Model):
    material = models.CharField(max_length=50)   # campos = atributos de clase
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.material} {self.color}"
```

### PHP → Python

| PHP | Python |
|---|---|
| `__toString()` | `__str__()` |
| `const HORAS = 200;` / `self::HORAS` | `HORAS = 200` / `self.HORAS` |
| `public static $total = 0;` / `self::$total++` | `total = 0` / `Impresora.total += 1` |

### Errores típicos

| Error | Qué pasa |
|---|---|
| `__str__` devuelve un número | `TypeError: Impresora.__str__() must return a str, not int` |
| `print` en vez de `return` en `__str__` | Imprime y luego `TypeError: ... must return a str, not NoneType` |
| Contador con `self.total += 1` | **Sin error**, pero `Impresora.total` queda en 0 (cada objeto crea su copia) |

---

## Clase 3 — Herencia

- **Herencia**: la clase **hija** toma todo de la **padre** y puede agregar o cambiar cosas. `class Hija(Padre):`
- Úsala solo si la frase **"es un"** tiene sentido (un dron *es una* máquina).
- **`pass`**: hereda todo sin agregar nada.
- **Sobrescribir (override)**: definir en la hija algo con el mismo nombre; gana el de la hija. Los métodos del padre leen los valores de la hija gracias a `self`.
- **`super()`**: accede a la versión del padre.
  - Si la hija tiene su propio `__init__`, **siempre** llama `super().__init__(...)` (sin `self`).
  - `super().metodo()` sirve para **extender** (lo del padre + lo tuyo). Sin `super()` = **reemplazar**.

```python
class Maquina:
    HORAS_MANTENIMIENTO = 200

    def __init__(self, nombre):
        self.nombre = nombre
        self.horas_uso = 0

    def usar(self, horas):
        self.horas_uso += horas

    def necesita_mantenimiento(self):
        return self.horas_uso >= self.HORAS_MANTENIMIENTO

    def __str__(self):
        return f"{self.nombre} - {self.horas_uso} h"


class Compresor(Maquina):          # 1. hereda todo
    pass


class Dron(Maquina):               # 2. sobrescribe un atributo de clase
    HORAS_MANTENIMIENTO = 50


class Impresora3D(Maquina):        # 3. super(): datos propios + extender
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} ({self.tipo})"
```

### En Django

- `class Filamento(models.Model)` → el modelo hereda de `Model` todo lo necesario para guardarse en la base de datos.
- Vistas genéricas: se heredan y se sobrescriben atributos:

```python
from django.views.generic import ListView

class ListaFilamentos(ListView):
    model = Filamento
```

- Para hacer algo extra al guardar: se sobrescribe `save()` y se llama `super().save(**kwargs)`.
- En los modelos casi no se escribe `__init__` (Django lo desaconseja).

### PHP → Python

| PHP | Python |
|---|---|
| `class Dron extends Maquina` | `class Dron(Maquina):` |
| `parent::__construct($nombre)` | `super().__init__(nombre)` |
| `parent::__toString()` | `super().__str__()` |

### Errores típicos

| Error | Qué pasa |
|---|---|
| Olvidar `super().__init__(nombre)` | `AttributeError: 'Impresora3D' object has no attribute 'horas_uso'` (sale al **usar** el objeto) |
| `super().__init__(self, nombre)` | `TypeError: Maquina.__init__() takes 2 positional arguments but 3 were given` |
| Crear la hija sin el dato nuevo | `TypeError: Impresora3D.__init__() missing 1 required positional argument: 'tipo'` |
| `super().__str__` sin paréntesis | **Sin error**, imprime `<bound method Maquina.__str__ of ...>` |

---

## Clase 4 — Módulos e imports

| Concepto | Qué es |
|---|---|
| **Módulo** | Cualquier archivo `.py` (`maquinas.py` → módulo `maquinas`) |
| **Paquete** | Carpeta con módulos y un `__init__.py` (puede estar vacío) |
| **`import`** | Trae código de otro módulo para usarlo aquí |
| **`__pycache__`** | Versiones precompiladas `.pyc`; automática, no se toca ni se sube a git |

### Formas de importar

| Forma | Uso |
|---|---|
| `from taller.maquinas import Dron, Maquina` | `Dron(...)` — la más usada y la de Django |
| `from taller import maquinas` | `maquinas.Dron(...)` |
| `import taller.maquinas` | `taller.maquinas.Dron(...)` |

- Los imports van al principio del archivo.
- Importa solo lo que usas (Ruff lo marca como `F401`; revisar con `uvx ruff check .`).

### `if __name__ == "__main__":`

- **Importar un módulo lo ejecuta completo.**
- `__name__` vale `"__main__"` si ejecutas el archivo directamente, y el nombre del módulo (`"taller.maquinas"`) si lo importas.
- Las pruebas de un módulo van dentro de ese `if`, así no se ejecutan al importarlo.

```
fase0/
├── clase4.py
└── taller/
    ├── __init__.py     ← vacío
    └── maquinas.py
```

```bash
mkdir taller
touch taller/__init__.py
```

### De dónde importa Python

1. Tu proyecto (empezando por la carpeta del archivo que ejecutas).
2. La librería estándar: `from datetime import date`.
3. Paquetes instalados en `.venv` con `uv add`: `from django.db import models`.

### Imports relativos (Django)

```python
from django.contrib import admin

from .models import Question     # el punto = "del mismo paquete"
```

Solo funcionan dentro de un paquete. En un script que se ejecuta directamente dan error.

### Novedad de Python 3.15

`lazy import json` (PEP 810): retrasa la carga del módulo hasta que se usa. Opcional; sirve para que programas grandes arranquen más rápido.

### Laravel → Python

| Laravel/PHP | Python |
|---|---|
| `namespace App\Models;` | La carpeta del paquete |
| `use App\Models\Filamento;` | `from inventario.materiales import Filamento` |

### Errores típicos

| Error | Mensaje |
|---|---|
| Módulo mal escrito | `ModuleNotFoundError: No module named 'taller.maquina'. Did you mean: 'taller.maquinas'?` |
| Paquete mal escrito | `ModuleNotFoundError: No module named 'tallr'. Did you mean: 'taller'?` |
| Clase mal escrita | `ImportError: cannot import name 'Drone' from 'taller.maquinas' (...)` |
| Usar sin importar | `NameError: name 'Dron' is not defined` |
| Import relativo en script | `ImportError: attempted relative import with no known parent package` |
| Pruebas sueltas en un módulo | **Sin error**, pero se ejecutan al importar |

---

## Prácticas realizadas

| Práctica | Qué se construyó |
|---|---|
| 1 | Clase `Filamento`: `usar()`, `queda_poco()`, `costo_pieza()`, `recargar()` |
| 2 | Constantes de clase (`PESO_ROLLO`, límite), contador `rollos_creados`, `__str__` |
| 3 | `Material` como padre de `Filamento`, `Resina` y `Tornillo` |
| 4 | Paquete `inventario/` con `materiales.py` y prueba interna con `__name__` |

## Lecciones de las revisiones

- **Comparar antes de restar**: validar primero si alcanza, y solo entonces modificar.
- **`return` vs. `print`**: un método que devuelve algo no muestra nada si nadie lo imprime.
- Una función sin `return` devuelve `None` sola; no hace falta `return None`.
- **Separar cálculo de presentación**: el método devuelve el número; el texto se arma afuera.
- **`+=` vs. `=`**: sumar al valor actual no es lo mismo que reemplazarlo. Elige según lo que represente el objeto (un carrete vs. el inventario).
- **El nombre de un método debe decir lo que hace** (`agregar_rollo()` en vez de `recargar()` si suma).
- **Los atributos de clase se modifican a través de la clase**, nunca con `self.`.
- **Importa solo lo que usas** y borra el código comentado que ya no sirve (git lo guarda).
- Lee siempre **la última línea del error**; Python 3.15 a veces sugiere el nombre correcto.