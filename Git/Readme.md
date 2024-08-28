# **Clase 1**

**COMANDOS**

***Import repository, New repository, New organization:** significa que es como tu empresa*

***New project:** significa es como un grupo de repositorios que puedes tener dentro de una empresa. *

***New gist:** es un pedacito de código que puedes compartir*

**New repository Ponemos el nombre:** class-git.

**Create repository:** Lo ponemos en privado o en Publico.

El **README.md** es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.

Para **clonar** un repositorio desde GitHub (o cualquier otro servidor remoto) debemos **copiar la URL** (por ahora, usando HTTPS) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

ATENCIÓN: ¿Por qué? **Porque a través de https nos pedirá usuario(nombre perfil) y contraseña.**

Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.

Cómo conectar un repositorio de GitHub a nuestro documento local: Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:

* [ ] **Guardar la URL del repositorio de GitHub con el nombre de origin**
* [ ] **git remote add origin URL**

**Verificar que la URL se haya guardado correctamente:**

* [ ] **git remote**
* [ ] **git remote -v**

Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. Podemos usar **git fetch y git merge** o solo **git pull con el flag --allow-unrelated-histories:**

**git pull origin master --allow-unrelated-histories**

Por último, ahora sí podemos hacer git push para guardar los cambios de nuestro repositorio local en GitHub:

**git push origin master**

### **Cómo autenticarte en GitHub 2022**

Antes de empezar debemos renombrar la rama **‘máster’ a ‘main’,** este es el nuevo estándar en GitHub, para esto:

Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.

Ejecutamos el siguiente comando: **git branch -M main**

#### Pasos para crear un token de acceso personal.

Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.

#### **Descubre el uso de tags en Github**

Seguir la secuencia: **Ingresamos a nuestra cuenta de GitHub.**

**Buscamos Settings**

**Click en Developer settings**

**Click en Personal access tokens**

**Click en Generate new token aquí se puede colocar un nombre, la fecha de expiración.**

**Tildar en repo y luego click en el botón verde Generate token**

# Clase 2

**¿Qué es una Llave SSH?**

Son un par de claves criptográficas que se utilizan para autenticarte en un servidor. Una **llave SSH** (Secure Shell) es una herramienta criptográfica utilizada para autenticar y cifrar las comunicaciones entre un cliente y un servidor, garantizando una conexión segura. En el contexto de Git y GitHub, las llaves SSH se utilizan para autenticar las conexiones entre tu máquina local y los servidores de GitHub. Aquí hay un desglose de qué es una llave SSH, cómo funciona y cómo se usa: Consiste en:

1. **Clave Privada (Private Key):**
   * Es una clave secreta que debe mantenerse en tu máquina local. No debe compartirse con nadie.
   * Se usa para firmar mensajes y autenticarse ante el servidor.
2. **Clave Pública (Public Key):**
   * Es una clave que se puede compartir abiertamente. Se coloca en el servidor al que deseas conectarte.
   * Se usa para verificar la autenticidad de la firma hecha con la clave privada.

Vamos a cargar la llave SSH (Secure Shell) publica en GitHub

**Para copiar la llave publica debes ir al archivo .ssh y allí encontrarás el archivo .pub lo podes abrir con el txt, luego copiar el contenido que esta dentro.**

copiar la llave publica **#Ir a GitHub, vamos a setting, vamos a SSH and GPG keys**

crear una nueva **#New SSH key poner nombre y pegar la ssh publica, con esto esta listo.**

Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.

**git branch #Vemos en que rama estamos**

**git checkout master #Ponernos en la rama master**

**git branch -M main #Cambiamos el nombre a la rama master**

**git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo**

**git remote -v #Vemos si ya esta conectado**

**git merge segunda #Mergeamos lo que tenemos en la rama segunda en main**

**git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy**

**git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.**

**Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.**
