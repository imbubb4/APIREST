# 🎬 API REST - Catálogo de Películas

Este proyecto es una API RESTful construida con **Django** y **Django REST Framework** como parte del curso de **Desarrollo de Aplicaciones Empresariales**. Permite gestionar películas, directores, actores, géneros, reseñas y listas de favoritos.

---

## 🚀 Funcionalidades principales

- ✅ CRUD completo para:
  - Películas
  - Directores
  - Actores
  - Géneros
- 🔍 Búsqueda de películas por título
- ⭐ Gestión de películas favoritas por usuario
- 📝 Calificación y reseñas de películas
- 📦 Probado con Thunder Client (VS Code)

---

## 🧱 Modelos

- `Pelicula`: título, descripción, fecha de estreno, director, actores, género
- `Director`: nombre
- `Actor`: nombre
- `Genero`: nombre
- `Reseña`: calificación, comentario, película relacionada
- `Favorito`: usuario, película marcada como favorita

FUNCIONAMIENTO PARA THUNDER CLIENT
PELICULA 
http://127.0.0.1:8000/api/peliculas/
{
        "id": 1,
        "titulo": "Inception",
        "descripcion": "Un ladrón que roba secretos mediante los sueños.",
        "fecha_estreno": "2010-07-16",
        "director": 1,
        "genero": 1,
        "actores": [1,2
        ]
    },
DIRECTORES 
http://127.0.0.1:8000/api/directores/

 {
        "id": 1,
        "nombre": "Christopher Nolan"
    },

ACTORES
http://127.0.0.1:8000/api/actores/
 {
        "id": 1,
        "nombre": "Leonardo DiCaprio"
    },

GENEROS
http://127.0.0.1:8000/api/generos/


        "id": 1,
        "nombre": "Ciencia ficción"
    },

RESEÑAS
http://127.0.0.1:8000/api/resenas/
{
        "id": 1,
        "calificacion": 5,
        "comentario": "Una obra maestra, visualmente impactante y emocionante.",
        "pelicula": 1
    }
BUSCAR PELICULAS 
http://127.0.0.1:8000/api/buscar/?q="AQUI VA EL NOMBRE DE LA PELI NOMAS"
FAVORITOS
http://127.0.0.1:8000/api/favoritos/
{
        "id": 1,
        "usuario": "bubbita",
        "pelicula": 2
    }
---

## 🛠️ Instalación y ejecución local
### 1. Clona el repositorio

```bash
git clone https://github.com/imbubb4/APIREST.git
cd APIREST

