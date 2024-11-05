<script setup>
import { ref } from 'vue';
import primerTramo from '@/assets/PrimerTramo.png';
import segundoTramo from '@/assets/SegundoTramo.png';
import tercerTramo from '@/assets/TercerTramo.png';
import testing1 from '@/assets/Testing1.png';
import testing2 from '@/assets/TestingUtn.png';
import java from '@/assets/JavaCAC.png';
import MiModal from './MiModal.vue';
const fechaColor = ref([]);
fechaColor.value = [
{color: '#41516c'},
{color: '#FBCA3E'},
{color: '#E24A68'},
{color: '#1B5F8C'},
{color: '#4CADAD'}
];

const educacion = ref([]);
educacion.value = [
{fecha: "2024", title: "Tecnicatura Universitaria en Programacion", descripcion: "Durante esta formación, adquirí conocimientos fundamentales en el desarrollo de software, incluyendo lenguajes de programación como Java, Python y JavaScript. Aprendí sobre estructuras de datos, algoritmos, bases de datos y metodologías de desarrollo ágil. Además, desarrollé habilidades en el trabajo en equipo y la resolución de problemas, lo que me permitió participar en proyectos prácticos que simularon entornos laborales reales. Esta formación me preparó para enfrentar desafíos en el campo de la tecnología y la programación."},
{fecha: "2024", title: "Desarrollo FullStack Java", descripcion: "En este curso, adquirí habilidades en el desarrollo de aplicaciones web utilizando Java en el backend y tecnologías como HTML, CSS y JavaScript en el frontend. Aprendí a trabajar con frameworks como Spring y Hibernate, así como a diseñar y gestionar bases de datos con MySQL.", enlace: java},
{fecha: "2023", title: "Quality Assurance Manual", descripcion: "En estos cursos, adquirí conocimientos fundamentales en aseguramiento de la calidad de software. Aprendí sobre metodologías de prueba, diseño de casos de prueba, ejecución de pruebas manuales y documentación de resultados. Me familiaricé con herramientas de seguimiento de errores y prácticas de gestión de calidad, lo que me permitió desarrollar habilidades críticas para garantizar que las aplicaciones cumplan con los estándares de calidad y funcionalidad.", enlace: "", enlaces: [
            { texto: "Diploma 1", enlace: testing1 },
            { texto: "Diploma 2", enlace: testing2 }
        ]},
{fecha: "2022", title: "Fundamentos de Programacion y Desarrollo FullStack Java", descripcion: "Este curso de un año me brindó una sólida base en programación. Comenzamos con dos meses de fundamentos de programación utilizando pseudocódigo, lo que me ayudó a desarrollar habilidades lógicas esenciales. Durante los siguientes diez meses, profundicé en Java y aprendí sobre bases de datos con MySQL y el entorno de desarrollo XAMPP. Como proyecto final, desarrollamos una aplicación con interfaz gráfica de usuario utilizando Java Swing, lo que me permitió aplicar mis conocimientos en un entorno práctico y real.", enlaces: [
            { texto: "Primer Tramo Java FullStack", enlace: primerTramo },
            { texto: "Segundo Tramo Java FullStack", enlace: segundoTramo },
            { texto: "Tercer Tramo Java FullStack", enlace: tercerTramo }
        ]},
];
const isModalOpen = ref(false);
const currentImage = ref('');

function openModal(imageUrl) {
  currentImage.value = imageUrl;
  isModalOpen.value = true;
}

