class Persona{ // Clase Padre
    constructor(nombre, apellido){
        this._nombre = nombre; //Usamos guion bajo antes del nombre de la propiedad para que el metodo get no tenga el mismo nombre que la propiedad
        this._apellido = apellido;
    }

    get nombre(){ // Obtener/mostrar un dato
        return this._nombre;
    }

    get apellido(){ // Obtener/mostrar un dato
        return this._apellido;
    }

    set nombre(nombre){ // Modificar un dato
        this._nombre = nombre;
    }

    set apellido(apellido){ // Modificar un dato
        this._apellido = apellido;
    }
}

class Empleado extends Persona{ // Clase hija o subclase
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento
    }
}

let persona1 = new Persona("Mariana", "Aguilera");
let persona2 = new Persona("Melina", "Aguilar");
console.log(persona1,"\n",persona2); // Mostramos ambos objetos

console.log("\nUsamos el método GET():");
console.log(persona1.nombre, persona1.apellido);
console.log(persona2.nombre, persona2.apellido);

console.log("\nUsamos el método SET():");
persona1.nombre = "Nicolas"; // Modificamos el nombre
persona1.apellido = "Mercado"; // Modificamos el apellido
console.log("Ahora persona1 es: ",persona1.nombre, persona1.apellido); // Mostramos el objeto modificado
persona2.nombre = "Nelson";
persona2.apellido = "Rios";
console.log("Ahora persona2 es: ",persona2.nombre, persona2.apellido);

// A diferencia de las funciones, no se puede crear un objeto antes de iniciar una clase. Cuando trabajamos con clases no se aplica el concepto de hoisting. Primero debe definirse la clase para poder utilizarla.

console.log("\nCreacion clase hija: ");
let empleado1 = new Empleado("Cirano", "Molina", "Sistemas");
console.log(empleado1);