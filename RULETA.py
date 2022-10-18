
# ? IMPORTAR LIBRERÍAS NECESARIAS
from machine import Pin, PWM
from ssd1306 import SSD1306_I2C
import time
# ? INSTANCIA PANTALLA OLED
i2c = I2C(0, scl=Pin(35), sda=Pin(34))
ancho, alto = 128, 64
oled = SSD1306_I2C(ancho, alto, i2c)

# ? CASILLA QUE EL JUGADOR DESEA APOSTAR
casillaApostada0 = int(input("Tape la casilla que desea apostar"))
casillaApostada = int(input("Tape la casilla que desea apostar"))

# ? INSTANCIA BUZZER
buzzer = PWM(Pin(5))
notas1 = [369, 277, 329, 369, 329, 277, 493, 277, 369, 277, 329, 369, 329, 277, 493, 277, 369, 261, 329,
          369, 329, 277, 493, 277, 369, 277, 329, 369, 329, 277, 493, 277, 349, 1, 1, 277, 329,
          1, 369, 1, 1, 329, 277, 493, 277, 369, 1, 1, 277, 329, 369, 1, 1
          ]


def cancion1():
    for i in notas1:
        buzzer.freq(i)
        time.sleep(0.2)


# ? INSTANCIA SERVOMOTORES
servo360 = PWM(Pin(19), freq=50)
servo180 = PWM(Pin(18), freq=50)

# ? INSTANCIA CASILLAS (FOTORRESISTENCIAS)
casilla0 = Pin(13, Pin.IN, Pin.PULL_UP)
casilla1 = Pin(12, Pin.IN, Pin.PULL_UP)
casilla2 = Pin(14, Pin.IN, Pin.PULL_UP)
casilla3 = Pin(27, Pin.IN, Pin.PULL_UP)
casilla4 = Pin(26, Pin.IN, Pin.PULL_UP)
casilla5 = Pin(25, Pin.IN, Pin.PULL_UP)
casilla6 = Pin(33, Pin.IN, Pin.PULL_UP)
casilla7 = Pin(32, Pin.IN, Pin.PULL_UP)
casilla8 = Pin(23, Pin.IN, Pin.PULL_UP)
casilla9 = Pin(22, Pin.IN, Pin.PULL_UP)
casilla10 = Pin(21, Pin.IN, Pin.PULL_UP)

# ? ARRAYS PARA LA POSICION DE CADA CASILLA
numeroCasillas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colorCasillas = ["verde", "roja", "negra", "roja", "negra",
                 "roja", "negra", "roja", "negra", "roja", "negra"]

# ? ARRAYS PARA EL VALOR DE CADA CASILLA
casillasValor = [casilla0.value(), casilla1.value(), casilla2.value(), casilla3.value(), casilla4.value(
), casilla5.value(), casilla6.value(), casilla7.value(), casilla8.value(), casilla9.value(), casilla10.value()]

# ? IMPRESION DEL RESULTADO EN PANTALLA OLED PARA EL FOR
def casillaGanadora():
    oled.text("CASILLA"+numeroCasillas[i], 15, 27, 1)
    oled.text("COLOR"+colorCasillas[i], 37, 42, 1)
    oled.show()
    time.sleep(120)

# ? LED DE PRUEBA
led1 = Pin(33, Pin.OUT)

# ? CICLO INFINITO
while True:
    # ~ REPRODUCCIÓN CANCIÓN
    cancion1()

    # ~ CICLO PARA MOVER EL SERVO DE 180°
    # for i in range(0,180,-180):

    # ~ CICLO PARA MOVER EL SERVO DE 360°
    # for i in range(0,360,-360):
    # cuando esté en el valor 1 debe esperar 30s para poder calcular la casilla donde cayó

    time.sleep(30)
    # ~ VERIFICAR EN QUE CASILLA TERMINÓ CON IF DENTRO DEL FOR
    for i in range(0, 11):
        if casillasValor[i] == 1:
            casillaGanadora()
            time.sleep(15)
        else:
            pass

    # ** VERIFICAR EN QUE CASILLA TERMINÓ CON IF
    if casilla0.value() == 1:
        oled.text("CASILLA 0", 15, 27, 1)
        oled.text("VERDE", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla1.value() == 1:
        oled.text("CASILLA 1", 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla2.value() == 1:
        oled.text("CASILLA 2", 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla3.value() == 1:
        oled.text("CASILLA 3", 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla4.value() == 1:
        oled.text("CASILLA 4", 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla5.value() == 1:
        oled.text("CASILLA 5", 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla6.value() == 1:
        oled.text("CASILLA 6", 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla7.value() == 1:
        oled.text("CASILLA 7", 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla8.value() == 1:
        oled.text("CASILLA 8", 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla9.value() == 1:
        oled.text("CASILLA 9", 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
    if casilla10.value() == 1:
        oled.text("CASILLA 10", 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(15)
    else:
        pass
