<script setup>
const title = "Maria Mercedes Atim";
const descripcion = "Tecnica Universitaria en Programación - UTN";
const residencia = "General San Martin, Buenos Aires, Argentina";
const presentacion = "Hola, bienvenido a mi portafolio de proyectos. Soy una desarrolladora FullStack con experiencia en desarrollo de aplicaciones web y móviles.";
const telefono = "+54 9 11 1212-1414";
const redesSociales = [
    {id: 1, name: "LinkedIn", src: "../assets/linkedin_icon.svg", url: "https://www.linkedin.com/in/maria-mercedes-atim-648898280/"},
    {id: 2, name: "GitHub", src: "../assets/github_icon.svg", url: "https://github.com/MerAtim/"},
    {id: 2, name: "Curriculum Vitae", src: "../assets/cv_resume_icon.svg", url: "https://www.canva.com/design/DAF7k0BgkOc/dOVgmgYoyrsUaBKbXUtFIQ/edit"}
];
</script>

<template>
<section class="datos-personales">
<div class="card">
    <h1>{{ title }}</h1>
    <h2>{{ descripcion }}</h2>
    <p>{{ presentacion }}</p>
    <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
            <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
        </li>
    </ul>
    <h3>☎ Mi telefono personal: {{ telefono }}</h3>
    <h4>{{ residencia }}</h4>
</div>
</section>
</template>

<style scoped>
h1{
    font-size: 2.5rem;
}

p{
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.card{
    background-color: rgb(28, 41, 52);
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
}

.container-lista{
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

.icon-redsocial{
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover{
    background-color: rgb(28, 41, 52);
    box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3{
    font-size: 1.2rem;
    font-weight: 600;
}
</style>