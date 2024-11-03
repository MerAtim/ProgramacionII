<template>
    <div>
      <div id="particles-js"></div>
      <div id="stats">
        <div class="count-particles">Partículas: <span class="js-count-particles">0</span></div>
      </div>
    </div>
  </template>
  
  <script>
  import particlesJS from 'particles.js';
  import Stats from 'stats.js';
  
  export default {
    mounted() {
      this.initParticles();
      this.initStats();
    },
    methods: {
      initParticles() {
        particlesJS("particles-js", {
          particles: {
            number: {
              value: 380,
              density: { enable: true, value_area: 800 }
            },
            color: { value: "#35df9b" },
            shape: {
              type: "circle",
              stroke: { width: 0, color: "#35df9b" },
              polygon: { nb_sides: 5 },
              image: { width: 100, height: 100 }
            },
            opacity: {
              value: 0.5,
              random: false,
              anim: { enable: false }
            },
            size: {
              value: 3,
              random: true,
              anim: { enable: false }
            },
            line_linked: {
              enable: true,
              distance: 150,
              color: "#35df9b",
              opacity: 0.4,
              width: 1
            },
            move: {
              enable: true,
              speed: 6,
              direction: "none",
              random: false,
              straight: false,
              out_mode: "out",
              bounce: false,
              attract: { enable: false }
            }
          },
          interactivity: {
            detect_on: "canvas",
            events: {
              onhover: { enable: true, mode: "grab" },
              onclick: { enable: true, mode: "push" },
              resize: true
            },
            modes: {
              grab: { distance: 140, line_linked: { opacity: 1 } },
              bubble: { distance: 400, size: 40, duration: 2, opacity: 8, speed: 3 },
              repulse: { distance: 200, duration: 0.4 },
              push: { particles_nb: 4 },
              remove: { particles_nb: 2 }
            }
          },
          retina_detect: true
        });
      },
      initStats() {
        const stats = new Stats();
        stats.setMode(0);
        stats.domElement.style.position = 'absolute';
        stats.domElement.style.left = '0px';
        stats.domElement.style.top = '0px';
        document.body.appendChild(stats.domElement);
  
        const count_particles = document.querySelector('.js-count-particles');
  
        const update = () => {
          stats.begin();
          stats.end();
          if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) {
            count_particles.innerText = window.pJSDom[0].pJS.particles.array.length;
          }
          requestAnimationFrame(update);
        };
  
        requestAnimationFrame(update);
      }
    }
  };
  </script>
  
  <style scoped>
  body {
    margin: 0;
  }
  
  canvas {
    display: block;
    vertical-align: bottom;
  }
  
  #particles-js {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: #245864;
  }
  
  #stats,
  .count-particles {
    -webkit-user-select: none;
  }
  
  #stats {
    border-radius: 3px 3px 0 0;
    overflow: hidden;
  }
  
  .count-particles {
    border-radius: 0 0 3px 3px;
  }
  </style>