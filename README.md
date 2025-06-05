# 🎯 Image Detector on Kubernetes

Este proyecto despliega una plataforma de detección de objetos en imágenes sobre un clúster de Kubernetes, utilizando herramientas modernas para garantizar escalabilidad, automatización y observabilidad.

## 🚀 ¿Qué hace?

Permite enviar imágenes a través de una interfaz web, y el sistema responde con las categorías u objetos detectados en ellas. El procesamiento se realiza mediante un modelo de Machine Learning alojado en el backend. Las imágenes y sus resultados se almacenan en AWS S3 para una gestión eficiente y persistente.

## 🧱 Tecnologías principales

- **Kubernetes (AlmaLinux 9)**: clúster de tres nodos para orquestación de contenedores.
- **Helm**: automatiza el despliegue del frontend, backend, proxy inverso, ingress y un simulador de carga.
- **FastAPI + React**: backend inteligente y frontend interactivo.
- **Docker**: contenedores personalizados y servidor DNS externo.
- **Ingress Controller y Proxy Inverso**: exponen la aplicación con acceso mediante dominio.
- **Servidor DNS (Docker)**: permite usar dominios personalizados en lugar de IPs directas.
- **GitLab + KubeSphere**: integración continua aplicada al desarrollo.
- **Horizontal Pod Autoscaler (HPA)**: escalado automático del backend según la carga.
- **Metrics Server**: monitorización del uso de CPU y memoria de pods y nodos.

## 🔁 Funciones clave

- Rollbacks simples con **Helm** y **kubectl** ante errores en despliegues.
- Simulación de carga para probar autoescalado con un pod de pruebas (crash).
- Monitorización integrada para asegurar rendimiento y estabilidad.
- Acceso por dominio gracias a un servidor DNS alojado fuera del clúster.

## 🛠 Ideal para...

Estudiantes, desarrolladores y DevOps que quieran ver una integración realista de Kubernetes con Machine Learning, CI/CD, infraestructura moderna y despliegue de microservicios.

---

# image-detector-k8s
