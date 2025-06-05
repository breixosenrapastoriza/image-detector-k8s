#!/bin/sh

# Ruta a la imagen local (puedes empotrar una imagen en la imagen Docker si lo deseas)
IMAGE_URL="https://i.pinimg.com/originals/c2/8a/85/c28a85f5c9fc226116128a4f3ef8b020.png"

# Descargar la imagen una vez
curl -o /tmp/test.png "$IMAGE_URL"

# Enviar solicitudes en bucle
while true; do
  curl -X POST http://192.168.204.132:30081/api/predict \
       -F "file=@/tmp/test.png" \
       -H "Expect:"
done
