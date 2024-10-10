<script setup>
import DatosPersonales from './components/DatosPersonales.vue';
import MiEducacion from './components/MiEducacion.vue';
import NavBar from './components/NavBar.vue';
import MiExperiencia from './components/MiExperiencia.vue';
import MisProyectos from './components/MisProyectos.vue';
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
                <!-- Contenido de habilidades aquí -->
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
    display: flex; /* O 'grid', según lo que prefieras */
    flex-direction: column; /* Alinea los elementos en una columna */
    align-items: center; /* Centra los elementos horizontalmente */
    gap: 2rem; /* Espaciado entre las secciones */
}
</style>

