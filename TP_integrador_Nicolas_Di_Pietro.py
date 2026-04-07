# Ejercicio 1— “Caja del Kiosco”

# Objetivo: Simular una compra con validaciones y cálculo de total.

# Requisitos

# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con
# .isdigit() en while).
# 3. Por cada producto (usar for):
# • Pedir precio (entero, validar .isdigit()).
# • Pedir si tiene descuento S/N (validar con while, aceptar s o n en
# cualquier mayuscula/minuscula).
#  Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar:
# • Total sin descuentos
# • Total con descuentos
# • Ahorro total
# • Promedio por producto (usar float y formatear con :.2f, ejem:
# x = 3.14159
# print(f"{x:.2f}"))

# Validaciones obligatorias
# • Sin try/except.
# • No aceptar vacío en nombre (si queda vacío, es error).
# • Cantidad > 0 (si ingresa 0, volver a pedir).

# Salida esperada (ejemplo)

# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100 Descuento (S/N): s
# Producto 2 - Precio: 50 Descuento (S/N): n
# Producto 3 - Precio: 200 Descuento (S/N): s
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.67

print("EJERCICIO 1 - Caja del Kiosco\n")

total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0
productos_finales = ""
numero_producto = 0


while True:
    nombre_cliente = input("Ingrese nombre de cliente: ").strip()

    if (nombre_cliente.replace(" ","").isalpha() and nombre_cliente != ""):
        break
    else:
        print("Error, ingrese un nombre válido (sólo letras)")

while True:

    cantidad_productos_str = input("Ingrese la cantidad de productos que desea comprar: ")
    
    if (cantidad_productos_str.isdigit() and cantidad_productos_str!= "" and int(cantidad_productos_str) > 0 ):
        cantidad_productos = int(cantidad_productos_str)
        break
    else:
        print("Ingrese un valor válido")
   
for i in range(cantidad_productos):
    while True:
        precio_producto_str = input(f"Indiquie el precio del producto {i + 1}: ")

        if (precio_producto_str.replace(".","").isdigit() and precio_producto_str != ""and float(precio_producto_str) > 0):
            precio_producto = float(precio_producto_str)
            break
        else:
            print("Ingrese un valor válido")
    while True:
        descuento_producto = input("Ingrese si tiene descuento (S) o no tiene descuento (N): ").strip()
        descuento = 0

        if descuento_producto.isalpha():
            match descuento_producto.lower():
                case "s":
                    print("El producto tiene un %10 de descuento")
                    descuento = precio_producto * 0.10
                    break
                case "n":
                    print("No hay descuentos disponibles para este producto")
                    descuento = 0
                    break
                case _:
                    print("Ingrese las letras correspondientes (S/N)")
        else:
            print("Ingrese un carácter válido (solo letras)")

    total_con_descuentos += (precio_producto - descuento)
    total_sin_descuentos += precio_producto
    ahorro_total += descuento
    productos = (f"Producto {numero_producto} - Precio: ${precio_producto} Descuento (S/N): {descuento_producto.capitalize()}\n")
    productos_finales += productos
    numero_producto += 1

promedio_por_producto = float(total_sin_descuentos / cantidad_productos)

print("\n")    
print("=" * 60)

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")

print("=" * 60)

print(productos_finales)
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto comprado: ${promedio_por_producto:.2f}")

print("=" * 60)

print("FIN EJERCICIO N° 1\n")


# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

# Objetivo: Login con intentos + menú de acciones con validación estricta.

# Requisitos

# 1. Definir credenciales fijas en el código:
# • usuario correcto: "alumno"
# • clave correcta: "python123"

# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:

# 1. Ver estado de inscripción (mostrar “Inscripto”)
# 2. Cambiar clave (pedir nueva clave y confirmación; deben
# coincidir)
# 3. Mostrar mensaje motivacional (1 frase)
# 4. Salir

