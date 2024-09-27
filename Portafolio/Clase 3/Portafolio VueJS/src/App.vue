<script setup>
import DatosPersonales from './components/DatosPersonales.vue';
import MiEducacion from './components/MiEducacion.vue';
import NavBar from './components/NavBar.vue';
import MiExperiencia from './components/MiExperiencia.vue';
</script>

<template>
    <header>
        <NavBar />
        <DatosPersonales />
    </header>
<main>
    <section id="educacion"><h2>Educación - Cursos</h2>
        <MiEducacion />
    </section>
    <section id="experiencia"><h2>Experiencia</h2></section>
    <MiExperiencia />
    <section id="proyectos"><h2>Proyectos</h2></section>
    <section id="habilidades"><h2>Habilidades</h2></section>
    <section id="intereses"><h2>Intereses</h2></section>
</main>
</template>