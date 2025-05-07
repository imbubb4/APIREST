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

---

## 🛠️ Instalación y ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/imbubb4/APIREST.git
cd APIREST
