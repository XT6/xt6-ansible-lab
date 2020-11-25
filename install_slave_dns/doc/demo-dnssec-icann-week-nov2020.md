# Firmando zonas autoritativas en 15 minuts

## Explicacion general 

- lab basado en Vagrant
- provisionado con Ansible

Levantar con:

```
vagrant up
```

## Cargar el servidor y verificar la operacion

Zona: pande.mia

dig @localhost soa +multi pande.mia

## Firmar con DNSSEC

1. Generar un par de claves ZSK

```
dnssec-keygen -K . -a RSASHA256 -b 2048 -n ZONE pande.mia
```

2. Firmar la zona 

```
dnssec-signzone -S -P -K . -o pande.mia db.pande.mia
```