function closeModal() {
  isModalOpen.value = false;
  currentImage.value = '';
}
</script>
<template>
  <div>
    <ul>
      <li v-for="(item, index) in educacion" :key="index" :style="{ '--fecha-color': fechaColor[index].color }">
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="title">{{ item.title }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
        <div>
          <span v-if="item.enlace">Diploma: </span>
          <a v-if="item.enlace" class="enlace" @click.prevent="openModal(item.enlace)">Ver Diploma</a>
          <div v-if="item.enlaces && item.enlaces.length">
            <span>Diplomas: </span>
            <span v-for="(enlace, enlaceIndex) in item.enlaces" :key="enlaceIndex">
              <a v-if="enlace.enlace" class="enlace" @click.prevent="openModal(enlace.enlace)">{{ enlace.texto }}</a>
              <span v-if="enlaceIndex < item.enlaces.length - 1">, </span>
            </span>
          </div>
        </div>
      </li>
    </ul>

    <!-- Componente Modal -->
    <MiModal :isOpen="isModalOpen" :image="currentImage" :close="closeModal" />
  </div>
</template>




<style scoped>
/* Reseteo de estilos básicos para todos los elementos y pseudo-elementos */
*,
*::before,
*::after {
  margin: 0; /* Elimina el margen predeterminado */
  padding: 0; /* Elimina el padding predeterminado */
  box-sizing: border-box; /* Incluye el padding y el borde en el tamaño total del elemento */
}

/* Estilo para el cuerpo de la página */
body {
  font-family: Montserrat, sans-serif;
  --color: rgba(30, 30, 30); /* Variable para el color de texto */
  --bgColor: rgba(245, 245, 245); /* Variable para el color de fondo */
  min-height: 100vh; /* Asegura que el cuerpo ocupe al menos el 100% de la altura de la ventana */
  display: grid; /* Utiliza el modelo de caja de cuadrícula */
  align-content: center; /* Centra verticalmente el contenido dentro de la cuadrícula */
  gap: 2rem; /* Espaciado entre los elementos de la cuadrícula */
  padding: 1rem; /* Espaciado interno alrededor del cuerpo */
  color: var(--color); /* Aplica el color de texto definido en la variable */
  background: var(--bgColor); /* Aplica el color de fondo definido en la variable */
}

/* Estilos para la lista */
ul {
  margin-top: 2rem;
  --col-gap: 2rem; /* Espacio entre las columnas de la cuadrícula */
  --row-gap: 2rem; /* Espacio entre las filas de la cuadrícula */
  --line-w: 0.25rem; /* Ancho de la línea que conecta los elementos de la lista */
  display: grid; /* Usa un layout de cuadrícula */
  grid-template-columns: var(--line-w) 1fr; /* Define las columnas de la cuadrícula: la primera es la línea y la segunda es el contenido */
  grid-auto-columns: max-content; /* Las columnas se ajustan automáticamente al contenido */
  column-gap: var(--col-gap); /* Espacio entre las columnas */
  list-style: none; /* Elimina las viñetas predeterminadas de la lista */
  width: min(50rem, 80%); /* Limita el ancho de la lista al mínimo entre 50rem y el 80% del ancho de la ventana */
  margin-inline: 20px; /* Centra la lista horizontalmente */
}

/* Estilo para la línea vertical que conecta los elementos de la lista */
ul::before {
  content: ""; /* Elemento vacío para crear la línea */
  grid-column: 1; /* Coloca la línea en la primera columna de la cuadrícula */
  grid-row: 1 / span 20; /* La línea se extiende sobre varias filas */
  background: rgb(225, 225, 225); /* Color de la línea */
  border-radius: calc(var(--line-w) / 2); /* Bordes redondeados para la línea */
}

/* Estilo para los elementos de la lista que no son el último */
ul li:not(:last-child) {
  margin-bottom: var(--row-gap); /* Espacio entre los elementos de la lista */
}

/* Estilo para cada ítem de la lista */
ul li {
  grid-column: 2; /* Coloca el contenido en la segunda columna de la cuadrícula */
  --inlineP: 1.5rem; /* Espacio interno horizontal dentro de cada ítem */
  margin-inline: var(--inlineP); /* Margen horizontal para los ítems */
  grid-row: span 2; /* Cada ítem ocupa dos filas en la cuadrícula */
  display: grid; /* Usa un layout de cuadrícula dentro de cada ítem */
  grid-template-rows: min-content min-content min-content; /* Define tres filas de altura mínima */
}

/* Estilo para la fecha dentro de cada ítem */
ul li .fecha {
  --dateH: 3rem; /* Altura de la sección de la fecha */
  height: var(--dateH); /* Aplica la altura definida */
  margin-inline: calc(var(--inlineP) * -1); /* Ajusta el margen horizontal para que la fecha sobresalga */
  text-align: center; /* Centra el texto dentro de la fecha */
  background-color: var(--fecha-color); /* Color de fondo, usando una variable personalizada */
  color: white; /* Color del texto en la fecha */
  font-size: 1.25rem; /* Tamaño del texto */
  font-weight: 700; /* Hace el texto en negrita */
  display: grid; /* Usa un layout de cuadrícula */
  place-content: center; /* Centra el contenido de la fecha */
  position: relative; /* Posiciona la fecha relativa a su contenedor */
  border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2); /* Bordes redondeados para la fecha */
}

/* Estilo para la parte inferior de la fecha, que parece un triángulo */
ul li .fecha::before {
  content: ""; /* Elemento vacío para crear el triángulo */
  width: var(--inlineP); /* Ancho igual al espacio interno definido */
  aspect-ratio: 1; /* Mantiene una relación de aspecto 1:1 para crear un cuadrado */
  background: var(--fecha-color); /* Usa el color de fondo de la fecha */
  background-image: linear-gradient(rgba(0, 0, 0, 0.2) 100%, transparent); /* Aplica un degradado sutil para dar un efecto de sombra */
  position: absolute; /* Posiciona el triángulo respecto al contenedor de la fecha */
  top: 100%; /* Coloca el triángulo justo debajo de la fecha */
  clip-path: polygon(0 0, 100% 0, 0 100%); /* Recorta el cuadrado para convertirlo en un triángulo */
  right: 0; /* Alinea el triángulo a la derecha de la fecha */
}

/* Estilo para el círculo que conecta la fecha con la línea */
ul li .fecha::after {
  content: ""; /* Elemento vacío para crear el círculo */
  position: absolute; /* Posiciona el círculo respecto al contenedor de la fecha */
  width: 1rem; /* Ancho del círculo */
  aspect-ratio: 1; /* Mantiene una relación de aspecto 1:1 para crear un círculo */
  background: var(--bgColor); /* Color de fondo, utilizando la variable definida */
  border: 0.3rem solid var(--fecha-color); /* Borde del círculo, con el color de la fecha */
  border-radius: 50%; /* Hace que el elemento sea un círculo perfecto */
  top: 50%; /* Centra verticalmente el círculo dentro del contenedor de la fecha */
  transform: translate(50%, -50%); /* Ajusta la posición del círculo para alinearlo correctamente */
  right: calc(100% + var(--col-gap) + var(--line-w) / 2); /* Coloca el círculo a la izquierda de la línea */
}

