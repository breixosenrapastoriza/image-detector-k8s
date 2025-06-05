#!/bin/bash

set -e

# Crear estructura de carpetas
mkdir -p dns-server/config/zones
cd dns-server

# Crear named.conf.options
cat <<EOF > config/named.conf.options
options {
  directory "/var/cache/bind";

  forwarders {
    8.8.8.8;
    8.8.4.4;
  };

  allow-query { any; };
  recursion yes;
};
EOF

# Crear named.conf.local
cat <<EOF > config/named.conf.local
zone "albreimage.com" {
    type master;
    file "/etc/bind/zones/db.albreimage.com";
};
EOF

# Crear archivo de zona
cat <<EOF > config/zones/db.albreimage.com
\$TTL 604800
@   IN  SOA ns.albreimage.com. admin.albreimage.com. (
        1         ; Serial
        604800    ; Refresh
        86400     ; Retry
        2419200   ; Expire
        604800 )  ; Negative Cache TTL

@       IN  NS      ns.albreimage.com.
ns      IN  A       192.168.204.131
@       IN  A       192.168.204.131
EOF

# Crear Dockerfile
cat <<EOF > Dockerfile
FROM ubuntu:20.04

RUN apt-get update && \\
    DEBIAN_FRONTEND=noninteractive apt-get install -y bind9 dnsutils && \\
    mkdir -p /etc/bind/zones

COPY config/named.conf.options /etc/bind/named.conf.options
COPY config/named.conf.local /etc/bind/named.conf.local
COPY config/zones/db.albreimage.com /etc/bind/zones/db.albreimage.com

CMD ["named", "-g"]
EOF

# Construir imagen Docker
docker build -t mydns .

# Ejecutar contenedor con red del host
docker run -d --name dns-server --restart=always --network=host mydns

echo "Servidor DNS desplegado en 192.168.204.131"
