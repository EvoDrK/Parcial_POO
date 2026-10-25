# Guardians of the Ancient Kingdom

## 1. Presentación del proyecto

*Guardians of the Ancient Kingdom* es una aplicación creada en Python que permite simular enfrentamientos por turnos entre tres tipos de personajes del reino de Eldoria: guerreros, magos y arqueros.

Cada combatiente posee características como nombre, puntos de vida, ataque y defensa. Sin embargo, cada clase dispone de una habilidad particular que influye en el daño que puede ocasionar. El programa se encarga de gestionar los turnos, calcular los ataques, modificar la vida de los participantes y establecer el desenlace de cada enfrentamiento.

## 2. Organización de los archivos

El repositorio está formado por tres archivos:

- **personajes.py:** Define las clases del sistema, sus atributos, las habilidades especiales, las validaciones y las reglas de combate.
- **main.py:** Contiene el código principal para crear personajes, iniciar batallas y ejecutar diferentes pruebas.
- **README.md:** Explica el funcionamiento del proyecto, su estructura y los principios de programación orientada a objetos utilizados.

## 3. Descripción de las clases

**Personaje:** Es la clase abstracta que establece los atributos y comportamientos básicos de los combatientes. Incluye el nombre, la vida, el ataque y la defensa, además de métodos para recibir daño, comprobar si continúa vivo y consultar su estado. También define `atacar()` como método abstracto.

**Guerrero:** Es un luchador especializado en ataques físicos. Su habilidad, denominada *Golpe Contundente*, incrementa el ataque en un 20 % antes de calcular el daño contra la defensa rival.

**Mago:** Utiliza ataques mágicos capaces de atravesar las defensas del oponente, por lo que el daño depende directamente de su poder de ataque.

**Arquero:** Combate a distancia y puede realizar un disparo crítico que duplica el daño base cuando su ataque supera la defensa enemiga.

**Combate:** Administra el desarrollo de las batallas, alterna los turnos, ejecuta los ataques y determina si existe un vencedor, un empate o una condición para finalizar el enfrentamiento.

## 4. Vínculos entre las clases

- **Herencia:** Guerrero, Mago y Arquero derivan de Personaje, por lo que comparten sus características generales.
- **Asociación:** Se presenta cuando un personaje interactúa con otro, como sucede al ejecutar un ataque contra un rival.
- **Agregación:** La clase Combate utiliza personajes que fueron creados previamente. Estos pueden seguir existiendo independientemente de que la batalla haya terminado.

## 5. Principios de programación orientada a objetos

**Abstracción:** La clase Personaje establece una estructura común sin definir los detalles particulares del ataque de cada clase.

**Encapsulamiento:** Los atributos se administran mediante propiedades y métodos de acceso que permiten validar los valores antes de modificarlos.

**Herencia:** Las clases especializadas aprovechan los atributos y métodos de Personaje, reduciendo la repetición de código.

**Polimorfismo:** Cada tipo de combatiente implementa su propia versión del método `atacar()`, adaptándola a su habilidad especial.

## 6. Funcionamiento del combate

Las batallas se desarrollan mediante una secuencia de turnos. En cada uno, el atacante ejecuta su habilidad, se calcula el daño, el rival pierde vida y se comprueba el estado de ambos participantes. El proceso continúa hasta que se cumpla una condición de finalización.

Las reglas de daño son las siguientes:

- **Guerrero:** Daño = máximo entre 0 y (ataque × 1.20 − defensa).
- **Mago:** Daño = ataque, sin descontar la defensa rival.
- **Arquero:** El daño base corresponde a ataque − defensa. Si el ataque supera la defensa, el daño base se multiplica por dos.

El combate puede terminar en empate si ambos personajes completan una ronda sin infligirse daño o si se alcanza el límite establecido de 50 rondas sin un ganador.

## 7. Cómo ejecutar el programa

Para iniciar el proyecto, es necesario tener Python instalado.

1. Descargar el repositorio o clonarlo.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el archivo principal con el siguiente comando:

```bash
python mainP.py
```

Al iniciarse, el programa ejecuta el enfrentamiento principal y posteriormente realiza las pruebas definidas.

## 8. Verificación del sistema

Se probaron diferentes situaciones para comprobar el comportamiento del programa, entre ellas:

1. Instanciación de las tres clases de personajes.
2. Validación de los puntos de vida y rechazo de valores no permitidos.
3. Detección de nombres vacíos.
4. Control de los límites de ataque y defensa.
5. Funcionamiento de las habilidades especiales.
6. Aplicación correcta del daño y actualización de la vida.
7. Prevención de ataques por parte de personajes derrotados.
8. Ejecución de combates y determinación de sus resultados.
9. Comprobación de empates cuando no es posible causar daño.

De acuerdo con las pruebas descritas, el sistema cumple con los comportamientos esperados para las validaciones, los ataques y la resolución de las batallas.
