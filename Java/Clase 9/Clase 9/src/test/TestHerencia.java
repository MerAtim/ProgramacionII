package test; // Paquete donde se encuentra la clase TestHerencia

import domain.Cliente;
import domain.Empleado; // Importa la clase Empleado del paquete domain
import java.util.Date;

public class TestHerencia { // Clase principal para probar la herencia
    public static void main(String[] args) { // Método principal que se ejecuta al iniciar el programa
        Empleado empleado1 = new Empleado("Nazareno", 70000); // Crea una nueva instancia de Empleado
        System.out.println("empleado1 = " + empleado1); // Imprime la representación de empleado1
   
        Cliente cliente1 = new Cliente(new Date, true) ;
    }
}