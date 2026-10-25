from abc import ABC, abstractmethod
from math import floor


class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El nombre esta vacio")
        self._nombre = valor

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if not isinstance(valor, int):
            raise TypeError("La vida debe ser un numero entero")
        if valor < 0 or valor > 100:
            raise ValueError("La vida debe estar entre los numeros 0 y 100")
        self._vida = valor

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        if not isinstance(valor, int):
            raise TypeError("El ataque debe ser un numero entero")
        if valor <= 0:
            raise ValueError("El ataque debe ser positivo")
        self._ataque = valor

    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, valor):
        if not isinstance(valor, int):
            raise TypeError("La defensa debe ser un numero entero")
        if valor < 0:
            raise ValueError("La defensa no puede ser menor a 0")
        self._defensa = valor

    def recibir_danio(self, cantidad):
        if not isinstance(cantidad, int):
            raise TypeError("El daño debe ser un numero natural")
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo")

        vida_anterior = self.vida
        self._vida = max(0, self.vida - cantidad)
        return vida_anterior - self.vida

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_estado(self):
        print(
            f"Nombre: {self.nombre} | Vida: {self.vida} | "
            f"Ataque: {self.ataque} | Defensa: {self.defensa}"
        )

    def _validar_ataque(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError("Objetivo invalido")
        if not self.esta_vivo():
            raise ValueError(f"{self.nombre} Esta derrotado")
        if not objetivo.esta_vivo():
            raise ValueError(f"{objetivo.nombre} Ya fue derrotado, no se puede atacar")

    def atacar(self, objetivo):
        self._validar_ataque(objetivo)
        return objetivo.recibir_danio(self._calcular_danio(objetivo))

    @abstractmethod
    def _calcular_danio(self, objetivo):
        pass


class Guerrero(Personaje):
    def _calcular_danio(self, objetivo):
        ataque_potenciado = floor(self.ataque * 1.20)
        return max(0, ataque_potenciado - objetivo.defensa)


class Mago(Personaje):
    def _calcular_danio(self, objetivo):
        return self.ataque


class Arquero(Personaje):
    def _calcular_danio(self, objetivo):
        return max(0, self.ataque - objetivo.defensa) * 2


class Combate:
    MAX_RONDAS = 30

    def __init__(self, personaje1, personaje2):
        if not isinstance(personaje1, Personaje):
            raise TypeError(
                "El primer participante no es invalido, este debe ser un objeto de tipo Personaje"
            )
        if not isinstance(personaje2, Personaje):
            raise TypeError(
                "El segundo participante no es invalido, este debe ser un objeto de tipo Personaje"
            )

        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.turno_actual = personaje1
        self.ganador = None

    def _obtener_defensor(self):
        if self.turno_actual is self.personaje1:
            return self.personaje2
        return self.personaje1

    def cambiar_turno(self):
        self.turno_actual = self._obtener_defensor()

    def verificar_ganador(self):
        if not self.personaje1.esta_vivo():
            self.ganador = self.personaje2
        elif not self.personaje2.esta_vivo():
            self.ganador = self.personaje1

        return self.ganador

    def mostrar_resultado(self):
        if self.ganador:
            print(f"El ganador es: {self.ganador.nombre}")
        else:
            print("Empate")

    def iniciar(self):
        for ronda in range(1, self.MAX_RONDAS + 1):
            dano_ronda = 0

            for _ in range(2):
                atacante = self.turno_actual
                defensor = self._obtener_defensor()

                dano = atacante.atacar(defensor)
                dano_ronda += dano

                print(
                    f"ronda {ronda}: {atacante.nombre} ataca a {defensor.nombre} "
                    f"y causa {dano} de daño, vida restante de {defensor.nombre}: {defensor.vida}"
                )

                self.personaje1.mostrar_estado()
                self.personaje2.mostrar_estado()

                if self.verificar_ganador():
                    self.mostrar_resultado()
                    return

                self.cambiar_turno()

            if dano_ronda == 0:
                print("Empate tecnico")
                self.mostrar_resultado()
                return

        print("Limite de rondas alcanzado, el combate termina en empate")
        self.mostrar_resultado()


if __name__ == "__main__":
    guerrero = Guerrero("Conan", 100, 20, 5)
    mago = Mago("Merlin", 80, 25, 2)
    combate = Combate(guerrero, mago)
    combate.iniciar()
