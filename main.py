
# ? IMPORTAR LIBRERÍAS NECESARIAS
from machine import Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
import time

# ? INSTANCIA PANTALLA OLED
i2c = I2C(0, scl=Pin(18), sda=Pin(19))
ancho, alto = 128, 64
oled = SSD1306_I2C(ancho, alto, i2c)

# ? FUNCIÓN PRINCIPAL 
def main():

    # ? INSTANCIA CASILLAS (FOTORRESISTENCIAS)
    casilla0 = Pin(13, Pin.IN, Pin.PULL_UP)
    casilla1 = Pin(14, Pin.IN, Pin.PULL_UP)
    casilla2 = Pin(12, Pin.IN, Pin.PULL_UP)
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
    colorCasillas = ["VERDE", "ROJA", "NEGRA", "ROJA", "NEGRA",
                     "ROJA", "NEGRA", "ROJA", "NEGRA", "ROJA", "NEGRA"]

    # ? ARRAYS PARA EL VALOR DE CADA CASILLA
    casillasValor = [casilla0.value(), casilla1.value(), casilla2.value(), casilla3.value(), casilla4.value(
    ), casilla5.value(), casilla6.value(), casilla7.value(), casilla8.value(), casilla9.value(), casilla10.value()]

   # ? INSTANCIA BUZZER
    buzzer = PWM(Pin(5))
    notas1 = [369, 277, 329, 369, 329, 277, 493, 277, 369, 277, 329, 369, 329, 277, 493, 277, 369, 261, 329,
              369, 329, 277, 493, 277, 369, 277, 329, 369, 329, 277, 493, 277, 349, 1, 1, 277, 329,
              1, 369, 1, 1, 329, 277, 493, 277, 369, 1, 1, 277, 329, 369, 1, 1
              ]

    def notas1():
        for i in notas1:
            buzzer.freq(i)
            time.sleep(0.2)

    # ? INSTANCIA SERVOMOTORES
    servo180 = PWM(Pin(18), freq=50)
    servo360 = PWM(Pin(19), freq=50)

    # ? PEDIR CASILLA PARA APOSTAR
    casillaApostada0 = input()
    casillaApostada = input("Tape la casilla que desea apostar: ")

    # ? DEFINICIÓN DE FUNCIONES PARA CADA RESULTADO
    def resultadoCasilla0():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 0", 0, 10)
        oled.text("     VERDE", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)
        oled.fill()

    def resultadoCasilla1():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 1", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla2():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 2", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla3():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 3", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla4():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 4", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla5():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 5", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla6():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 6", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla7():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 7", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla8():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 8", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla9():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 9", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla10():
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 10", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+casillaApostada, 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    # ? DEFINICIÓN DE FUNCIONES PARA MOVIMIENTO DE CADA SERVO

    repe = 0
    def movimientoServo180():
        while repe in range(0, 2):
            servo180.duty(0)
            time.sleep_ms(1)
            servo180.duty(180)
            time.sleep_ms(1)
            servo180.duty(0)

    repe2 = 0
    def movimientoServo360():
        while repe2 in range(0, 4):
            servo360.duty(0)
            time.sleep_ms(1)
            servo360.duty(360)
            time.sleep_ms(1)
            servo360.duty(0)

# ? CICLO INFINITO
    while True:
        # ~ REPRODUCCIÓN CANCIÓN
        notas1()

        # ~ CICLO PARA MOVER EL SERVO DE 180°
        movimientoServo180()

        # ~ CICLO PARA MOVER EL SERVO DE 360°
        movimientoServo360()

        time.sleep(15)

        # ** VERIFICAR EN QUE CASILLA TERMINÓ CON IF
        if casilla0.value() == 1:
            resultadoCasilla0()
        else:
            pass
        if casilla1.value() == 1:
            resultadoCasilla1()
        else:
            pass
        if casilla2.value() == 1:
            resultadoCasilla2()
        else:
            pass
        if casilla3.value() == 1:
            resultadoCasilla3()
        else:
            pass
        if casilla4.value() == 1:
            resultadoCasilla4()
        else:
            pass
        if casilla5.value() == 1:
            resultadoCasilla5()
        else:
            pass
        if casilla6.value() == 1:
            resultadoCasilla1()
        else:
            pass
        if casilla7.value() == 1:
            resultadoCasilla7()
        else:
            pass
        if casilla8.value() == 1:
            resultadoCasilla8()
        else:
            pass
        if casilla9.value() == 1:
            resultadoCasilla9()
        else:
            pass
        if casilla10.value() == 1:
            resultadoCasilla10()
        else:
            pass


# ? BOTÓN EJECUCIÓN
button = Pin(15, Pin.IN, Pin.PULL_UP)
if __name__ == "__main__" and button.value() == 0:
    main()