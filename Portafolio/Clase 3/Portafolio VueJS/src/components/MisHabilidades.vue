<template>
    <div class="mis-habilidades">
      <div v-for="(categoria, index) in habilidadesPorCategoria" :key="index" class="categoria">
        <h3>{{ categoria.nombre }}</h3>
        <div class="habilidades-container">
          <div v-for="habilidad in categoria.habilidades" :key="habilidad.nombre" class="habilidad-card">
            <img :src="habilidad.gif" :alt="habilidad.nombre" class="habilidad-gif" />
            <div class="detalle">
              <h4>{{ habilidad.nombre }}</h4>
              <p>Nivel: {{ habilidad.nivel }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import javaGif from '@/assets/Java.gif';
  import pythonGif from '@/assets/Python.gif';
  import javascriptGif from '@/assets/js.gif';
  import vueGif from '@/assets/Vuejs.gif';
  import nodeGif from '@/assets/node.gif';
  import gitGif from '@/assets/git.gif';
  import htmlGif from '@/assets/HTML.gif';
  import cssGif from '@/assets/css.gif';
  import mysqlGif from '@/assets/MySQL.gif';
  import figmaGif from '@/assets/Figma.gif';
  import adobeIllustratorGif from '@/assets/Illustrator.gif';
  import photoshopGif from '@/assets/Photoshop.gif';
  import inglesGif from '@/assets/ingles.gif';
  import espanolGif from '@/assets/Español.gif';
  import postmanGif from '@/assets/Postman.gif';
  import dbeaver from '@/assets/Dbeaver.gif';
  import eclipse from '@/assets/Eclipse.gif';
  import intellij from '@/assets/Intellij.gif';
  import netbeans from '@/assets/Netbeans.gif';
  import pycharm from '@/assets/Pycharm.gif';
  import sql from '@/assets/Sql.gif';
  import sublime from '@/assets/SublimeText.gif';
  import vscode from '@/assets/Vscode.gif';

  
  export default {
    name: 'MisHabilidades',
    data() {
      return {
        habilidadesPorCategoria: [
          {
            nombre: 'Lenguajes de Programación:',
            habilidades: [
              { nombre: 'Java', nivel: 'Básico', gif: javaGif },
              { nombre: 'Python', nivel: 'Básico', gif: pythonGif },
              { nombre: 'SQL', nivel: 'Básico', gif: sql },
              { nombre: 'JavaScript', nivel: 'Básico', gif: javascriptGif }
          ]
          },
          {
            nombre: 'Desarrollo Web y Bibliotecas',
            habilidades: [
              { nombre: 'HTML', nivel: 'Intermedio', gif: htmlGif },
              { nombre: 'CSS', nivel: 'Avanzado', gif: cssGif },
              { nombre: 'Vue.js', nivel: 'Básico', gif: vueGif },
              { nombre: 'Node.js', nivel: 'Básico', gif: nodeGif }
            ]
          },
          {
            nombre: 'Herramientas y Frameworks:',
            habilidades: [
              { nombre: 'Figma', nivel: 'Intermedio', gif: figmaGif },
              { nombre: 'Adobe Illustrator', nivel: 'Intermedio', gif: adobeIllustratorGif },
              { nombre: 'Photoshop', nivel: 'Intermedio', gif: photoshopGif },
              { nombre: 'Postman', nivel: 'Intermedio', gif: postmanGif },
              { nombre: 'DBeaver', nivel: 'Intermedio', gif: dbeaver },
              { nombre: 'Eclipse', nivel: 'Intermedio', gif: eclipse },
              { nombre: 'Git', nivel: 'Intermedio', gif: gitGif },
              { nombre: 'Intellij Idea', nivel: 'Intermedio', gif: intellij },
              { nombre: 'Netbeans', nivel: 'Intermedio', gif: netbeans },
              { nombre: 'Pycharm', nivel: 'Intermedio', gif: pycharm },
              { nombre: 'Sublime Text', nivel: 'Intermedio', gif: sublime },
              { nombre: 'Visual Studio', nivel: 'Intermedio', gif: vscode },
            ]
          },
          {
            nombre: 'Bases de Datos:',
            habilidades: [
              { nombre: 'MySQL', nivel: 'Intermedio', gif: mysqlGif },
            ]
          },
          {
            nombre: 'Idiomas:',
            habilidades: [
              { nombre: 'Inglés', nivel: 'Avanzado', gif: inglesGif },
              { nombre: 'Español', nivel: 'Nativo', gif: espanolGif }
            ]
          },
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .mis-habilidades {
  margin: 20px;
  background-color: #E24A68;
  border-radius: 15px; /* Bordes redondeados */
  padding: 20px; /* Espaciado interno para que el contenido no toque los bordes */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Sombra suave para el contenedor */
}
  
  .categoria {
    margin-bottom: 20px;
  }
  
  .habilidades-container {
    display: flex;
    flex-wrap: wrap; /* Permite que las tarjetas se ajusten en varias filas */
    gap: 20px; /* Espaciado entre las tarjetas */

  }
  
  .habilidad-card {
  background-color: #d294b3; /* Fondo de la tarjeta */
  border: 1px solid #ddd; /* Borde de la tarjeta */
  border-radius: 8px; /* Bordes redondeados */
  padding: 15px; /* Espaciado interno */
  width: 150px; /* Ancho fijo de las tarjetas */
  text-align: center; /* Centra el contenido */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Sombra suave */
  transition: transform 0.2s; /* Transición suave para el hover */display: flex;
  flex-direction: column; /* Organiza el contenido en columna */
  align-items: center; /* Centra el contenido horizontalmente */
  justify-content: center; /* Centra el contenido verticalmente */
  height: 220px; /* Asegúrate de que todas las tarjetas tengan la misma altura */
}
  
  .habilidad-card:hover {
    transform: scale(1.05); /* Aumenta ligeramente el tamaño al pasar el mouse */
  }
  
  .habilidad-gif {
    width: 80px; /* Ajusta el tamaño según tus preferencias */
    height: 80px;
    object-fit: contain;
  }
  
  .detalle {
  margin-top: 10px; /* Espaciado entre la imagen y el texto */
  text-align: center; /* Centra el texto */
  color: black;
}
  
  h4, h3 {
    font-weight: bolder;
  }

  .habilidad-gif[alt="JavaScript"] {
  width: 50px; /* Tamaño reducido solo para el logo de JavaScript */
  height: 50px;
  margin-bottom: 30px;
}

@media (max-width: 768px) {
  .mis-habilidades {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 20px auto;
    max-width: 100%;
    padding: 10px;
    }

  .habilidades-container {
    justify-content: center;
  }

  .habilidad-card {
    width: 100%;
    max-width: 150px;
    margin: 0 auto;
  }
}
  </style>