# 5. Validación del menú:
# • Debe ser número (.isdigit())
# • Debe estar entre 1 y 4

# Cambio de clave
# • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
# rechazar.

# Salida esperada
# Intento 1/3 - Usuario: alumno
# Clave: xxx
# Error: credenciales inválidas.
# Intento 2/3 - Usuario: alumno
# Clave: python123
# Acceso concedido.
# 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir
# Opción: a
# Error: ingrese un número válido.
# Opción: 5
# Error: opción fuera de rango.
# 3
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# Opción: 2
# Nueva clave: 123
# Error: mínimo 6 caracteres.
# ...

print("EJERCICIO 2 - Acceso al Campus y Menú Seguro\n")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0

menu = ""

while intentos <= 3 :
    print(f"Intento {intentos + 1}/3")
    usuario = input("Ingrese nombre de usuario: ").strip()
    clave = input("Ingrese clave: ").strip()
    if (usuario.lower() != usuario_correcto or clave != clave_correcta):
        print(f"Usuario: {usuario}")
        print(f"Clave: xxx")
        print("Error: credenciales inválidas")

    intentos += 1

    if intentos == 3:
        print("Cuenta bloqueada")
        break
    
    elif (usuario.lower() == usuario_correcto and clave == clave_correcta):
        print("Acceso concedido.")

        while menu != "4":
            menu = input("""
Menú 
1) Estado
2) Cambiar calve
3) Mensaje
4) Salir 
""").strip()

            if menu.isdigit():
                match int(menu):
                    case 1:
                        print("Estado: Inscripto")
                    case 2:
                        nueva_clave = input("Ingrese nueva clave: ").strip()
                        if len(nueva_clave) >= 6:
                            print("clave modificada")
                            clave_correcta = nueva_clave
                            print(clave_correcta)
                        else:
                            print("Error: mínimo 6 caracteres")
                    case 3:
                        print("Programación 1")
                        print("TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN")
                    case 4:
                        print("Sesión finalizada. Hasta Luego")
                    case _:
                        print("Opción fuera de rango")
            else:
                print("Ingrese un número válido")
        break        
    
print("FIN EJERCICIO N° 2\n")

# ✅ Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

# Contexto

# Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:

# • Lunes: 4 turnos
# • Martes: 3 turnos

# Reglas

# 1. Pedir nombre del operador (solo letras).

# 2. Menú repetitivo hasta salir:

# 1. Reservar turno
# 2. Cancelar turno (por nombre)
# 3. Ver agenda del día
# 4. Ver resumen general
# 5. Cerrar sistema

# 3. Reservar:

# • Elegir día (1=Lunes, 2=Martes).
# • Pedir nombre del paciente (solo letras).
# • Verificar que no esté repetido en ese día (comparando con las variables
# ya cargadas).
# • Guardar en el primer espacio libre (ej. lunes1, lunes2…).

# 4. Cancelar:

# • Elegir día.
# • Pedir nombre del paciente (solo letras).
# • Si existe, cancelar y dejar el espacio vacío ("").

# 5. Ver agenda del día:
# 4
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN

# • Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
# está vacío.

# •. Resumen general:
# • Turnos ocupados y disponibles por día.
# • Día con más turnos (o empate).
# Restricciones
# • ❌ No listas, no diccionarios, no sets, no tuplas.
# • ✅ Se permite usar "" como “vacío”.
# • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).

print("EJERCICIO 3 - (Alta) — “Agenda de Turnos con Nombres\n")        

print("-" * 60)
nombre_operador = input("Ingrese nombre del operador: ").strip().capitalize()

paciente = ""

lunes = ""
martes = ""

turnos_lunes = 0
turnos_martes = 0

menu = ""

