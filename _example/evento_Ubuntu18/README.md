Este play se ejecuta corriendo el ./mk que esta en el
directorio raiz de la distribucion.

En cada evento hay que cambiar las siguiente variables
para ajustar las configuraciones al nuevo evento.

 - Instalar Ubuntu
 
 - apt update/upgrade
 
 - Instalar python
     apt install python-minimal
 
 - Agregar clave ssh del usuario que va a correr
   la instalacion (ver el usuario en el script MK)
 
 - Agregar al usuario que corre el proceso en el
   /etc/sudoers  

 - Modificar las variables en roles/utiles/vars/main.yml

 - Customizar /etc/hosts para que tenga la IP local del server
    127.0.0.1	localhost srv{1,2}-lacnic{evt}
    200.0.87.12 lacnic.lacnic.net srv2-lacnic{evt}
 
 - Revisar los datos del host (archivo hosts) a donde conectarse 
   en el script MK y correrlo (root del ansible)

