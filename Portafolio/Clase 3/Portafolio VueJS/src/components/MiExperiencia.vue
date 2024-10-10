<script setup>
import { ref } from "vue";
import experiencia1 from '../assets/Experiencia1.gif';
import experiencia2 from '../assets/Experiencia2.gif';

const titulo = "DESARROLLADORA FULLSTACK";
const fecha = "Desde Noviembre 2022 / Septiembre 2024";

const experiencias = ref([
    {
        id: 1,
        gif: experiencia1,
        parrafo: "Formé parte de un equipo en el desarrollo de una aplicación para la Universidad de La Punta, en San Luis."
    },
    {
        id: 2,
        gif: experiencia2,
        parrafo: "Formé parte del grupo 'CTRL-Z' en el desarrollo de una aplicación para una organización similar a un consultorio médico. "
    }
]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <div class="flex-container">
                    <img :src="experiencia.gif" alt="Experiencia" class="imagen" />
                    <p class="parrafo">{{ experiencia.parrafo }}</p>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: #E24A68;
    border-radius: 15px;
    overflow: visible;
    margin: 0;
}

.flex-container {
    display: flex;
    align-items: center; /* Cambia a center para alinear verticalmente */
    gap: 1rem; /* Espacio entre la imagen y el texto */
    margin-bottom: 1rem; /* Espacio entre cada experiencia */
}

.imagen {
    width: 100px; /* Establece un tamaño fijo para las imágenes */
    height: auto; /* Mantiene la relación de aspecto */
}

.titulo {
    font-size: 1.5rem;
    color: black;
    font-weight: bold;
}

.fecha {
    font-size: 1rem;
    color: rgb(42, 41, 41);
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
    list-style-type: none; /* Elimina las viñetas */
    padding: 0; /* Elimina el padding predeterminado */
}

.item {
    padding: 1rem;
}

.parrafo {
    margin: 0;
    font-size: 1.25rem;
    line-height: 1.5;
    word-wrap: break-word;
}
</style>