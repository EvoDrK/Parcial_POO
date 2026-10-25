from Personajes import (
    Guerrero,
    Mago,
    Arquero,
    Kombate as ClaseCombate
)
#ejemplo de funcionamiento del programa
print("|---------------------------|")

arthas = Guerrero(
    "Arthas",
    100,
    30,
    20
)

gandalf = Mago(
    "Gandalf",
    80,
    40,
    10
)

Kombate = ClaseCombate(
    arthas,
    gandalf
)

Kombate.iniciar()
print("|----------------------------|")

#casos de  prueba
print()
#caso 1: Creación correcta de los tres tipos de personajes.
try: 
    guerrero = Guerrero("Arthas", 100, 30, 15)
    mago = Mago("Gandalf", 80, 40, 10)
    arquero = Arquero("Bl4ck", 90, 35, 12)
    
    print("caso 1: se crearon los 3 tipos de personaje")
    
    print("Guerrero:")
    guerrero.mostrar_estado()
    print("Mago:")
    mago.mostrar_estado()
    print("Arquero:")
    arquero.mostrar_estado()
    
except Exception as e:
    print(e)

#caso 2: Rechazo de personajes con vida superior a 100 o negativa.
try:
    print(" Caso 2: Rechazo de personajes con vida superior a 100 o negativa.")
    Guerrero("Arthas", -10, 30, 15)

except Exception as e:
    print("caso 2:", e)
    
#caso 3: Rechazo de nombres vacíos.
try:
    print(" Caso 3: Rechazo de nombres vacíos.")
    Guerrero("", 100, 30, 15)
except Exception as e:
    print("caso 3: ", e)

#caso 4: Rechazo de ataques y defensas inválidos.
try: 
    print(" Caso 4: Rechazo de ataques y defensas inválidos.")
    Guerrero("Arthas", 100, -10, 15)
except Exception as e:
    print("caso 4: ", e)
    
#caso 5: Aplicación correcta de la habilidad del Guerrero.
print("caso 5: habilidad del Guerrero")
guerrero_atacante = Guerrero("Arthas", 100, 30, 10)
mago_objetivo = Mago("Gandalf", 80, 20, 10)

print("vida inicial del mago: ", mago_objetivo.vida)

dano = guerrero_atacante.atacar(mago_objetivo)

print("daño causado: ", dano)
print("vida final del mago: ", mago_objetivo.vida)


#caso 6: Aplicación correcta del ataque del Mago ignorando defensa.
print("caso 6: ataque del mago que ignora la defensa")

mago_atacante = Mago("Gandalf", 100, 40, 10)
guerrero_objetivo = Guerrero("Arthas", 100, 20, 50)

print("vida inicial: ", guerrero_objetivo.vida)

dano = mago_atacante.atacar(guerrero_objetivo)

print("daño causado: ", dano)
print("vida final del guerrero: ", guerrero_objetivo.vida)

#caso 7: Aplicación correcta del disparo crítico del Arquero.
print("caso 7: disparo critico del arquero")

arquero_atacante = Arquero("Bl4ck", 100, 35, 10)
guerrero_objetivo = Guerrero("Arthas", 100, 20, 15)

print("vida inicial: ", guerrero_objetivo.vida)

dano = arquero_atacante.atacar(guerrero_objetivo)

print("daño critico: ", dano)
print("vida final del guerrero: ", guerrero_objetivo.vida)

#caso 8: Imposibilidad de tener vida negativa.

guerrero_derrotado = Guerrero("Arthas", 10, 20, 10)
guerrero_derrotado.recibir_danio(100)
print("caso 8: vida del personaje: ", 
      guerrero_derrotado.vida)

#caso 9: Imposibilidad de atacar estando derrotado.

try: 
    guerrero_derrotado.atacar(arquero_atacante)
except Exception as e:
    print("caso 9: imposibilidad: ", e)

print()

#caso 10: Ejecución de un combate completo.
#caso 11: Identificación correcta del ganador.
print("caso 10 y 11: combate completo y identificacion del ganador")
print("|----------------------------|")
arthas_2 = Guerrero("Arthas", 100, 30, 20)

gandalf_2 = Mago("Gandalf", 80, 40, 10)

combate_2 = ClaseCombate(arthas_2, gandalf_2)
combate_2.iniciar()
print("|----------------------------|")

print()

#caso 12: Finalización de un combate sin daño mediante empate técnico.
print("caso 12: empate tecnico")
print("|----------------------------|")

arthas_3 = Guerrero("Arthas", 100, 10, 100)

arthas_4 = Guerrero("Dark Arthas", 100, 10, 100)

combate_empate = ClaseCombate(arthas_3, arthas_4)
combate_empate.iniciar()
print("|-----------------------------|")