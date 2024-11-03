<script setup>
import { ref, onMounted } from 'vue';
import DatosPersonales from './components/DatosPersonales.vue';
import MiEducacion from './components/MiEducacion.vue';
import NavBar from './components/NavBar.vue';
import MiExperiencia from './components/MiExperiencia.vue';
import MisProyectos from './components/MisProyectos.vue';
import MisHabilidades from './components/MisHabilidades.vue';
import MisIntereses from './components/MisIntereses.vue';
import ParticulasComponente from './components/ParticulasComponente.vue';
 // Importa el componente de partículas

// Importa las imágenes GIF
import educacionGif from '@/assets/Educacion.gif';
import experienciaGif from '@/assets/Experiencia.gif';
import proyectosGif from '@/assets/Proyecto.gif';
import habilidadesGif from '@/assets/Habilidades.gif';
import interesesGif from '@/assets/Intereses.gif';

// Estado para las secciones
const showSection = ref({
    educacion: false,
    experiencia: false,
    proyectos: false,
    habilidades: false,
    intereses: false
});

// Función para alternar la visibilidad de la sección
const toggleSection = (section) => {
    showSection.value[section] = !showSection.value[section];
};

// Computar si la pantalla es amplia
const isWideScreen = ref(window.innerWidth >= 768);

// Agregar un event listener para el resize
const updateWidth = () => {
    isWideScreen.value = window.innerWidth >= 768;
};

onMounted(() => {
    window.addEventListener('resize', updateWidth);
});
</script>

<template>
    <header id="top">
        <NavBar />
    </header>
    <main>
        <ParticulasComponente /> <!-- Añade aquí el componente de partículas -->
        <DatosPersonales />
        <div class="contenedor-principal">
            <section id="educacion">
                <h2 @click="toggleSection('educacion')" class="toggle-header">
                    Educación - Cursos
                    <img :src="educacionGif" alt="Educación" class="gif-icon" />
                </h2>
                <div v-if="showSection.educacion && !isWideScreen" class="section-content">
                    <MiEducacion />
                </div>
                <div v-if="isWideScreen" class="section-content">
                    <MiEducacion />
                </div>
            </section>
            <section id="experiencia">
                <h2 @click="toggleSection('experiencia')" class="toggle-header">
                    Experiencia
                    <img :src="experienciaGif" alt="Experiencia" class="gif-icon" />
                </h2>
                <div v-if="showSection.experiencia && !isWideScreen" class="section-content">
                    <MiExperiencia />
                </div>
                <div v-if="isWideScreen" class="section-content">
                    <MiExperiencia />
                </div>
            </section>
            <section id="proyectos">
                <h2 @click="toggleSection('proyectos')" class="toggle-header">
                    Proyectos
                    <img :src="proyectosGif" alt="Proyectos" class="gif-icon" />
                </h2>
                <div v-if="showSection.proyectos && !isWideScreen" class="section-content">
                    <MisProyectos />
                </div>
                <div v-if="isWideScreen" class="section-content">
                    <MisProyectos />
                </div>
            </section>
            <section id="habilidades">
                <h2 @click="toggleSection('habilidades')" class="toggle-header">
                    Habilidades
                    <img :src="habilidadesGif" alt="Habilidades" class="gif-icon" />
                </h2>
                <div v-if="showSection.habilidades && !isWideScreen" class="section-content">
                    <MisHabilidades />
                </div>
                <div v-if="isWideScreen" class="section-content">
                    <MisHabilidades />
                </div>
            </section>
            <section id="intereses">
                <h2 @click="toggleSection('intereses')" class="toggle-header">
                    Intereses
                    <img :src="interesesGif" alt="Intereses" class="gif-icon" />
                </h2>
                <div v-if="showSection.intereses && !isWideScreen" class="section-content">
                    <MisIntereses />
                </div>
                <div v-if="isWideScreen" class="section-content">
                    <MisIntereses />
                </div>
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
    width: 30px; /* Tamaño uniforme para todos los íconos */
    height: 30px; /* Mantiene el mismo tamaño para todos */
    margin-left: 10px; /* Espacio entre el texto y la imagen */
    vertical-align: middle; /* Alineación vertical */
    border-radius: 10px;
}

header {
    position: fixed; /* Fija la cabecera */
    top: 0; /* Alinea al top */
    left: 0; /* Alinea a la izquierda */
    right: 0; /* Alínea a la derecha */
    z-index: 1000; /* Asegúrate de que esté sobre otros elementos */
}

main {
    padding-top: 100px; /* Espacio para el navbar fijo */
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
    color: lightseagreen;
    cursor: pointer; /* Cambia el cursor al pasar sobre el encabezado */
}

.toggle-header {
    display: flex;
    align-items: center;
}

/* Estilos para pantallas grandes */
@media (min-width: 768px) {
    .section-content {
        display: block; /* Muestra el contenido siempre en pantallas grandes */
    }

    .toggle-header {
        cursor: default; /* Cambia el cursor en pantallas grandes */
    }

    h2:hover {
        text-decoration: none; /* Sin efecto de hover en pantallas grandes */
    }
}

/* Estilos para pantallas pequeñas */
@media (max-width: 767px) {
    .section-content {
        display: none; /* Oculta el contenido por defecto en pantallas pequeñas */
    }

    .section-content.active {
        display: block; /* Muestra el contenido si está activo */
    }
}
</style>