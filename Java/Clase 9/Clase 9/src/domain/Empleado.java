package domain;

public class Empleado extends Persona {

    private int idEmpleado; // Identificador único de cada empleado
    private double sueldo; // Sueldo del empleado
    private static int contadorEmpleados; // Contador estático para generar idEmpleado únicos

    // Constructor de la clase Empleado
    public Empleado(String nombre, double sueldo) {
        super(nombre); // Llama al constructor de la clase padre (Persona)
        this.idEmpleado = ++Empleado.contadorEmpleados; // Incrementa y asigna el idEmpleado
        this.sueldo = sueldo; // Asigna el sueldo del empleado
    }

    // Getter para obtener el sueldo
    public double getSueldo() {
        return sueldo;
    }

    // Getter para obtener el id del empleado
    public int getIdEmpleado() {
        return idEmpleado;
    }

    // Setter para modificar el sueldo
    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }   

    // Sobrescribe el método toString para imprimir detalles del empleado
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(); // Usa StringBuilder para crear la cadena
        sb.append("Empleado ");
        sb.append(" idEmpleado: ").append(idEmpleado); // Agrega el idEmpleado
        sb.append(", sueldo: ").append(sueldo); // Agrega el sueldo
        return sb.toString(); // Retorna la cadena con los detalles del empleado
    }
}