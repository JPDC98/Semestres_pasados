/*
 * i2c_max30100.h
 *
 *  Created on: 18/10/2020
 *      Author: jdp_p
 */

#ifndef DEBUG_I2C_MAX30100_H_
#define DEBUG_I2C_MAX30100_H_

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define MAX30100_DIRECCION              0x57       // Dirección del MAX30100 en el formato que espera la librería Wire de Arduino

#define MAX30100_INTERRUPCION_ESTADO    0x00       // Descripción del estado que ha producido la interrupción
#define MAX30100_INTERRUPCION_ACTIVA    0x01       // Descripción de los eventos que producen una interrupción

#define MAX30100_FIFO_PUNTERO_ESCRITURA 0x02       // FIFO_WR_PTR Puntero a la dirección en la que se grabará la siguiente lectura (Es recomendable inicializarlo a cero al empezar)
#define MAX30100_FIFO_DESBORDAMIENTO    0x03       // OVF_COUNTER Contador de las lecturas almacenadas en la FIFO que no se han leído
#define MAX30100_FIFO_PUNTERO_LECTURA   0x04       // FIFO_RD_PTR Puntero al valor que toca leer. Se actualiza automáticamente y se puede escribir, además de leerse, para releer valores
#define MAX30100_FIFO_DATOS             0x05       // FIFO_DATA Datos que toca leer (la dirección de la FIFO apuntada por MAX30100_FIFO_PUNTERO_LECTURA)

#define MAX30100_CONFIGURACION_MODO     0x06       // Establece la manera en la que funciona el MAX30100 en sus diferentes aspectos. Por medio de este registro, además de determinar el modo de medida (latido o pulso frente a SPO2) se pasa al modo de ahorro de energía, se resetea y se pide la medida de la temperatura
#define MAX30100_CONFIGURACION_SPO2     0x07       // Determina la precisión de las medidas: activa la resolución de 16 bits, configura la frecuencia de muestreo y la duración del pulso de los LED (que indirectamente determina la resolución de la conversión analógica a digital)
#define MAX30100_CONFIGURACION_LED      0x09       // Almacena la corriente de los led rojo (4 bits más significativos) e infrarrojo (4 bits menos significativos)

#define MAX30100_TEMPERATURA_ENTERO     0x16       // TINT Parte entera de la temperatura medida
#define MAX30100_TEMPERATURA_FRACCION   0x17       // TFRAC Parte fraccionaria de la la temperatura medida (dieciseisavos de grado Celsius)
#define MAX30100_TEMPERATURA            0x16       // Como los dos registros son consecutivos, se suelen leer en una misma operación, para lo que resulta más claro llamarlos simplemente TEMPERATURA

#define MAX30100_VERSION                0xFE       // REV_ID Versión del MAX30100
#define MAX30100_IDENTIFICADOR          0xFF       // PART_ID Código de identificación del MAX30100


// Bits indicadores de los tipos de interrupción (registros MAX30100_INTERRUPCION_ESTADO y MAX30100_INTERRUPCION_ACTIVA)

#define MAX30100_FIFO_CASI_LLENA        0x80       // A_FULL La memoria está casi llena (queda espacio para una lectura)
#define MAX30100_TEMPERATURA_LISTA      0x40       // TEMP_RDY Se puede leer la temperatura (temperatura lista)
#define MAX30100_PULSO_LISTO            0x20       // HR_RDY Se puede leer el pulso
#define MAX30100_LED_LISTOS             0x10       // SPO2_RDY Se pueden leer los LED
#define MAX30100_ENCENDIDO              0x01       // PWR_RDY El MAX30100 ha terminado el ciclo de encendido y está listo para utilizarse


// Bits del modo de funcionamiento MAX30100_CONFIGURACION_MODO

#define MAX30100_APAGAR                 0x80      // SHDN Apagar el MAX30100 (iniciar el modo de ahorro de energía)
#define MAX30100_RESETEAR               0x40       // RESET Resetear el MAX30100
#define MAX30100_TEMPERATURA_ACTIVAR    0x08       // TEMP_EN Iniciar la lectura de la temperatura (solamente se lee una vez y cambia automáticamente el valor de este bit por cero)
#define MAX30100_PULSO_ACTIVAR          0x02       // MODE(1) Establecer el modo de lectura de pulso (informar del latido del corazón en lugar de la luz de los LED reflejada)
#define MAX30100_LED_ACTIVAR            0x03       // MODE(2) Establecer el modo de lectura de la luz reflejada por los LED (en lugar del latido del corazón)

// //bits del registro de spo2

#define MAX30100_ALTA_RESOLUCION        0x40       // SPO2_HI_RES_EN

// Bits de configuración de lectura del pulso MAX30100_CONFIGURACION_SPO2