if nombre_operador.replace(" ", "").isalpha():
    print("-" * 60)
    print("Ingresando al sistema...")
    print(f"Bienvenido {nombre_operador}")
    print("-" * 60)
    while menu != "5":
        menu = input("""
    --------------------------------------------------------
    Menú
    1) Reservar Turno
    2) Cancelar turno (por nombre)
    3) Ver agenda del día
    4) Ver resumen general
    5) Cerrar sistema
    --------------------------------------------------------
    """).strip()
        if menu.isdigit():
            match int(menu):
                case 1:
                    print("Reservar: ")
                    print("-" * 60)
                    reserva = input("Elegir día (1=Lunes 2=Martes): ").strip()
                    nombre_paciente = input("Ingrese nombre del paciente: ").strip().capitalize()
                    print("-" * 60)
                    if nombre_paciente.replace(" ", "").isalpha() or reserva.isdigit():
                        if int(reserva) == 1:
                            if (turnos_lunes < 4):
                                if (nombre_paciente not in lunes):
                                    paciente = nombre_paciente + ", "
                                    lunes += paciente 
                                    turnos_lunes += 1
                                    print("Turno reservado")
                                else:
                                    print("El paciente ya cuenta con un turno reservado para este día")
                            else:
                                print("Lo sentimos, ya no hay mas turnos disponibles para esta fecha")
                        if int(reserva) == 2:
                            if (turnos_martes < 3):
                                if (nombre_paciente not in martes):
                                    paciente = nombre_paciente + ", "
                                    martes += paciente 
                                    turnos_martes += 1
                                    print("Turno reservado")
                                else:
                                    print("El paciente ya cuenta con un turno reservado para este día")
                            else:
                                print("Lo sentimos, ya no hay más turnos disponibles para esta fecha")
                    else:
                        print("Error, ingrese una opción valida para el día (sólo numeros) o un nombre válido (solo letras)")            
                case 2:
                    print("Cancelar: ")
                    print("-" * 60)
                    reserva = input("Elegir día (1=Lunes 2=Martes): ").strip()
                    nombre_paciente = input("Ingrese nombre del paciente: ").strip().capitalize()
                    print("-" * 60)
                    if nombre_paciente.replace(" ", "").isalpha() or reserva.isdigit():
                        if int(reserva) == 1:
                            if (turnos_lunes > 0):
                                if (nombre_paciente in lunes):
                                    paciente = nombre_paciente + ", "
                                    lunes = lunes.replace(paciente, "")
                                    turnos_lunes -= 1
                                    print("Turno cancelado")
                                else:
                                    print("El paciente no cuenta con un turno reservado para este día")
                        if int(reserva) == 2:
                            if (turnos_martes > 0):
                                if (nombre_paciente in martes):
                                    paciente = nombre_paciente + ", "
                                    martes = martes.replace(paciente, "")
                                    turnos_martes -= 1
                                    print("Turno cancelado")
                                else:
                                    print("El paciente ya cuenta con un turno reservado para este día")
                    else:
                        print("Error, ingrese una opción valida para el día (sólo numeros) o un nombre válido (solo letras)")
                case 3:
                    print("Ver agenda: ")
                    agenda = input("Elegir día (1=Lunes 2=Martes): ").strip()
                    if agenda.isdigit():
                        if int(agenda) == 1:
                            print("AGENDA LUNES")
                            nombre = ""
                            numero_turno = 1
                            for letra in lunes:
                                if letra == ",":
                                    print(f"Turno {numero_turno}: {nombre.strip()}")
                                    nombre = ""
                                    numero_turno += 1
                                else:
                                    nombre += letra
                            for i in range(numero_turno, 5):
                                print(f"Turno {i}: (libre)")
                        if int(agenda) == 2:
                            print("AGENDA MARTES")
                            nombre = ""
                            numero_turno = 1
                            for letra in martes:
                                if letra == ",":
                                    print(f"Turno {numero_turno}: {nombre.strip()}")
                                    nombre = ""
                                    numero_turno += 1
                                else:
                                    nombre += letra
                            for i in range(numero_turno, 4):
                                print(f"Turno {i}: (libre)")
                case 4:
                    print("RESUMEN GENERAL")
                    libres_lunes = 4 - turnos_lunes 
                    libres_martes = 3 - turnos_martes
                    print(f"Turnos ocupados lunes: {turnos_lunes}")
                    print(f"Turnos disponibles lunes: {libres_lunes}")
                    print(f"Turnos ocupados martes: {turnos_martes}")
                    print(f"Turnos disponibles martes: {libres_martes}")
                    if turnos_lunes == turnos_martes:
                        print("Ambos días cuentan con la misma cantidad de turnos ocupados")
                    elif turnos_lunes > turnos_martes:
                        print(f"El día con más turnos es el lunes")
                    else:
                        print(f"El día con más turnos es el martes")
                case 5:
                    print("Cerrrando sitema. Hasta luego")
                case _:
                    print("Error ingrese una opción válida")
        else:
            print("Error, ingrese una opción válida")            
