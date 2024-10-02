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

    nombreCompleto(){
        return this._nombre+" "+this._apellido;
    }
// Sobreescribiendo el metodo de la super clase padre Object
    toString(){ //devuelve un String
        //Se aplica El polimorfismo que es un principio de la programación orientada a objetos que permite que diferentes clases implementen métodos con el mismo nombre, pero con comportamientos específicos. Esto permite tratar objetos de distintas clases de manera uniforme, mejorando la flexibilidad y mantenibilidad del código.
        //El metodo que se ejecuta depende si es una referencia de tipo padre o hija
    return this.nombreCompleto();
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

    // Sobreescritura (Modificar el comportamiento del metodo de la clase padre)
    nombreCompleto(){
        return super.nombreCompleto()+ ", " + this._departamento;
    }
}

let persona1 = new Persona("Mariana", "Aguilera");
let persona2 = new Persona("Melina", "Aguilar", "");
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
console.log("\nMetodo heredado de la clase padre: nombreCompleto(): ",empleado1.nombreCompleto());

// Object.prototype.toString  Es una manera de acceder de forma dinamica a los atributos y métodos

console.log("\nMetodo de la clase padre toString aplicando polimorfismo usando la forma de la clase hija, de ésta manera muestra nombre completo y departamento de trabajo: ",empleado1.toString());
console.log("En este caso solo trae el metodo de la clase padre: ", persona1.toString());