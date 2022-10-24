
# ? IMPORTAR LIBRERÍAS NECESARIAS
from machine import Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
import bluetooth
from BLE import BLEUART
import time

# ? FUNCIÓN PRINCIPAL
def main():

    # ? INSTANCIA SERVOMOTORES
    servo180 = PWM(Pin(2), freq=50)

    motorPolo1 = PWM(Pin(19), 20000)
    motorPolo2 = PWM(Pin(18), 20000)

    # ? INSTANCIA BLUETOOTH
    ble = bluetooth.BLE()
    name = "ESPCamiloT"
    uart = BLEUART(ble, name)

    # ? INSTANCIA PANTALLA OLED
    i2c = I2C(0, scl=Pin(4), sda=Pin(15))
    ancho, alto = 128, 64
    oled = SSD1306_I2C(ancho, alto, i2c)

    # ? INSTANCIA CASILLAS (FOTORRESISTENCIAS)
    casilla0 = Pin(32, Pin.IN, Pin.PULL_UP)
    casilla1 = Pin(13, Pin.IN, Pin.PULL_UP)
    casilla2 = Pin(23, Pin.IN, Pin.PULL_UP)
    casilla3 = Pin(33, Pin.IN, Pin.PULL_UP)
    casilla4 = Pin(26, Pin.IN, Pin.PULL_UP)
    casilla5 = Pin(25, Pin.IN, Pin.PULL_UP)
    casilla6 = Pin(22, Pin.IN, Pin.PULL_UP)
    casilla7 = Pin(21, Pin.IN, Pin.PULL_UP)
    casilla8 = Pin(12, Pin.IN, Pin.PULL_UP)
    casilla9 = Pin(27, Pin.IN, Pin.PULL_UP)
    casilla10 = Pin(14, Pin.IN, Pin.PULL_UP)

    # ? PEDIR CASILLA PARA APOSTAR
    casillaApostada = 0


    def casilla0Seleccionada(casi):
        cas0 = 0
        return (cas0)

    def casilla1Seleccionada(casi):
        cas1 = 1
        return (cas1)

    def casilla2Seleccionada(casi):
        cas2 = 2
        return (cas2)

    def casilla3Seleccionada(casi):
        cas3 = 3
        return (cas3)

    def casilla4Seleccionada(casi):
        cas4 = 4
        return (cas4)

    def casilla5Seleccionada(casi):
        cas5 = 5
        return (cas5)

    def casilla6Seleccionada(casi):
        cas6 = 6
        return (cas6)

    def casilla7Seleccionada(casi):
        cas7 = 7
        return (cas7)

    def casilla8Seleccionada(casi):
        cas8 = 8
        return (cas8)

    def casilla9Seleccionada(casi):
        cas9 = 9
        return (cas9)

    def casilla10Seleccionada(casi):
        cas10 = 10
        return (cas10)

    # ? DEFINICIÓN DE FUNCIONES PARA CADA RESULTADO
    def resultadoCasilla0():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 0", 0, 10)
        oled.text("     VERDE", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla1():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 1", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla2():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 2", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla3():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 3", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla4():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 4", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla5():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 5", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla6():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 6", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla7():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 7", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla8():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 8", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla9():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 9", 0, 10)
        oled.text("     ROJA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    def resultadoCasilla10():
        oled.fill(0)
        oled.text("*"*16, 0, 0)
        oled.text("   CASILLA 10", 0, 10)
        oled.text("     NEGRA", 0, 20)
        oled.text("USTED APOSTO LA ", 0, 30)
        oled.text("       "+str(casillaApostada), 0, 40)
        oled.text("*"*16, 0, 50)
        oled.show()
        time.sleep(15)

    
    # ? DEFINICIÓN DE FUNCIONES PARA LA APUESTA
    def casillaGana0():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("VERDE", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana1():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana2():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana3():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana4():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana5():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana6():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana7():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana8():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana9():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("ROJA", 37, 42, 1)
        oled.show()
        time.sleep(5)

    def casillaGana10():
        oled.fill(0) 
        oled.text("GANA"+str(casillaApostada), 15, 27, 1)
        oled.text("NEGRA", 37, 42, 1)
        oled.show()
        time.sleep(5)


    def casillaPerder():
        oled.fill(0) 
        oled.text("PERDIO", 15, 27, 1)
        oled.text("APOSTO"+str(casillaApostada), 37, 42, 1)
        oled.show()
        time.sleep(5)

        
    # ? POSICIÓN INICIAL DE LOS MOTORES
    motorPolo1.duty(0)
    motorPolo2.duty(0)

    servo180.duty(90)

    # ? MAPEO MOTORES
    def map(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
        valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
        return valor_mapeado


# ? CICLO INFINITO
    while True:

        print("TAPE UNA CASILLA PARA APOSTAR")

        # ~ SELECCIÓN DE CASILLAS
        if casilla0.value() == 1:
            casillaApostada = casilla0Seleccionada(casillaApostada)

        if casilla1.value() == 1:
            casillaApostada = casilla1Seleccionada(casillaApostada)

        if casilla2.value() == 1:
            casillaApostada = casilla2Seleccionada(casillaApostada)

        if casilla3.value() == 1:
            casillaApostada = casilla3Seleccionada(casillaApostada)

        if casilla4.value() == 1:
            casillaApostada = casilla4Seleccionada(casillaApostada)

        if casilla5.value() == 1:
            casillaApostada = casilla5Seleccionada(casillaApostada)

        if casilla6.value() == 1:
            casillaApostada = casilla6Seleccionada(casillaApostada)

        if casilla7.value() == 1:
            casillaApostada = casilla7Seleccionada(casillaApostada)

        if casilla8.value() == 1:
            casillaApostada = casilla8Seleccionada(casillaApostada)

        if casilla9.value() == 1:
            casillaApostada = casilla9Seleccionada(casillaApostada)

        if casilla10.value() == 1:
            casillaApostada = casilla10Seleccionada(casillaApostada)

        time.sleep(7)
        print("Ya puede quitar el dedo")


        # ~ CICLO PARA MOVER EL SERVO DE 180°
        def on_rx():
            dato = 0
            rx_recibe = uart.read().decode().strip()
            dato = float(rx_recibe)

            if dato == "A":
                dato = int(map(180, 0, 180, 1150, 8100))
                servo180.duty_u16(dato)
                print("Abierto")

            if dato == "C":
                dato = int(map(90, 0, 180, 1150, 8100))
                servo180.duty(dato)
                print("Cerrado")

        # ~ CICLO PARA MOVER EL SERVO DE 360°
            i = 0
            for i in range(700, 1000, 10):
                motorPolo1.duty(i)
                time.sleep(0.2)
                print(i)

            for i in range(1000, 1023, 2):
                motorPolo1.duty(i)
                time.sleep(0.2)
                print(i)

            for i in range(1023, 600, -10):
                motorPolo1.duty(i)
                time.sleep(0.2)
                print(i)

            else:
                uart.write("el valor no aplica")
                print("El valor no aplica")

            servo180.duty(90)
            motorPolo1.duty(0)

        uart.irq(handler=on_rx)


        time.sleep(15)

        # ** VERIFICAR EN QUE CASILLA TERMINÓ 
        if casilla0.value() == 1:
            resultadoCasilla0()

        if casilla1.value() == 1:
            resultadoCasilla1()

        if casilla2.value() == 1:
            resultadoCasilla2()

        if casilla3.value() == 1:
            resultadoCasilla3()

        if casilla4.value() == 1:
            resultadoCasilla4()

        if casilla5.value() == 1:
            resultadoCasilla5()

        if casilla6.value() == 1:
            resultadoCasilla6()

        if casilla7.value() == 1:
            resultadoCasilla7()

        if casilla8.value() == 1:
            resultadoCasilla8()

        if casilla9.value() == 1:
            resultadoCasilla9()

        if casilla10.value() == 1:
            resultadoCasilla10()

        # ** VERIFICAR SI LA APUESTA GANÓ
        if casillaApostada == 0 and casilla0.value()==1:
            casillaGana0()
        else:
            casillaPerder()

        if casillaApostada == 1 and casilla1.value()==1:
            casillaGana1()
        else:
            casillaPerder()

        if casillaApostada == 2 and casilla2.value()==1:
            casillaGana2()
        else:
            casillaPerder()

        if casillaApostada == 3 and casilla3.value()==1:
            casillaGana3()
        else:
            casillaPerder()

        if casillaApostada == 4 and casilla4.value()==1:
            casillaGana4()
        else:
            casillaPerder()

        if casillaApostada == 5 and casilla5.value()==1:
            casillaGana5()
        else:
            casillaPerder()

        if casillaApostada == 6 and casilla6.value()==1:
            casillaGana6()
        else:
            casillaPerder()

        if casillaApostada == 7 and casilla7.value()==1:
            casillaGana7()
        else:
            casillaPerder()

        if casillaApostada == 8 and casilla8.value()==1:
            casillaGana8()
        else:
            casillaPerder()

        if casillaApostada == 9 and casilla9.value()==1:
            casillaGana9()
        else:
            casillaPerder()

        if casillaApostada == 10 and casilla10.value()==1:
            casillaGana10()
        else:
            casillaPerder()


# ? BOTÓN EJECUCIÓN
if __name__ == "__main__":
    main()
