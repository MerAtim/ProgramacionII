<script setup>
import DatosPersonales from './components/DatosPersonales.vue';
import MiEducacion from './components/MiEducacion.vue';
import NavBar from './components/NavBar.vue';
import MiExperiencia from './components/MiExperiencia.vue';
import MisProyectos from './components/MisProyectos.vue';
import MisHabilidades from './components/MisHabilidades.vue';
</script>

<template>
    <header>
        <NavBar />
        <DatosPersonales />
    </header>
    <main>
        <div class="contenedor-principal">
            <section id="educacion">
                <h2>Educación - Cursos</h2>
                <MiEducacion />
            </section>
            <section id="experiencia">
                <h2>Experiencia</h2>
                <MiExperiencia />
            </section>
            <section id="proyectos">
                <h2>Proyectos</h2>
                <MisProyectos />
            </section>
            <section id="habilidades">
                <h2>Habilidades</h2>
                <MisHabilidades />
            </section>
            <section id="intereses">
                <h2>Intereses</h2>
                <!-- Contenido de intereses aquí -->
            </section>
        </div>
    </main>
</template>

<style scoped>
.contenedor-principal {
    display: flex; 
    flex-direction: column; 
    align-items: center;
    gap: 2rem; 
}
</style>

