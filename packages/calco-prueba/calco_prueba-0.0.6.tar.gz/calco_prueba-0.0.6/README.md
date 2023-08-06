# Libreria Calconut
#
#
#
[![N|Solid](https://www.calconut.com/wp-content/uploads/2020/09/logo.svg)](https://calconut.com)


Esta es la libreria de Calconut, creada para uso propio de integraciones y automatizaciones.

## Indice
- `CodeDecode( )`
- `conectar_MariaDB( )`
- `conectar_HanaDB( )`
- `SAPContextManager( )`
- `enviarCorreo( )`
- `mail_send( )`
- `API_microsoft( )`

## requirements.txt
Para instalar todas las dependencias copia y pega estas librerias en un archivo requiremens.txt y luego ejecutalo con pip.
```sh
msal==1.21.0
calco-prueba == 1.0.4
smbprotocol==1.10.1
certifi == 2022.12.7
cffi == 1.15.1
charset-normalizer == 3.0.1
cryptography == 39.0.0
hdbcli == 2.15.19
idna == 3.4
mariadb == 1.1.5.post3
numpy == 1.24.1
packaging == 23.0
pycparser == 2.21
python-dateutil == 2.8.2
pytz == 2022.7.1
requests == 2.28.2
six == 1.16.0
urllib3 == 1.26.14
```

## - CodeDecode( )

Este es el modulo que usamos para codificar, descodificar o parsear archivos .ini

#### Para codificar:
```sh
import configparser

parser = configparser.ConfigParser()
parser.read("./config.ini")
code = cm.CodeDecode()
code.encriptar_items(parser, code.cargar_clave())
```

#### Para descodificar:
```sh
import configparser

parser = configparser.ConfigParser()
parser.read("./config_code.ini")
code = cm.CodeDecode()
mail = code.parserReader('mail', parser)
```

## - conectar_MariaDB( )
#### Atributos
- `host`: ip del host
- `user`: usuario
- `password`: contraseña
- `database`: nombre de la base de datos
- `port`: puerto de conexión (por defecto 3306)
#### Crear conexión:
Ejemplo de como establece conexión a base de datos de mariaDB.
```sh
import calco_prueba as cm

with cm.conectar_MariaDB(host=credencialesDB['host'],
                         port=int(credencialesDB['port']),
                         user=credencialesDB['user'],
                         password=credencialesDB['password'],
                         database=credencialesDB['db']) as conn:
    trabajadores = getEmpleadosFromDB(conn)
```

## - conectar_HanaDB( )
#### Atributos
- `host`: ip del host
- `user`: usuario
- `password`: contraseña
- `port`: puerto de conexión (por defecto 3306)
#### Crear conexión:
Ejemplo de como establece conexión a base de datos de mariaDB.
```sh
import calco_prueba as cm

with cm.conectar_HanaDB(db['host'], db['user'], db['pass'],
                        db['port']) as conn:
    ej = ejemplo(conn)
```

## - SAPContextManager( )
#### Atributos
- `ip`: Dirección IP de SAP
- `CompanyDB`: Nombre de la base de datos de SAP
- `UserName`: Nombre de usuario de SAP
- `password`: Contraseña de usuario de SAP

#### Crear conexión:
Ejemplo de como establece conexión a base de datos de mariaDB.
```sh
import calco_prueba as cm

with cm.SAPContextManager(ip=sap_data['ip'], CompanyDB=sap_data['companydb'],
                          UserName=sap_data['username'],
                          password=sap_data['password']) as conn: 
```


## - enviarCorreo( )
Esta función sirve para mandar un correo usando el hosting de dynaserver.
#### Atributos
- `mensaje`: mensaje a enviar
- `destino`: correo de destino
- `origen`: correo de origen
- `asunto`: asunto del correo
- `server`: servidor smtp del correo
- `puerto`: puerto del servidor smtp
- `password`: contraseña del correo
- `isFile`: True o False
- `fileName`: ruta local al archivo

#### Crear conexión:
Ejemplo de como establece conexión a base de datos de mariaDB.
```sh
import calco_prueba as cm

cm.enviarCorreo(msg,
                mail['destinatario'],
                mail['remitente'],
                mail['asunto'],
                mail['server'],
                mail['port'],
                mail['pass']
                )
```

## - mail_send( )
Esta función sirve para mandar un correo usando el hosting de dynaserver.
#### Atributos
- `mensaje`: mensaje a enviar
- `destino`: correo de destino (Si es mas de uno ponerlo en una)
- `origen`: correo de origen
- `asunto`: asunto del correo
- `server`: servidor smtp del correo
- `puerto`: puerto del servidor smtp
- `password`: contraseña del correo
- `isFile`: True o False
- `fileName`: ruta local al archivo
- `copia`: lista de personas que van en copia

#### Crear conexión:
Ejemplo de como establece conexión a base de datos de mariaDB.
```sh
import calco_prueba as cm

cm.mail_send(msg,
             mail['destinatario'],
             mail['remitente'],
             mail['asunto'],
             mail['server'],
             mail['port'],
             mail['pass']
             )
```


## - API_microsoft():
Funciones para el uso de la API de Microsoft Graph:
* `obtenerAccessToken()`
* `getIdMicrosoft(email)`
* `enableDisableAccount(email, desbloquear)`
* `getRuleID(email)`
* `deshabilitar_redireccion(email)`
* `redireccionar(email, email_redireccion)`

Instanciamos la clase de API_microsoft
```sh
import calco_prueba as cm

# Instanciamos la api
api = cm.API_microsoft()
```

#### Obtener access token
Para obtener el acces_token necesitamos tener en la ruta raiz de nuestro proyecto un archivo `parameters.json` con los siguientes datos:
> {
  "authority": "https://login.microsoftonline.com/<id_microsoft>",
  "client_id": "<client_id_de_microsoft",
  "scope": [ "https://graph.microsoft.com/.default" ],
  "secret": "<secret_microsoft",
  "endpoint": "https://graph.microsoft.com/v1.0/users"
}
```sh
# Despues de instanciar la clase y guardarlo en api
access_token = api.obtenerAccessToken()
```

#### Obtener ID de Microsoft de un usuario
```sh
email = 'ejemplo@mail.com'
id_microsoft = api.getIdMicrosoft(email)
```

#### Bloquear o desbloquear la cuenta de un usuario
```sh
email = 'ejemplo@mail.com'
# Bloquear usuario
api.enableDisableAccount(email, 'false')
# Desbloquear usuario
api.enableDisableAccount(email, 'true')
```

#### Obtener ID las reglas de Outlook de un usuario
```sh
email = 'ejemplo@mail.com'
ids_reglas = api.getRuleID(email)
```

#### Deshabilitar la redirección mediante regla de un usuario
```sh
email = 'ejemplo@mail.com'
api.deshabilitar_redireccion(email)
```

#### Redireccionar mediante regla a un usuario
```sh
email = 'ejemplo@mail.com'
email_redireccion = 'ejemplo2@mail.com'
api.redireccionar(email, email_redireccion)
```

## - samba_conection():
Esta clase contiene las funciones que necesitan una conexion de samba a una unidad de red.
#### Subir un archivo a una unidad de red
Parámetros smb_conection:
> username = user
password = Pass!
server_ip = 192.168.1.8
server_path = 192.168.1.8\MiUnidad\
```sh
# Instanciamos CodeDecode y parseamos config_code.ini para el parámetro smb
code = cm.CodeDecode()
smb_conection = code.parserReader('smb', parser)

# Instanciamos la clase samba_conection
smb = cm.samba_conection()

archivo = 'ejemplo.pdf'
# Ruta de la unidad de red
ruta_unid_red = r'ip\ruta\unidad\de\red'
ruta_salida = os.path.join(ruta_unid_red, archivo)
# Ruta del archivo de entrada
ruta_entrada = os.path.join('.', archivo)

# Subimos archivo
smb.uploadFile(ruta_entrada, ruta_salida, smb_conection, archivo)
```


> Autor: Kirill Zhiganov
> Empresa: Calconut S.L.