else:
    print("Error ingrese un nombre de operador válido (solo letras)")

print("FIN EJERCICIO N° 3\n")

# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
# limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
# • energia = 100
# • tiempo = 12
# • cerraduras_abiertas = 0
# • alarma = False
# • codigo_parcial = ""
# Validaciones obligatorias
# • No usar try/except.
# 5
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# • Pedir nombre del agente y validar con .isalpha() en un while.
# • Validar opciones del menú y cualquier número pedido con .isdigit() en un
# while.
# • El juego debe funcionar con estructuras secuenciales, condicionales y
# repetitivas (puede usar funciones propias del lenguaje como .lower(), len(),
# formateo, etc.).
# Regla anti-spam (muy importante)
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al
# iniciar:
# ✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
# • se cobra el costo normal (-20 energía, -2 tiempo),
# • NO abre cerradura, y
# • se activa la alarma automáticamente (alarma = True) porque “la cerradura se
# trabó”.
# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
# Menú de acciones (se repite mientras el juego siga)
# El juego continúa mientras:
# • energia > 0, tiempo > 0, cerraduras_abiertas < 3
# • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
# o Si la energía está por debajo de 40, hay “riesgo de alarma”:
# ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
# o Si no hay alarma, abre 1 cerradura.
# o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y
# no abre.
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
# o Debe usar un for de 4 pasos mostrando progreso.
# o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
# o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
# todavía faltan.
# 6
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
# energía extra)
# Regla de bloqueo por alarma ✓
# • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
# se bloquea y se pierde.
# Condiciones de fin  ✓
# • Si cerraduras_abiertas == 3 → VICTORIA
# • Si energia <= 0 o tiempo <= 0 → DERROTA
# • Si se bloquea por alarma → DERROTA (bloqueo)

print("EJERCICIO 4 — “Escape Room: La Bóveda”\n")   

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
menu = ""
forzar_seguidas = 0


nombre_agente = input("Ingrese su nombre de agente: ").strip().capitalize()


while not nombre_agente.isalpha():
    print("Error Agente, ingrese un nombre válido")
    nombre_agente = input("Ingrese su nombre de agente: ").strip().capitalize()

