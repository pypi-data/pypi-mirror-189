# Transbank Python POS SDK


SDK Oficial de Transbank para POS integrado

## Requisitos:

- Python 3.4+

# Instalación

Puedes instalar el SDK directamente

```bash
pip install transbank-pos-sdk
```
### ¿Cómo se usa?
Como se explica más abajo, la documentación oficial está en [Transbank developers](https://www.transbankdevelopers.cl/producto/posintegrado), pero como una breve introducción: 

#### `listPorts()`
Devuelve una lista de los puertos disponibles.
```python
from transbank.POS.POSIntegrado import POSIntegrado

POS = POSIntegrado()
ports = POS.list_ports()
print(ports)
```

#### `open_port(port: str)`
Abre el puerto indicado. Retorna `True` si logra abrir el puerto, en caso contrario retorna `False`.
```python
port = "/dev/cu.usbmodem0123456789ABCD1"
print(POS.open_port(port))
```
#### `close_port()`
Cierra el puerto que se haya abierto previamente.
```python
print(POS.close_port())
```
#### `poll()`
Ejecuta el comando `POLL` en el POS. Retorna `True` si el POS se encuentra conectado.
```python
print(POS.poll())
```

#### `POS.load_keys()`
Ejecuta el comando `load keys` en el POS.
```python
print(POS.load_keys())
```

#### `POS.sale(amount: int, ticket: str, send_status=False, callback=None)`
Ejecuta el comando `sale` en el POS.
`amount` es el integer que representa el monto a pagar. `ticket` es un número de ticket  que te permita 
referenciar la venta internamente.

Si `sendStatus` es `false` el POS solo enviará un mensaje cuando se termine el proceso de venta. Si `sendStatus` es 
`false` el POS enviará mensajes a medida que se va avanzando en el proceso  (se selecciona método de pago, 
el usuario pasa la tarjeta, se ingresa la clave, etc). Estos mensajes de estados intermedios se pueden capturar 
definiendo una función en el parámetro `callback`
```python
# Venta con mensajes intermedios
def intermediate_message_callback(response):
    print("Intermediate message: {}".format(str(response['response_message'])))
    
print(POS.sale(25000, "abcd12", True, callback=intermediate_message_callback))

# Venta sin mensajes intermedios
print(POS.sale(25000, "123456"))
```

#### `POS.multicode_sale(amount: int, ticket: str, commerce_code: int, send_status=False, callback=None)`
Ejecuta el comando `multicode sale` en el POS.
`amount` es el integer que representa el monto a pagar. `ticket` es un número de ticket  que te permita 
referenciar la venta internamente. `commerce_code` es el código de comercio que ejecutara la venta

Si `sendStatus` es `false` el POS solo enviará un mensaje cuando se termine el proceso de venta. Si `sendStatus` es 
`false` el POS enviará mensajes a medida que se va avanzando en el proceso  (se selecciona método de pago, 
el usuario pasa la tarjeta, se ingresa la clave, etc). Estos mensajes de estados intermedios se pueden capturar 
definiendo una función en el parámetro `callback`
```python
# Venta con mensajes intermedios
def intermediate_message_callback(response):
    print("Intermediate message: {}".format(str(response['response_message'])))
    
print(POS.multicode_sale(1200, "Tic123", 597029414301, send_status=True, callback=intermediate_message_callback))

# Venta sin mensajes intermedios
print(POS.multicode_sale(1200, "Tic123", 597029414301))
```

#### `last_sale()`
Ejecuta el comando `last sale` en el POS.
```python
print(POS.last_sale())
```

#### `multicode_last_sale(send_voucher=False)`
Ejecuta el comando `multicode last sale` en el POS. `send_voucher` indica si el comprobante de la ultima venta debe ser enviado a la caja.
```python
print(POS.multicode_last_sale(True))
```

#### `refund(operation_id: int)`
Ejecuta el comando `refund` en el POS. `operation_id` es el número de operación que se quiere anular.
```python
print(POS.refund(83))
```

#### `totals()`
Ejecuta el comando `totals` en el POS.
```python
print(POS.totals())
```

#### `details(print_on_pos=False)`
Ejecuta el comando `details` en el POS. `print_on_pos` indica si la información se debe imprimir en el POS o en la caja.
```python
print(POS.details(False))
```

#### `close()`
Ejecuta el comando `close` en el POS.
```python
print(POS.close())
```

## Documentación

Puedes encontrar toda la documentación de cómo usar este SDK en el sitio https://www.transbankdevelopers.cl.

La documentación relevante para usar este SDK es:


## Información para contribuir y desarrollar este SDK

### Requerimientos
- [Pipenv](https://github.com/pypa/pipenv)
- Plugin de editorconfig para tu editor favorito.

### Standares

- Para los commits respetamos las siguientes normas: https://chris.beams.io/posts/git-commit/
- Usamos ingles, para los mensajes de commit.
- Se pueden usar tokens como WIP, en el subject de un commit, separando el token con `:`, por ejemplo:
`WIP: This is a useful commit message`
- Para los nombres de ramas también usamos ingles.
- Se asume, que una rama de feature no mezclada, es un feature no terminado.
- El nombre de las ramas va en minúsculas.
- Las palabras se separan con `-`.
- Las ramas comienzan con alguno de los short lead tokens definidos, por ejemplo: `feat/tokens-configuration`

#### Short lead tokens
##### Commits
- WIP = Trabajo en progreso.

##### Ramas
- feat = Nuevos features
- chore = Tareas, que no son visibles al usuario.
- bug = Resolución de bugs.

### Todas las mezclas a master se hacen mediante Pull Request.


### Deploy de una nueva versión.
Para generar una nueva versión, se debe crear un PR (con un título "Prepare release X.Y.Z" con los valores que correspondan para `X`, `Y` y `Z`). Se debe seguir el estándar semver para determinar si se incrementa el valor de `X` (si hay cambios no retrocompatibles), `Y` (para mejoras retrocompatibles) o `Z` (si sólo hubo correcciones a bugs).

En ese PR deben incluirse los siguientes cambios:

1. Modificar el archivo `CHANGELOG.md` para incluir una nueva entrada (al comienzo) para `X.Y.Z` que explique en español los cambios **de cara al usuario del SDK**.
2. Modificar [__version__.py](./transbank/__version__.py) para que apunte a la nueva versión `X.Y.Z`.

Luego de obtener aprobación del pull request, debe mezclarse a master e inmediatamente generar un release en GitHub con el tag `vX.Y.Z`. En la descripción del release debes poner lo mismo que agregaste al changelog.

Con eso Travis CI generará automáticamente una nueva versión de la librería y la publicará en PyPI.