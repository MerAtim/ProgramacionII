<script setup>
import { ref } from "vue";

const titulo = "DESARROLLADORA FULLSTACK";
const fecha = "Desde Noviembre 2022 / Septiembre 2024";
import appULPJava from '../assets/App ULP JAVA.png';
import appULPJavaII from '../assets/App ULP JAVA ii.png';
import masSalud from '../assets/Mas Salud.jpg';
import masSalud1 from '../assets/Mas salud 1.jpg';

const experiencias = ref([
    {
        id: 1,
        src1: appULPJava,
        src2: appULPJavaII,
        parrafo: "Formé parte de un equipo reducido en el desarrollo de una aplicación para la Universidad de La Punta, en San Luis. Esta aplicación, construida en Java con una interfaz de usuario en Java Swing, se conecta a una base de datos para gestionar el alta, baja y modificación de cátedras, calificaciones y alumnos. Mi participación incluyó tanto el diseño de la interfaz como la implementación de funcionalidades críticas, contribuyendo a optimizar la gestión académica."
    },
    {
        id: 2,
        src1: masSalud,
        src2: masSalud1,
        parrafo: "Formé parte de un equipo reducido llamado 'CTRL-Z' en el desarrollo de una aplicación para una organización similar a un consultorio médico. Este proyecto fue desarrollado en Java utilizando Java Swing para la interfaz gráfica y está conectado a una base de datos. El proyecto incluyó la realización de pruebas, diseño de la interfaz, selección de colores e imágenes, así como la implementación del patrón MVC. También gestioné reuniones del equipo para coordinar el desarrollo y las pruebas, similar a la metodología SCRUM. La aplicación permite la gestión de afiliados, prestadores, especialidades y órdenes médicas."
    }
]);

</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <p class="parrafo">{{ experiencia.parrafo }}</p>
                <div class="imagenes">
                    <img class="imagen" :src="experiencia.src1" width="100%" :alt="Desarrollo">
                    <img class="imagen" :src="experiencia.src2" width="50%" :alt="Desarrollo">
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

.imagenes {
    display: flex;
    flex-direction: row;
    gap: 1rem;
    margin-top: 1rem;
}

.imagen{
    width: 45%;
    height: auto;
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
}

.item {
    padding: 1rem;
    gap: 1rem;
}
.parrafo{
    margin: 0;
    font-size: 1rem;
    line-height: 1.5;
    word-wrap: break-word;
}
</style>