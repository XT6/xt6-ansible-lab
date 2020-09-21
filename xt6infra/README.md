# ACCIONES COMUNES CON EL ANSIBLE DE MANTENIMIENTO
# ------------------------------------------------

## Consideraciones generales

Hay tres grandes grupos de hosts:

- los equipos y vms locales
- los equipos y vms remotos (linode, etc.)
- el equipamiento de red

El usuario de conexion a las vms locales es carlos y puede siempre hacer sudo.

## Tareas comunes

1. Update de paquetes y actualizacion de usuarios

1.1 Comando basico, para todos los hosts

    ```./mk --tags=xt6pkgupdate```

1.2 Para correr con mucho debug y limitando a un cierto host
 
    ```./mk --tags=xt6pkgupdate -vvv --limit=alonso.in.xt6.us```

2. Actualizar usuarios y claves ssh

   ```./mk --tags=xt6users -vvv --limit=alonso.in.xt6.us```
