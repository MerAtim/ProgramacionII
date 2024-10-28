<script setup>
import { ref } from "vue";
import imgULP2 from '../assets/App ULP JAVA ii.png';
import CAC from '../assets/CAC.png';
import gitNube from '../assets/GitNube.png';
import imgMasSalud1 from '../assets/Mas Salud.png';


const proyectos = ref([
    {
        id: 1,
        nombre: "ULP Universidad",
        descripcion: "Creamos una aplicacion de gestión academica. Esta aplicación, construida en Java con una interfaz de usuario en Java Swing, se conecta a una base de datos para gestionar el alta, baja y modificación de cátedras, calificaciones y alumnos. Mi participación incluyó tanto el diseño de la interfaz como la implementación de funcionalidades críticas, contribuyendo a optimizar la gestión académica.",
        imagenes: [imgULP2],
        github: "https://github.com/MerAtim/Proyecto-ULP-GRUPO-67"
    },
    {
        id: 2,
        nombre: "Mas Salud",
        descripcion: "Creamos una aplicacion de gestion medica. Este proyecto fue desarrollado en Java utilizando Java Swing para la interfaz gráfica y está conectado a una base de datos. El proyecto incluyó la realización de pruebas, diseño de la interfaz, selección de colores e imágenes, así como la implementación del patrón MVC, gestión de reuniones para coordinar el desarrollo y pruebas, similar a la metodología SCRUM. La aplicación permite la gestión de afiliados, prestadores, especialidades y órdenes médicas.",
        imagenes: [imgMasSalud1],
        github: "https://github.com/MerAtim/clonMasSalud21-10"
    },
    {
        id: 3,
        nombre: "CAC Turismo",
        descripcion: "Creamos una pagina Web de Turismo Argentino. Este proyecto fue desarrollado en Java el Backend y en HTML, CSS y JavaScript para el Frontend. Tambien esta contectado a una base de datos que alberga lugares turisticos con su descripcion e imagenes. Se puede gestionar en la pagina web el Alta, Baja y Modificar de cada lugar turístico.",
        imagenes: [CAC],
        github: "https://github.com/MerAtim/CAC-Turismo"
    },
]);
</script>

<template>
    <div class="galeria">
        <div class="proyecto" v-for="proyecto in proyectos" :key="proyecto.id">
            <div class="proyecto-info">
                <h3>{{ proyecto.nombre }}</h3>
                <p>{{ proyecto.descripcion }}</p>
                <div class="imagenes">
                    <img v-for="(img, index) in proyecto.imagenes" :key="index" :src="img" alt="Proyecto" class="proyecto-imagen"/>
                </div>
            </div>
            <div class="proyecto-links">
                <a :href="proyecto.github" target="_blank">
                    <img :src="gitNube" alt="GitHub" class="git-button" />
                    <p class="mensaje">Link al proyecto en Github</p>
                </a>
            </div>
        </div>
    </div>
</template>


<style>
.galeria {
    width: 100%;
    max-width: 1200px; /* Ajusta según lo que necesites */
    margin: 0 auto; /* Centra el contenedor */
    display: flex;
    flex-wrap: wrap;
    gap: 20px; /* Espacio entre proyectos */
    padding: 10px;
    justify-content: center;
    background-color: #E24A68;
    border-radius: 8px;
}

.proyecto {
    display: flex;
    flex-direction: column;
    border: 2px solid #ddd;
    border-radius: 8px;
    background-color: #d294b3;
    flex: 1 1 390px; /* Proyectos ocupan mínimo 400px, ajustable */
    max-width: 400px; /* Ajusta según necesites */
    margin-bottom: 20px; /* Espacio entre las tarjetas */
}

.proyecto-info {
    padding: 15px;
    text-align: center;
    flex-grow: 1; /* Permite que este contenedor crezca y ocupe el espacio disponible */
}

.proyecto-links {
    display: flex;
    flex-direction: column; /* Cambia la dirección a columna */
    align-items: center; /* Centra los elementos horizontalmente */
    margin-top: 10px;
    padding-bottom: 15px; /* Espacio al fondo de la tarjeta */
}

.proyecto-links a {
    display: flex;
    flex-direction: column; /* Cambia la dirección a columna */
    align-items: center; /* Centra el contenido horizontalmente */
    text-decoration: none; /* Opcional: elimina el subrayado */
    border: none; /* Elimina el borde del enlace */
    outline: none; /* Elimina el contorno al hacer foco */
}

.proyecto-imagen {
    width: 100%; /* Ajusta el ancho al 100% del contenedor */
    height: auto; /* Mantiene la proporción de la imagen */
    justify-content: center;
    border-radius: 10px;
}

.proyecto-info h3 {
    margin: 10px 0;
    font-size: 1.3em;
    color: #333;
    font-weight: bolder;
}

.proyecto-info p {
    margin: 10px 0;
    font-size: 1em;
    color: #666;
}

.git-button {
    width: 100px; /* Ajusta el tamaño según sea necesario */
    height: auto; /* Mantiene la proporción */
    cursor: pointer; /* Cambia el cursor al pasar el ratón */
    background: none; /* Elimina el fondo */
    padding: 0; /* Elimina el padding */
    transition: all 0.3s; /* Agrega una transición suave */
}

.proyecto-links a:hover .git-button {
    /* Aquí puedes agregar efectos al pasar el ratón */
    transform: scale(1.1); /* Ejemplo: aumentar un poco el tamaño */
}

.imagenes {
    display: flex;
    flex-direction: column; /* Cambia la dirección de las imágenes */
    align-items: center; /* Alinea las imágenes al centro */
    gap: 10px; /* Espacio entre imágenes */
    justify-content: center;
}

.mensaje{
    font-size: smaller;
    font-weight: bold;
}

@media (max-width: 768px) {
    .galeria {
        padding: 5px;
    }

    .proyecto {
        max-width: 100%; /* Ocupa toda la pantalla en dispositivos pequeños */
        margin-bottom: 15px;
    }

    .proyecto-info h3 {
        font-size: 1.2em;
    }

    .proyecto-info p {
        font-size: 0.9em;
    }

    .git-button {
        width: 80px; /* Ajusta el tamaño del botón de GitHub */
    }
}
</style>