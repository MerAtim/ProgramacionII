package pasoPorReferencia;

import clase4.Persona;

public class PasoPorReferencia {

    public static void main(String[] args) {
        Persona persona1 = new Persona(); // Se llama al constructor de la clase
        persona1.nombre = "Melina"; // Se declara el nombre del objeto
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = null; // Instancia una persona como nulo, vacío
        persona2 = cambiarElValor(persona2);
        Persona persona3 = new Persona(); // se instancia un objeto de tipo Persona
        persona3 = cambiarElValor(persona3);
        System.out.println("El nuevo valor del objeto es: " + persona3.nombre);
    }

    public static void cambiarValor(Persona persona) { // parametro por referencia
        persona.nombre = "Maria";  // Se va a modificar el original, ya que no es una copia
    }

    public static Persona cambiarElValor(Persona persona) {
        if (persona == null) {
            System.out.println("Valor de persona es inválido: Null");
            return null;
        } else {
            persona.nombre = "Monica";
            return persona;
        }
    }
}