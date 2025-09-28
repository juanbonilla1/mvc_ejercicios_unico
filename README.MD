# MVC Ejercicios Único
Aplicación **Flask** que agrupa 8 ejercicios independientes en un solo proyecto, cada uno con su propio módulo y rutas. Incluye un contenedor **Docker** para despliegue rápido en **Linux**, **Windows** y **macOS**.
## 🚀 Requisitos previos
- **Docker** instalado:  
  - [Linux](https://docs.docker.com/engine/install/)  
  - [Windows (Docker Desktop)](https://docs.docker.com/desktop/install/windows/)  
  - [macOS (Docker Desktop)](https://docs.docker.com/desktop/install/mac/)
> **Consejo para Linux**  
> Añade tu usuario al grupo docker (opcional pero recomendado):  
> ```bash
> sudo usermod -aG docker $USER
> ```  
> Luego cierra sesión y vuelve a iniciar.
## 🛠️ Instalación y despliegue con Docker
Clona este repositorio en cualquier sistema y construye la imagen Docker. Los comandos varían ligeramente según el sistema operativo:
### Linux / macOS (terminal Bash o Zsh)
```bash
git clone https://github.com/juanbonilla1/mvc_ejercicios_unico.git
cd mvc_ejercicios_unico
docker build -t mvc_ejercicios_unico .
docker run -d -p 5000:5000 mvc_ejercicios_unico

git clone https://github.com/juanbonilla1/mvc_ejercicios_unico.git
cd mvc_ejercicios_unico
docker build -t mvc_ejercicios_unico .
docker run -d -p 5000:5000 mvc_ejercicios_unico
