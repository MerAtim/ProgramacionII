<script setup>
import {ref} from 'vue';
const fechaColor = ref([]);
fechaColor.value = [
    {color: "#41516c"},
    {color: "#FBCA3E"},
    {color: "#E24A68"},
    {color: "#1B5F8C"},
    {color: "#4CACAD"}
];

const educacion = ref([]);
educacion.value = [
{fecha: "2024", title: "Tecnicatura Universitaria en Programacion", descripcion: "Durante esta formación, adquirí conocimientos fundamentales en el desarrollo de software, incluyendo lenguajes de programación como Java, Python y JavaScript. Aprendí sobre estructuras de datos, algoritmos, bases de datos y metodologías de desarrollo ágil. Además, desarrollé habilidades en el trabajo en equipo y la resolución de problemas, lo que me permitió participar en proyectos prácticos que simularon entornos laborales reales. Esta formación me preparó para enfrentar desafíos en el campo de la tecnología y la programación."},
{fecha: "2024", title: "Diseño Grafico" , descripcion: "En este curso, adquirí habilidades en diseño gráfico utilizando herramientas de Adobe, como Photoshop e Illustrator. Aprendí sobre principios de diseño, teoría del color y tipografía, así como técnicas para crear composiciones visuales efectivas. A través de proyectos prácticos, desarrollé la capacidad de conceptualizar y ejecutar diseños creativos para diversos medios, fortaleciendo mi portafolio y mis habilidades en comunicación visual."},
{fecha: "2024", title: "Desarrollo FullStack Java", descripcion: "En este curso, adquirí habilidades en el desarrollo de aplicaciones web utilizando Java en el backend y tecnologías como HTML, CSS y JavaScript en el frontend. Aprendí a trabajar con frameworks como Spring y Hibernate, así como a diseñar y gestionar bases de datos con MySQL."},
{fecha: "2023", title: "Quality Assurance Manual", descripcion: "En estos cursos, adquirí conocimientos fundamentales en aseguramiento de la calidad de software. Aprendí sobre metodologías de prueba, diseño de casos de prueba, ejecución de pruebas manuales y documentación de resultados. Me familiaricé con herramientas de seguimiento de errores y prácticas de gestión de calidad, lo que me permitió desarrollar habilidades críticas para garantizar que las aplicaciones cumplan con los estándares de calidad y funcionalidad."},
{fecha: "2022", title: "Fundamentos de Programacion y Desarrollo FullStack Java", descripcion: "Este curso de un año me brindó una sólida base en programación. Comenzamos con dos meses de fundamentos de programación utilizando pseudocódigo, lo que me ayudó a desarrollar habilidades lógicas esenciales. Durante los siguientes diez meses, profundicé en Java y aprendí sobre bases de datos con MySQL y el entorno de desarrollo XAMPP. Como proyecto final, desarrollamos una aplicación con interfaz gráfica de usuario utilizando Java Swing, lo que me permitió aplicar mis conocimientos en un entorno práctico y real."},
];
</script>