print(f"Bienvenido Agente {nombre_agente}")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    menu = input(f"""
    --------------------------------------------------------
                     
    Estado actual:
    Energia: {energia}
    Tiempo: {tiempo}
    Cerraduras abiertas: {cerraduras_abiertas}

    --------------------------------------------------------

    Menú
    1) Forzar cerradura (costo: -20 energía, -2 tiempo)
    2) Hackear panel (costo: -10 energía, -3 tiempo)
    3) Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
                     
    --------------------------------------------------------
    """).strip()
    if menu.isdigit():
            match int(menu):
                case 1:
                    energia -= 20
                    tiempo -= 2
                    forzar_seguidas += 1
                    if forzar_seguidas == 3:
                        print("ALARMA ACTIVADA")
                        print("La cerradura se trabó")
                        alarma = True
                    elif energia < 40:
                        print("Riesgo de alarma")
                        numero = input("Ingrese un número del 1 al 3").strip()
                        if numero.isdigit():
                            if int(numero) == 3:
                                alarma = True
                            elif int(numero) == 1 or int(numero) == 2:
                                cerraduras_abiertas += 1
                                print("Se ha abierto una cerradura")
                            else:
                                print("Error Agente, ingrese un valor válido")
                    else:
                         cerraduras_abiertas += 1
                case 2:
                    forzar_seguidas = 0
                    energia -=10
                    tiempo -= 3
                    for i in range(0,4):
                        letra = "A"
                        codigo_parcial += letra
                    if cerraduras_abiertas < 3:
                        if len(codigo_parcial) >= 8:
                                cerraduras_abiertas += 1
                                codigo_parcial = ""
                case 3:
                    forzar_seguidas = 0
                    tiempo -= 1
                    if alarma == True:
                        energia -= 10
                    if energia > 0:
                        energia += 15
                        if energia > 100:
                            energia = 100
                case _:
                    print("Error, ingrese una opción válida")
    else:
        print("Error, ingrese una opción válida")             

    if cerraduras_abiertas == 3:
        print("VICTORIA")
        break

    if energia <= 0 or tiempo <= 0:
        print("DERROTA")
        break

    if alarma == True and tiempo <= 3 and cerraduras_abiertas <= 3:
        print("Sistema Bloqueado")
        print("DERROTA")
        break

print("FIN EJERCICIO N° 3\n")

# Ejercicio 5 — “Escape Room:"La Arena del
# Gladiador"
# 1. Descripción del Escenario
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
# usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
# objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.
# Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
# control (if/elif/else), ciclos (while y for) y validación de datos estricta.
# 2. Requerimientos Técnicos
# A. Tipos de Datos
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
# • • String: Para el nombre del jugador.
# • • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
# • • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).
# 7
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# • • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
# B. Reglas de Validación (¡Importante!)
# • • No está permitido usar bloques try / except.
# • • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
# • • Para validar números, debes usar el método .isdigit() dentro de un ciclo
# while.
# 3. Flujo del Programa
# Paso 1: Configuración del Personaje
# El programa inicia pidiendo el nombre del Gladiador.
# • • Validación: El nombre solo puede contener letras. Si el usuario ingresa números,
# símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a
# preguntar hasta que sea válido.
# Paso 2: Inicialización de Estadísticas
# 8
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# El programa debe definir las variables iniciales (sin preguntar al usuario):
# • • Vida del Gladiador: 100 (int)
# • • Vida del Enemigo: 100 (int)
# • • Pociones de Vida: 3 (int)
# • • Daño base "Ataque Pesado": 15 (int)
# • • Daño base del enemigo: 12 (int)
# • • Turno Gladiador : True (booleano)
# Paso 3: El Ciclo de Combate
# El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0
# puntos de vida.
# Turno del Jugador:
# Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3
# opciones:
# 1. Ataque Pesado
# 2. Ráfaga Veloz (Requiere uso de for)
# 3. Curar
# • Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo
# ingresado sea un número (.isdigit()).
# 2. Verificar que el número sea 1, 2 o 3.
# o Si falla alguna validación, mostrar mensaje de error y volver a pedir.
# Lógica de las Acciones:
# Acción A: Ataque Pesado (Opción 1)
# • • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador
# realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
# • • Resta el daño a la vida del enemigo.
# • • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
# Acción B: Ráfaga Veloz (Opción 2)
# • • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
# • • El bucle debe repetirse 3 veces (usando range).
# • • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.
# • 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".
# •
# Acción C: Curar (Opción 3)
# 9
# Programación 1
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# • • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
# • • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el
# enemigo ataca igual).
# Turno del Enemigo:
# Justo después de tu acción, el enemigo ataca automáticamente.
# • • Resta el daño base del enemigo (12) a tu vida.
# • • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
# Paso 4: Fin del Juego
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
# • • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
# • • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."
# 4. Ejemplo de Ejecución (Consola)
# Plaintext
# --- BIENVENIDO A LA ARENA ---
# Nombre del Gladiador: Leonidas1
# Error: Solo se permiten letras.
# Nombre del Gladiador: Leonidas
# === INICIO DEL COMBATE ===
# Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3
# Elige acción:
# 1. Ataque Pesado
# 2. Ráfaga Veloz
# 3. Curar
# Opción: A
# Error: Ingrese un número válido.
# Opción: 2
# >> ¡Inicias una ráfaga de golpes!
# > Golpe conectado por 5 de daño
# > Golpe conectado por 5 de daño
# > Golpe conectado por 5 de daño
# >> ¡El enemigo contraataca por 12 puntos!
# === NUEVO TURNO ===
# Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3
# ... 

