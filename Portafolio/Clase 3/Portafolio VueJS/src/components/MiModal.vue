<template>
    <div v-if="isOpen" class="modal-overlay mi-modal" @click="close">
        <div class="modal-content" @click.stop>
            <img :src="image" alt="Seleccionada" />
            <button @click="close" class="mi-modal-boton">Cerrar</button>
        </div>
    </div>
</template>


<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    isOpen: {
        type: Boolean,
        required: true
    },
    image: {
        type: String,
        required: true
    },
    close: {
        type: Function,
        required: true
    }
});
</script>

<style>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content {
    display: flex;
    background: white;
    padding: 20px;
    border-radius: 5px;
    align-items: center;
    flex-direction: column;
    gap: 10px;
}

img {
    max-width: 100%;
    max-height: 80vh;
}

.mi-modal-boton {
    background-color: #E24A68; /* Color de fondo del botón */
    color: white; /* Color del texto */
    border: none; /* Sin borde */
    border-radius: 10px; /* Bordes redondeados */
    padding: 0.75rem 0.75rem; /* Espaciado interno */
    font-size: 15px; /* Tamaño de fuente */
    font-weight: bold; /* Texto en negrita */
    cursor: pointer; /* Cambia el cursor al pasar el ratón */
    transition: background-color 0.4s, transform 0.3s; /* Transición suave para el color y el tamaño */
    align-items: center;
}

.mi-modal-boton:hover {
    background-color: #D23E56; /* Color de fondo en hover */
    transform: scale(1.15); /* Efecto de aumento al pasar el ratón */
}

.mi-modal-boton:active {
    transform: scale(0.95); /* Efecto de reducción al hacer clic */
}
</style>