#define MAX30100_PULSO_50_MPS           0x00       // 50 muestras por segundo. Leer el pulso (latido del corazón) 50 veces por segundo
#define MAX30100_PULSO_100_MPS          0x04       // 100 muestras por segundo
#define MAX30100_PULSO_167_MPS          0x08       // 167 muestras por segundo
#define MAX30100_PULSO_200_MPS          0x0C       // 200 muestras por segundo
#define MAX30100_PULSO_400_MPS          0x10       // 400 muestras por segundo
#define MAX30100_PULSO_600_MPS          0x14       // 600 muestras por segundo
#define MAX30100_PULSO_800_MPS          0x18       // 800 muestras por segundo
#define MAX30100_PULSO_1000_MPS         0x1C       // 1000 muestras por segundo. Leer el pulso (latido del corazón) 1000 veces por segundo

//control del ancho de pulso del led registro spo2

#define MAX30100_TIEMPO_LED_200         0x00 // Mantener los LED encendidos 200 µs (ancho del pulso = 200 µs)
#define MAX30100_TIEMPO_LED_400         0x01 // Mantener los LED encendidos 400 µs
#define MAX30100_TIEMPO_LED_800         0x02 // Mantener los LED encendidos 800 µs
#define MAX30100_TIEMPO_LED_1600        0x03 // Mantener los LED encendidos 1600 µs (ancho del pulso = 1600 µs)


// Configuración de la corriente de los LED MAX30100_CONFIGURACION_LED

#define MAX30100_ROJO_0                 0x00    // Corriente del LED rojo = 0 µA
#define MAX30100_ROJO_4400              0x10    // Corriente del LED rojo = 4400 µA
#define MAX30100_ROJO_7600              0x20    // Corriente del LED rojo = 7600 µA
#define MAX30100_ROJO_11000             0x30    // Corriente del LED rojo = 11000 µA
#define MAX30100_ROJO_14200             0x40    // Corriente del LED rojo = 14200 µA
#define MAX30100_ROJO_17400             0x50    // Corriente del LED rojo = 17400 µA
#define MAX30100_ROJO_20800             0x60    // Corriente del LED rojo = 20800 µA
#define MAX30100_ROJO_24000             0x70    // Corriente del LED rojo = 24000 µA
#define MAX30100_ROJO_27100             0x80    // Corriente del LED rojo = 27100 µA
#define MAX30100_ROJO_30600             0x90    // Corriente del LED rojo = 30600 µA
#define MAX30100_ROJO_33800             0xA0    // Corriente del LED rojo = 33800 µA
#define MAX30100_ROJO_37000             0xB0    // Corriente del LED rojo = 37000 µA
#define MAX30100_ROJO_40200             0xC0    // Corriente del LED rojo = 40200 µA
#define MAX30100_ROJO_43600             0xD0    // Corriente del LED rojo = 43600 µA
#define MAX30100_ROJO_46800             0xE0    // Corriente del LED rojo = 46800 µA
#define MAX30100_ROJO_50000             0xF0    // Corriente del LED rojo = 50000 µA

#define MAX30100_INFRARROJO_0            0x00   // Corriente del LED infrarrojo = 0 µA
#define MAX30100_INFRARROJO_4400         0x01   // Corriente del LED infrarrojo = 4400 µA
#define MAX30100_INFRARROJO_7600         0x02   // Corriente del LED infrarrojo = 7600 µA
#define MAX30100_INFRARROJO_11000        0x03   // Corriente del LED infrarrojo = 11000 µA
#define MAX30100_INFRARROJO_14200        0x04   // Corriente del LED infrarrojo = 14200 µA
#define MAX30100_INFRARROJO_17400        0x05   // Corriente del LED infrarrojo = 17400 µA
#define MAX30100_INFRARROJO_20800        0x06   // Corriente del LED infrarrojo = 20800 µA
#define MAX30100_INFRARROJO_24000        0x07   // Corriente del LED infrarrojo = 24000 µA
#define MAX30100_INFRARROJO_27100        0x08   // Corriente del LED infrarrojo = 27100 µA
#define MAX30100_INFRARROJO_30600        0x09   // Corriente del LED infrarrojo = 30600 µA
#define MAX30100_INFRARROJO_33800        0x0A   // Corriente del LED infrarrojo = 33800 µA
#define MAX30100_INFRARROJO_37000        0x0B   // Corriente del LED infrarrojo = 37000 µA
#define MAX30100_INFRARROJO_40200        0x0C   // Corriente del LED infrarrojo = 40200 µA
#define MAX30100_INFRARROJO_43600        0x0D   // Corriente del LED infrarrojo = 43600 µA
#define MAX30100_INFRARROJO_46800        0x0E   // Corriente del LED infrarrojo = 46800 µA
#define MAX30100_INFRARROJO_50000        0x0F   // Corriente del LED infrarrojo = 50000 µA
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static const uint8_t FIX_IR_CURRENT = 0x20;
//////////////////////////////////////////////////////// FUNCIONES //////////////////////////////////////////////////////////////////////////

void I2C_M30100_INIT (uint32_t port_I2C , uint8_t direccion_modulo);//inicialización
void I2C_M30100_COMANDO (uint8_t comando, uint8_t valor);//envio de comandos
void I2C_M30100_RESEPCION (uint8_t comandito,int muestra, uint8_t *deteccion);//resepción de información
void delayMils(uint32_t milis);//funcion de retardo

#endif /* DEBUG_I2C_MAX30100_H_ */
