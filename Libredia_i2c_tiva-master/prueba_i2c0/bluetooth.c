/*
 * bluetooth.c
 *
 *  Created on: 16/10/2020
 *      Author: jdp_p
 */
#include <stdbool.h>
#include <stdint.h>
#include "driverlib/sysctl.h"
#include "driverlib/i2c.h"
#include "inc/hw_memmap.h"
#include "driverlib/uart.h"
#include "inc/hw_memmap.h"
#include "i2c_lcd.h"

void bluetooth_char (uint8_t caracter){
    while (UARTBusy(UART3_BASE)){}///regresa un valor booleano si esta enviando o no el mensaje
    UARTEnable(UART3_BASE);
    UARTCharPut(UART3_BASE,caracter);// caga un caracter para ser enviado
    UARTDisable(UART3_BASE); // espera el final de la transmisión y la para
}

void bluetooth_text (const char *cadena){// envio de cadena de caracteres
    while (*cadena){
           bluetooth_char (*cadena);//envia datos uno por uno
           cadena++;
    }
}

void concatenar (char variable1[] ,char variable2[],char variable3[]){// concatencaicón de variables que se mandaran para la aplicación
    bluetooth_text (variable1);// se envia la variable
    bluetooth_char (',');// la aplicación reconoce el termino de una cadena de caracteres por una ','
    bluetooth_text (variable2);// se envia la variable
    bluetooth_char (',');// la aplicación reconoce el termino de una cadena de caracteres por una ','
    bluetooth_text (variable3);// se envia la variable
    delayMs(900);// tiempo de espera
}



