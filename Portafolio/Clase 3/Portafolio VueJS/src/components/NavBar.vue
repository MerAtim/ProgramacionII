<template>
    <nav class="navbar">
            <div class="navbar-menu">
                <ul>
                    <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="nav-item" >{{nav.nombre}}</a>
                </ul>
            </div>
</nav>
</template>

<script setup>
import { ref } from 'vue';
const navegacion= ref([
    {id:1, nombre:'Educación', enlace:'#educacion'},
    {id:2, nombre:'Experiencia', enlace:'#experiencia'},
    {id:3, nombre:'Proyectos', enlace:'#proyectos'},
    {id:4, nombre:'Habilidades', enlace:'#habilidades'}
]);
</script>

<style>
.navbar {
    background-color:#E24A68;
    color: #000000;
    padding: 0.5rem 1rem;
    align-items: center;
}
.navbar-item {
    color: #000000;
    text-decoration: none;
    margin-right: 1rem;
}
.navbar-menu {
display: flex;
justify-content: flex-end;
}
.nav-list{
list-style: none;
}
a {
font-family: Montserrat, sans-serif;
border: 1px solid ;
border-color: #E24A68;
color: black;
font-weight: bold;
border-radius: 5px;
  /* Elimina la subrayado de los enlaces y elementos con clase "green" */
text-decoration: none;
  /* Añade una transición suave para los cambios de estilo */
transition: 0.4s;
  /* Añade padding alrededor del contenido */
padding: 5px;
}

a:hover {
    /* Cambia el color de fondo al pasar el mouse sobre un enlace */
    background-color: hsla(0, 0%, 100%, 0.2);
}

@media (max-width: 768px) {
.navbar-menu {
display: flex;
justify-content: flex-end;
width: 100%;
}
}
</style>
