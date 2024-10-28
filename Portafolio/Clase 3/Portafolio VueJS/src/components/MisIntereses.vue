<script setup>
import { ref } from 'vue';
import FondoLava from './FondoLava.vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
    'Contribución a Proyectos de Código Abierto: Participo activamente en proyectos en GitHub, colaborando con otros desarrolladores para mejorar mis habilidades y aprender de la comunidad.',
    'Exploración de Innovaciones Tecnológicas: Me apasiona investigar y experimentar con tendencias emergentes, como la inteligencia artificial y el desarrollo de aplicaciones web y móviles.',
    'Diseño Gráfico como Hobby: Practico el diseño gráfico en mi tiempo libre, lo que enriquece mi creatividad y aporta una perspectiva fresca a mi trabajo profesional y personal.'
]);

</script>

<template>
    <div class="intereses-contenedor">
        <FondoLava />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
.intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 100%;
    padding: 1rem;
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: black;
    font-size: 1.2rem;
}

.item {
    margin-bottom: 1rem;
    font-weight: bolder;
    color: #2d98e4;
    text-shadow:
        1px 1px 2px rgba(0, 0, 0, 0.7),
        -1px -1px 2px rgba(255, 255, 255, 0.5);
}
</style>