player_hp = 100
enemy_hp = 100
heal_potion = 3
player_base_ad = 15
enemy_base_ad = 12
player_turno = True
menu = ""

nombre_jugador = input("Ingrese su nombre, Gladiador: ").strip().capitalize()

while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_jugador = input("Ingrese su nombre, Gladiador: ").strip().capitalize()

print("--- BIENVENIDO A LA ARENA ---")
print(f"Gladiador {nombre_jugador}")

while player_hp > 0 and enemy_hp > 0:
    if player_turno == True:
        print("=== INICIO DEL COMBATE ===")
    else:
        print("=== NUEVO TURNO ===")
    menu = input(f"""
Gladiador {nombre_jugador} HP: {player_hp}
Pociones de vida: {heal_potion}
--------------------------------------------
Enemigo HP: {enemy_hp}

Elige acción:
1) Atacar Ataque pesado
2) Ráfaga veloz
3) Tomar poción 
""").strip()
        
    if menu.isdigit():
        match int(menu):
            case 1:
                print(". . . .")
                if enemy_hp < 20:
                    print("¡Critical Hit!")
                    critical_hit = float(player_base_ad * 1.5)
                    enemy_hp -= critical_hit
                    print(f">¡Atacaste al enemigo por {critical_hit} puntos de daño!")
                    if enemy_hp > 0:
                        player_hp -= enemy_base_ad 
                        print(f">>¡El enemigo contraataca por {enemy_base_ad} puntos de daño!")
                    player_turno = False 
                else:
                    enemy_hp -= player_base_ad
                    print(f">¡Atacaste al enemigo por {player_base_ad} puntos de daño!")
                    if enemy_hp > 0:  
                        player_hp -= enemy_base_ad 
                        print(f">>¡El enemigo contraataca por {enemy_base_ad} puntos de daño!")
                        player_turno = False 
            case 2:
                print(". . . .")
                print(">>Inicias una ráfaga de golpes")
                for i in range(3):
                    enemy_hp -= 5
                    print("> Golpe conectado por 5 de daño")
                if enemy_hp > 0:    
                    player_hp -= enemy_base_ad 
                    print(f">>¡El enemigo contraataca por {enemy_base_ad} puntos de daño!")
                player_turno = False 
            case 3:
                if heal_potion > 0:
                    player_hp += 30
                    heal_potion -= 1
                    print(f" +30 HP")
                    player_hp -= enemy_base_ad
                    print(f">>¡El enemigo contraataca por {enemy_base_ad} puntos de daño!")
                else:
                    print("¡No quedan pociones!")
                    player_hp -= enemy_base_ad
                    print(f">>¡El enemigo contraataca por {enemy_base_ad} puntos de daño!")
                    player_turno = False
            case _:
                print("Error, ingrese una opción válida")
    else:
        print("Error, ingrese una opción válida")

if player_hp > 0:
    print(f"¡VICOTRIA {nombre_jugador} ha ganado la batalla!")

if player_hp <= 0:
    print(f"¡DERROTA. Has caído en combate! ") 