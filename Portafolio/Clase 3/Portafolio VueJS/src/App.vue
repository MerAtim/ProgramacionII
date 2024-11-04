<script setup>
import DatosPersonales from './components/DatosPersonales.vue';
import MiEducacion from './components/MiEducacion.vue';
import NavBar from './components/NavBar.vue';
import MiExperiencia from './components/MiExperiencia.vue';
import MisProyectos from './components/MisProyectos.vue';
import MisHabilidades from './components/MisHabilidades.vue';
import MisIntereses from './components/MisIntereses.vue';

// Importa las imágenes GIF
import educacionGif from '@/assets/Educacion.gif';
import experienciaGif from '@/assets/Experiencia.gif';
import proyectosGif from '@/assets/Proyecto.gif';
import habilidadesGif from '@/assets/Habilidades.gif';
import interesesGif from '@/assets/Intereses.gif';
</script>

<template>
    <header id="top">
        <NavBar />
        <DatosPersonales />
    </header>
    <main>
        <div class="contenedor-principal">
            <section id="educacion">
                <h2>
                    Educación - Cursos
                    <img :src="educacionGif" alt="Educación" class="gif-icon" />
                </h2>
                <MiEducacion />
            </section>
            <section id="experiencia">
                <h2>
                    Experiencia
                    <img :src="experienciaGif" alt="Experiencia" class="gif-icon" />
                </h2>
                <MiExperiencia />
            </section>
            <section id="proyectos">
                <h2>
                    Proyectos
                    <img :src="proyectosGif" alt="Proyectos" class="gif-icon" />
                </h2>
                <MisProyectos />
            </section>
            <section id="habilidades">
                <h2>
                    Habilidades
                    <img :src="habilidadesGif" alt="Habilidades" class="gif-icon" />
                </h2>
                <MisHabilidades />
            </section>
            <section id="intereses">
                <h2>
                    Intereses
                    <img :src="interesesGif" alt="Intereses" class="gif-icon" />
                </h2>
                <MisIntereses />
            </section>
        </div>
    </main>
    <footer>
        <a class="linkFooter" href="#top">Inicio</a>
        <p>Maria Mercedes Atim - Portafolio web - &copy; 2024</p>
    </footer>
</template>

<style scoped>
.gif-icon {
    width: 150px; /* Ajusta el tamaño según necesites */
    height: auto; /* Mantiene la proporción */
    margin-left: 10px; /* Espacio entre el texto y la imagen */
    vertical-align: middle; /* Alineación vertical */
    border-radius: 10px;
}

footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    font-size: 1.3rem;
    background-color: #E24A68;
    border-top: 2px solid #eaeaea;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    border-radius: 20px;
}

.linkFooter {
    color: #007BFF;
    text-decoration: none;
    transition: color 0.3s;
}

.linkFooter:hover {
    color: #0056b3;
    text-decoration: underline;
}

p {
    margin-top: 1rem;
    color: #171717;
    text-align: center;
    font-weight: bolder;
    font-size: smaller;
}

.contenedor-principal {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

section {
    width: 100%;
    padding: 2rem 1.5rem;
    margin: 0;
}

h2 {
    font-weight: bold;
    color: lightseagreen
}
</style>
