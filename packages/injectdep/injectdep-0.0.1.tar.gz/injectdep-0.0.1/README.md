# Probando injection dependency

Librareria para la inyección de dependencias para python

## Porqué usarlo ?

Pues esta librería está hecha para proyectos pequeños que no necesiten testear la applicación o que quieran probar la inyección de dependencias


## Cómo usarlo ?

Aquí es un ejemplo de inyección de forma global con la librería

```py
from injectdep import global_module


@global_module.register
class MyDB:
    def find_all():
        return ["Jhon", "Pepe", "Carlos"]

def main(db: MyDB):
    results = db.find_all()
    print(results) # ["Jhon", "Pepe", "Carlos"]


if __name__ == "__main__":
    injected = global_module.inject(main)
    injected()
```

## Puede construir su propio módulo

```py
from injectdep import Module

database_module = Module()

@database_module.register
class MyDB:
    def find_all():
        return ["Jhon", "Pepe", "Carlos"]

def main(db: MyDB):
    results = db.find_all()
    print(results) # ["Jhon", "Pepe", "Carlos"]


if __name__ == "__main__":
    injected = database_module.inject(main)
    injected()
```

<p align="center">Inspirado en AngularModules</p>