/* Estilos para el título y la descripción dentro de cada ítem */
ul li .title,
ul li .descripcion {
  background: var(--bgColor); /* Fondo del título y la descripción, usando la variable definida */
  position: relative; /* Posiciona los elementos relativos a su contenedor */
  padding-inline: 1.5rem; /* Espaciado interno horizontal */
}

ul li .title {
  overflow: hidden; /* Oculta cualquier contenido que se desborde */
  padding-block-start: 1.5rem; /* Espaciado interno superior */
  padding-block-end: 1rem; /* Espaciado interno inferior */
  font-weight: 500; /* Hace el texto del título un poco más grueso */
}

ul li .descripcion {
  padding-block-end: 1.5rem; /* Espaciado interno inferior */
  font-weight: 300; /* Hace el texto de la descripción más delgado */
}

/* Estilos para las sombras debajo del título y la descripción */
ul li .title::before,
ul li .descripcion::before {
  content: ""; /* Elemento vacío para crear la sombra */
  position: absolute; /* Posiciona la sombra respecto al contenedor del título o descripción */
  width: 90%; /* Ancho de la sombra */
  height: 0.5rem; /* Altura de la sombra */
  left: 50%; /* Centra la sombra horizontalmente */
  border-radius: 50%; /* Bordes redondeados para la sombra */
  filter: blur(4px); /* Aplica un desenfoque para hacer la sombra más suave */
  transform: translate(-50%, 50%); /* Ajusta la posición para centrar la sombra */
}

ul li .title::before {
  bottom: calc(100% + 0.125rem); /* Coloca la sombra debajo del título */
}

ul li .descripcion::before {
z-index: -1; /* Coloca la sombra detrás del contenido */
bottom: 0.25rem; /* Coloca la sombra justo*/
}

.title{
  color: lightseagreen;
  font-weight: bold;
}

.enlace{
    font-size: 22px;
    color: blue;
    text-align: center;
    font-weight: bold;
    padding: 0.5rem 1rem;
    border: 1px solid blue;
    border-radius: 5px;
    display: inline-block;
    text-decoration: none;
    transition: background-color 0.3s;
    width: 400px;
    height: 60px;
}

.enlace:hover {
    background-color: rgba(0, 0, 255, 0.1); /* Fondo al pasar el ratón */
}

/* Media query para pantallas anchas (40rem o más) */
@media (min-width: 40rem) {
ul {
    grid-template-columns: 1fr var(--line-w) 1fr; /* Ajusta la cuadrícula para tener tres columnas */
}
ul::before {
    grid-column: 2; /* Mueve la línea vertical a la segunda columna de la cuadrícula */
}
ul li:nth-child(odd) {
    grid-column: 1; /* Coloca los ítems impares en la primera columna */
}
ul li:nth-child(even) {
    grid-column: 3; /* Coloca los ítems pares en la tercera columna */
}

  /* Ajuste para que el segundo ítem abarque dos filas */
ul li:nth-child(2) {
    grid-row: 2/4; /* El segundo ítem ocupará desde la segunda hasta la cuarta fila */
}

  /* Ajustes específicos para los ítems impares */
ul li:nth-child(odd) .fecha::before {
    clip-path: polygon(0 0, 100% 0, 100% 100%); /* Invierte el triángulo en los ítems impares */
    left: 0; /* Alinea el triángulo a la izquierda */
}

ul li:nth-child(odd) .fecha::after {
    transform: translate(-50%, -50%); /* Ajusta la posición del círculo en los ítems impares */
    left: calc(100% + var(--col-gap) + var(--line-w) / 2); /* Coloca el círculo a la derecha de la línea */
}

ul li:nth-child(odd) .fecha {
    border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0; /* Ajusta los bordes redondeados para los ítems impares */
}
}

/* Estilo para los créditos */
.credits {
  margin-top: 1rem; /* Espaciado superior para los créditos */
  text-align: right; /* Alinea el texto de los créditos a la derecha */
}
.credits a {
  color: var(--color); /* Aplica el color de texto definido en la variable */
}

@media (max-width: 768px) {
  ul {
    width: 100%; /* Haz que el contenedor ocupe el 100% del ancho de la pantalla */
    padding: 1rem; /* Reduce el padding alrededor del contenido */
  }

  .title, .descripcion {
    font-size: 0.9rem; /* Reduce el tamaño de fuente */
    padding-inline: 1rem; /* Reduce el padding horizontal */
  }

  .enlace {
    font-size: 16px; /* Ajusta el tamaño de la fuente */
    width: auto; /* Haz que el ancho del enlace se ajuste automáticamente */
    height: auto; /* Ajusta la altura para que sea dinámica */
  }
}
</style>