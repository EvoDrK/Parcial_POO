from Personajes import (
    Guerrero,
    Mago,
    Arquero,
    Combate as ClaseCombate
)
#ejemplo de funcionamiento
print("---------Kombate mortal---------")

Kratos = Guerrero(
    "Kratos",
    100,
    30,
    20
)

Arthur = Mago(
    "Arthur",
    80,
    40,
    10
)

Kombate = ClaseCombate(
    Kratos,
    Arthur
)

Kombate.iniciar()

#casos de  prueba
print()
#caso 1: Creación correcta de los tres tipos de personajes.
try: 
    g = Guerrero("Kratos", 100, 30, 15)
    m = Mago("Arthur", 80, 40, 10)
    a = Arquero("Bl4ck", 90, 35, 12)
    
    print("caso 1: se crearon los 3 tipos de personaje")
except Exception as e:
    print(e)

#caso 2: Rechazo de personajes con vida superior a 100 o negativa.
try:
    Guerrero("Kratos", 150, 30, 15)
    
except Exception as e:
    print("caso 2:", e)
    
#caso 3: Rechazo de nombres vacíos.
try:
    Guerrero("", 100, 30, 15)
except Exception as e:
    print("caso 3: ", e)

#caso 4: Rechazo de ataques y defensas inválidos.
try: 
    Guerrero("Kratos", 100, -10, 15)
except Exception as e:
    print("caso 4: ", e)
    
#caso 5: Aplicación correcta de la habilidad del Guerrero.

g1 = Guerrero("Kratos", 100, 30, 10)
m1 = Mago("Arthur", 80, 20, 10)

print("caso 5 - habilidad guerrero: ",
      g1.atacar(m1))

#caso 6: Aplicación correcta del ataque del Mago ignorando defensa.

m2 = Mago("Arthur", 100, 40, 10)
g2 = Guerrero("Kratos", 100, 20, 50)

print("caso 6 - ataque del mago ignorando defensa: ",
      m2.atacar(g2))

#caso 7: Aplicación correcta del disparo crítico del Arquero.

a1 = Arquero("Bl4ck", 100, 35, 10)
g3 = Guerrero("Kratos", 100, 20, 15)

print("caso 7- disparo critico del arquero: ",
      a1.atacar(g3))

#caso 8: Imposibilidad de tener vida negativa.

g4 = Guerrero("Kratos", 10, 20, 10)
g4.recibir_danio(100)
print("caso 8 - vida del personaje: ", 
      g4.vida)

#caso 9: Imposibilidad de atacar estando derrotado.

try: 
    g4.atacar(a1)
except Exception as e:
    print("caso 9 - imposibilidad: ", e)

print()
#caso 10: Ejecución de un combate completo.
#caso 11: Identificación correcta del ganador.
print("caso 10 y 11 - combate y identificacion del ganador")
print("-----------Kombate Mortal II-----------")
Kratos2 = Guerrero("Kratos", 100, 30, 20)

Arthur2 = Mago("Arthur", 80, 40, 10)

Kombate2 = ClaseCombate(Kratos2, Arthur2)
Kombate2.iniciar()
print("----Guardians of the Ancient Kingdom----")
print()
#caso 12: Finalización de un combate sin daño mediante empate técnico.
print("caso 12 - empate tecnico")
print("-----------Kombate Mortal III-----------")

Kratos3 = Guerrero("Kratos", 100, 10, 100)

Kratos4 = Guerrero("Dark Kratos", 100, 10, 100)

Kombate_empate = ClaseCombate(Kratos3, Kratos4)
Kombate_empate.iniciar()
print("----Guardians of the Ancient Kingdom----")
