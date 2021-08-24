 /*
 * I2C_LCD.h
 *
 *  Created on: 6/10/2020
 *      Author: José Daniel Palacios Cojolón
 *
BT-------------> 1: Base del transistor, enciende la led de la LCD
E--------------> 0/1: Confirmación de funcion o caracter ingresado
RW-------------> 0: Modo de lectura o escritura (En este caso siempre estaremos en modo escritura)
RS-------------> 0/1: valor bajo es para ingresar funciones, valor alto caracteres
D7/D6/D5/D4----> pines los cuales ingresaran funciones o caracteres

El Modulo I2C tiene como pines de entrada SCL/SDA/VCC/GND y como pines de salida
MS---D7/D6/D5/D4/BT/E/RW/RS---LS

La LCD cuenta con los pines de conceción  D7/D6/D5/D4/D3/D2/D1/D0/BT/E/RW/RS
dado que los datos a enviar son 8 bits y el modulod solo transmite 4 se dividira
la informacion de 2 paquetes de 4 bits cada envio, se enviara primero el primer
nivel más significativo y luego el segundo nivel menos significativo.

D7/D6/D5/D4/BT/E/RW/RS----> primer envio
D3/D2/D1/D0/BT/E/RW/RS----> segundo envio
 */

#ifndef DEBUG_I2C_LCD_H_
#define DEBUG_I2C_LCD_H_

///////////-------- Control de LCD------/////////////

#define LCD_BT_H            0x08//se activa el transistor que enciende la pantalla
#define LCD_E_H             0x04//aceptador de funciones
#define LCD_RW_H            0x02//modo escritura o de envio
#define LCD_RS_H            0x01// modo de escritura o de comando

///////////-Funciones y configuraciónes //////////////////////

////////////////// comandos simples de 4 bit ////////////////////
#define LCD_8B              0x30    //Programa la lcd a 8bit
#define LCD_4B              0x20    //Programa la lcd a 4bit
#define LCD_2L              0x08    //Lcd trabaja con 2 lineas
#define LCD_1L              0x00    //Lcd trabaja con 1 linea
#define LCD_5x_7            0x00    //cuadricula del caracter es de 5x8
#define LCD_5x_10           0x04    //cuadricula del caracter es de 5x10

//////////////////// comandos de 8 bit ///////////////////////

#define LCD_ACT_CUR_BLK     0x0F    //Activa pantalla, cursor y blink
#define LCD_ACT_CUR         0x0E    //Activa pantalla y cursor
#define LCD_ACT_BLK         0x0D    //Activa pantalla y blink
#define LCD_ACT             0x0C    //Activa pantalla, sin blink y sin cursor

#define LCD_PUNTERO         0x04    //Activa el puntero
#define LCD_PUNTERO_DER     0x02    //Arrastra puntero derecha
#define LCD_PUNTERO_IZQ     0x00    //Arrastra puntero izquierda
#define LCD_PUNTERO_ON      0x01    //Apaga punter
#define LCD_PUNTERO_OFF     0x00    //Enciende puentero


#define LCD_CLEARN          0x01    //Limpia pantalla
#define LCD_CUR_IZQ         0x10    //Mueve cursor izquierda
#define LCD_CUR_DER         0x14    //Mueve cursor dereche
#define LCD_CORR_IZQ        0x18    //Corre toda la pantalla a la izquierda
#define LCD_CORR_DER        0x1C    //Corre toda la pantalla a la derecha
#define LCD_CUR_INI         0x02    //Corre el cursor y pantalla a lac cordenenada [1,1]

/////////////////////// FUNCIONES A UTILIZAR ///////////////////////////////

void I2C_LCD_INIT (uint32_t direccion_I2C, uint8_t direccion_LCD ); // Inicializa el I2C y la LCD
void I2C_LCD_TEXTO (const char *texto); //Imprime una cadena de caracteres
void I2C_LCD_SET_CUR (uint8_t y , uint8_t x);// pocicionamiento del cursor en la cuadricula
void comando_simple (uint8_t comando);// envio de un solo comando sin nececidad de dividir información

void I2C_LCD_INGRESO_COMANDO (uint8_t dato); //Conmuta entre E=0 ---> E=1 ---> E=0 para dejar grabada la información en la LCD
void I2C_LCD_INGRESO_CHAR (uint8_t dato1);// ingresar caracter
void I2C_LCD_PLANTILLA (void);// ingresar plantilla prefabricada
void I2C_LCD_PLANTILLA_DAT(char valor1[],char valor2[],char valor3[]);// mostrar datos
void delayMs(uint32_t milisegundo);//  retardo en milisegundos
void delayUs(uint32_t microsegundos);// retardo en microsegundos

#endif /* DEBUG_I2C_LCD_H_ */
