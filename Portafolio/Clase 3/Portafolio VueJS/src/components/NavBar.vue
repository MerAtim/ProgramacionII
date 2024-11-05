<template>
  <nav class="navbar">
      <div class="navbar-brand">
          <button class="navbar-burger" @click="toggleMenu">☰</button>
      </div>
      <div :class="['navbar-menu', { 'is-active': isMenuActive }]">
          <ul class="nav-list">
              <li v-for="nav in navegacion" :key="nav.id" class="nav-item">
                  <a :href="nav.enlace">{{ nav.nombre }}</a>
              </li>
          </ul>
      </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';

const navegacion = ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' },
]);

const isMenuActive = ref(false);

function toggleMenu() {
  isMenuActive.value = !isMenuActive.value;
}
</script>

<style>
.navbar {
  background-color: #E24A68;
  color: #000000;
  padding: 0.5rem 1rem;
  align-items: center;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  position: fixed;
  top: 0;
  z-index: 2;
  width: 75%;
  margin-top: 1%;
}

/* Mueve el botón de hamburguesa a la derecha */
.navbar-burger {
  display: none;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  margin-left: auto; /* Alinea la hamburguesa a la derecha */
}

.navbar-menu {
  display: flex;
  justify-content: flex-end;
}

.nav-list {
  display: flex;
  padding: 0;
  margin: 0;
  list-style: none;
}

.nav-item {
  margin-right: 0.5rem;
}

a {
  font-family: Montserrat, sans-serif;
  border: 1px solid;
  border-color: #E24A68;
  color: black;
  font-weight: bold;
  border-radius: 5px;
  text-decoration: none;
  transition: 0.4s;
  padding: 5px;
}

a:hover {
  background-color: hsla(0, 0%, 100%, 0.2);
}

/* Estilos responsivos para dispositivos móviles */
@media (max-width: 768px) {
  .navbar-burger {
      display: block;
  }

  .navbar-menu {
      display: none;
      flex-direction: column;
      align-items: flex-start;
      width: 80%; /* Ajusta el ancho del menú desplegable */
      max-width: 250px; /* Ancho máximo para el menú */
      background-color: #E24A68;
      position: absolute;
      top: 60px;
      left: 1;
      max-height: 300px;
      overflow-y: auto;
      transition: max-height 0.3s ease;
      border-radius: 0 0 10px 10px;
  }

  .navbar-menu.is-active {
      display: flex;
  }

  .nav-list {
      flex-direction: column;
      width: 100%;
  }

  .nav-item {
      margin-bottom: 1rem;
      margin-right: 0;
  }
  .navbar{
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
  }
}
</style>