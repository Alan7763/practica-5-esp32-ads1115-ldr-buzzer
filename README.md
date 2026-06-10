# Práctica 5: Lectura del ADS1115 con ESP32-C3 y control de buzzer

## Descripción

Esta práctica implementa la lectura de un convertidor analógico-digital ADS1115 mediante un ESP32-C3 programado en MicroPython. Se utiliza una LDR en un divisor de voltaje como entrada analógica, y el valor leído por el ADS1115 se usa para controlar la frecuencia de un buzzer piezoeléctrico mediante PWM.

## Materiales

- ESP32-C3
- Módulo ADS1115
- LDR
- Resistencia de 10 kΩ
- Buzzer piezoeléctrico pasivo
- Cables Dupont
- Protoboard
- Cable USB
- MicroPython
- Thonny o terminal serial

## Conexiones

### ADS1115

| ADS1115 | ESP32-C3 |
|--------|----------|
| VDD    | 3.3V     |
| GND    | GND      |
| SCL    | GPIO9    |
| SDA    | GPIO8    |
| ADDR   | GND      |

### LDR

La LDR y la resistencia de 10 kΩ forman un divisor de voltaje. El nodo central del divisor se conecta al canal A0 del ADS1115.

### Buzzer

| Buzzer | ESP32-C3 |
|--------|----------|
| Positivo | GPIO4 |
| Negativo | GND |

## Funcionamiento

El ESP32-C3 se comunica con el ADS1115 mediante I2C. El programa lee el valor digital del canal A0 y lo convierte en una frecuencia audible entre 200 Hz y 3000 Hz. Cuando cambia la iluminación sobre la LDR, cambia el voltaje leído por el ADS1115 y también cambia el tono del buzzer.

## Ejecución

1. Cargar MicroPython en el ESP32-C3.
2. Abrir `main.py` en Thonny.
3. Verificar las conexiones del ADS1115, LDR y buzzer.
4. Ejecutar el programa.
5. Observar en la consola los valores del ADC y la frecuencia generada.

## Resultado

Al tapar o iluminar la LDR, el valor leído por el ADS1115 cambia y el buzzer modifica su tono de forma proporcional.
