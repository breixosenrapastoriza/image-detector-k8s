# Usa la imagen oficial de Node.js
FROM node:18-alpine

# Asegúrate de que npm esté instalado
RUN apk add --no-cache npm

# Establece el directorio de trabajo
WORKDIR /app

# Copia el package.json y package-lock.json primero
COPY package.json ./ 
# package-lock.json 

# Instala las dependencias
RUN npm install

# Copia el resto del código fuente al contenedor
COPY . .

# Construye la aplicación
RUN npm run build

# Expón el puerto de la aplicación
EXPOSE 5173
EXPOSE 4173

# Comando para iniciar la aplicación en producción
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]
