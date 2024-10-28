<template>
    <section class="datos-personales">
        <div class="card">
            <h1>{{ title }}</h1>
            <h2>{{ descripcion }}</h2>
            <p>{{ presentacion }}</p>
            <ul class="container-lista">
                <li v-for="red in redesSociales" :key="red.id">
                    <a :href="red.url" target="_blank">
                        <img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name">
                    </a>
                </li>
            </ul>
            <h3>
                <LineMdPhoneCallTwotoneLoop style="width: 1.5em; height: 1.5em; vertical-align: middle;" />
                Mi teléfono personal: {{ telefono }}
            </h3>
            <h4>{{ residencia }}</h4>
        </div>
    </section>
    </template>
    
    <script setup>
    import linkedinIcon from '../assets/linkedin_icon.svg';
    import githubIcon from '../assets/github_icon.svg';
    import cvIcon from '../assets/cv_resume_icon.svg';
    import LineMdPhoneCallTwotoneLoop from './LineMdPhoneCallTwotoneLoop.vue';
    
    const title = "Maria Mercedes Atim";
    const descripcion = "Tecnica Universitaria en Programación - UTN";
    const residencia = "General San Martin, Buenos Aires, Argentina";
    const presentacion = "Hola, bienvenido a mi portafolio de proyectos. Soy una desarrolladora FullStack con experiencia en desarrollo de aplicaciones web y móviles.";
    const telefono = "+54 9 11 3150-9571";
    const redesSociales = [
        {id: 1, name: "LinkedIn", src: linkedinIcon, url: "https://www.linkedin.com/in/maria-mercedes-atim-648898280/"},
        {id: 2, name: "GitHub", src: githubIcon, url: "https://github.com/MerAtim/"},
        {id: 3, name: "Curriculum Vitae", src: cvIcon, url: "https://www.canva.com/design/DAF7k0BgkOc/dOVgmgYoyrsUaBKbXUtFIQ/edit"}
    ];
    </script>
    
    <style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playwrite+ES+Deco:wght@100..400&family=Sacramento&family=Sevillana&family=Imperial+Script&family=Cookie&family=MonteCarlo&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Rochester&family=Updock&family=Delius&family=Macondo&family=Oregano:ital@0;1&family=Pinyon+Script&family=Rouge+Script&family=Style+Script&display=swap');
    
    .card {
        background-color: #E24A68;
        border-radius: 15px;
        padding: 2rem;
        margin: 20px auto;
        text-align: center;
        font-family: Montserrat, sans-serif;
        max-width: 1100px; /* Ajusta el ancho máximo de la tarjeta */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
/*.card {
    background-color: #E24A68;
    border-radius: 15px; /* Igual que el otro componente */
    /*padding: 2rem; /* Igualar padding */
    /*margin: 20px auto; /* Centrado */
    /*text-align: center;
    font-family: Montserrat, sans-serif;
    max-width: 800px; /* Ajusta según sea necesario */
   /* box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
*/

    h1 {
        font-family: 'MonteCarlo', cursive;
        font-size: 2.5rem; /* Reduce el tamaño del h1 */
        font-weight: bolder;
        color: black;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-size: 1.5rem; /* Puedes ajustar el tamaño del h2 si es necesario */
    }
    
    p {
        font-size: 1rem; /* Ajusta el tamaño del párrafo para que encaje mejor */
        font-weight: 600;
        margin-bottom: 1rem;
        color: black;
    }
    
    .container-lista {
        display: flex;
        justify-content: center;
        list-style: none;
        padding: 0;
        margin: 1rem 0;
    }
    
    .icon-redsocial {
        background-color: aliceblue;
        border-radius: 50%;
        padding: 5px;
        margin: 0 10px;
        box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
        width: 35px;
        height: 35px;
    }
    
    .icon-redsocial:hover {
        background-color: rgb(28, 41, 52);
        box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
    }
    
    h3 {
        font-size: 1rem; /* Ajusta el tamaño del h3 */
        font-weight: 600;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 1rem;
        color: black;
    }
    
    h4 {
        color: black;
        margin-top: 0.5rem;
    }
    
    h3 svg {
        margin-right: 8px;
    }
    
    /* Estilos responsivos */
    @media (max-width: 768px) {
        .card {
            padding: 10px; /* Reduce el padding en dispositivos móviles */
            margin: 10px; /* Reduce el margen en dispositivos móviles */
        }
    
        h1 {
            font-size: 2.5rem; /* Reduce el tamaño del h1 en dispositivos móviles */
        }
    
        h2 {
            font-size: 1.2rem; /* Ajusta el tamaño del h2 en dispositivos móviles */
        }
    
        p {
            font-size: 0.9rem; /* Ajusta el tamaño del párrafo en dispositivos móviles */
        }
    
        h3 {
            font-size: 0.9rem; /* Ajusta el tamaño del h3 en dispositivos móviles */
        }
    
        h4 {
            font-size: 0.9rem; /* Ajusta el tamaño del h4 en dispositivos móviles */
        }
    
        .container-lista {
            flex-direction: column; /* Alinea los íconos verticalmente en dispositivos móviles */
        }
    
        .icon-redsocial {
            margin: 5px; /* Ajusta el margen de los íconos en dispositivos móviles */
        }
    }
    </style>
    