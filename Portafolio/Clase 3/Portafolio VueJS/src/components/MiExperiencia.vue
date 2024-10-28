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
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
}

.imagen {
    width: 100px;
    height: auto;
}

.titulo {
    font-size: 1.5rem;
    color: black;
    font-weight: bold;
}

.fecha {
    font-size: 1.2rem;
    color: rgb(42, 41, 41);
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
    list-style-type: none;
    padding: 0;
}

.item {
    padding: 1rem;
}

.parrafo {
    margin: 0;
    font-size: 1.1rem;
    line-height: 1.4;
    word-wrap: break-word;
    font-weight: 550;
}

/* Ajustes para pantallas pequeñas */
@media (max-width: 768px) {
    .flex-container {
        flex-direction: column;
        align-items: flex-start;
    }

    .imagen {
        width: 80px; /* Reduce el tamaño de la imagen */
    }

    .parrafo {
        font-size: 1rem; /* Ajuste de tamaño de texto en pantallas chicas */
    }

    .card {
        padding: 1rem; /* Reduce el padding en pantallas pequeñas */
    }
    .titulo, .fecha{
        font-size: 20px;
    }
}
</style>
