/*
 * i2c_lcd.c
 *
 *  Created on: 14/10/2020
 *      Author: jdp_p
 */
#include <stdbool.h>
#include <stdint.h>
#include "driverlib/sysctl.h"
#include "driverlib/i2c.h"
#include "i2c_lcd.h"


uint8_t direccion_disp, datoMS,datoLS;// estos datos nos ayudaran a dividir las variables
uint32_t direccion_port;// se utiliza para asignar direción es
uint8_t coordenadaxy [2][16]={{0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87,0x88,0x89,0x8A,0x8B,0x8C,0x8D,0x8E,0x8F},// se hace un vector que nos hubicara en la cuadricula
                              {0xC0,0xC1,0xC2,0xC3,0xC4,0xC5,0xC6,0xC7,0xC8,0xC9,0xCA,0xCB,0xCC,0xCD,0xCE,0xCF}};

void I2C_LCD_INIT (uint32_t direccion_I2C, uint8_t direccion_LCD){
    direccion_port = direccion_I2C;// se asigna en que puerto estamos
    direccion_disp = direccion_LCD;// se asigna la direción del dispositivo a comunicarnos
    uint8_t aux;
    for (aux=0;aux<3;aux++){
        comando_simple (LCD_8B); // segun la tabla de especificaciones asi se inicializa la lcd
    }
    comando_simple (LCD_4B);//                                                   |
    I2C_LCD_INGRESO_COMANDO (LCD_4B|LCD_2L|LCD_5x_7);//                          |
    I2C_LCD_INGRESO_COMANDO (LCD_ACT);//                                         |
    I2C_LCD_INGRESO_COMANDO (LCD_PUNTERO|LCD_PUNTERO_DER|LCD_PUNTERO_OFF);//     |
    I2C_LCD_INGRESO_COMANDO (LCD_CLEARN);//                                      |
    I2C_LCD_INGRESO_COMANDO (LCD_CUR_INI); //                                    v fin
}

void I2C_LCD_TEXTO (const char *texto){// nos ayudara a concatenar una cadena de caracteres
    while (*texto){
        I2C_LCD_INGRESO_CHAR (*texto);
        texto++;
    }
}

void I2C_LCD_SET_CUR (uint8_t y , uint8_t x){// nos ayudara a enciar los datos al vector que esta al inicio del encabezado
    I2C_LCD_INGRESO_COMANDO (coordenadaxy[y-1][x-1]);
}

void comando_simple (uint8_t comando){// enviamos un solo comando no se necesita dividir datos
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        I2CMasterSlaveAddrSet(direccion_port, direccion_disp, false);
        I2CMasterDataPut(direccion_port, comando|LCD_BT_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_START);// se carga dato sin el Eneable que ingresa la fución
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);
        I2CMasterDataPut(direccion_port, comando|LCD_BT_H|LCD_E_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);// envio de la información con el Eneable para introducir comoando
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);
        I2CMasterDataPut(direccion_port, comando|LCD_BT_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_FINISH);// envio de información sin eneable para que el lcd procese el comando
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);
}


void I2C_LCD_INGRESO_COMANDO (uint8_t dato){
    while(I2CMasterBusy(direccion_port)){}
    datoMS=datoLS=0;
    datoMS= dato & 0xF0;
    datoLS= dato<<4;
///////////////////// Envio de dato Más significativo //////////////////////
    I2CMasterSlaveAddrSet(direccion_port, direccion_disp, false);
    I2CMasterDataPut(direccion_port, datoMS|LCD_BT_H);
    I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_START);// se carga dato sin el Eneable que ingresa la fución
    while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
    delayUs(40);//espera en microsegundos
    I2CMasterDataPut(direccion_port, datoMS|LCD_BT_H|LCD_E_H);
    I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);// se carga datos con eneable activado
    while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
    delayUs(40);//espera en microsegundos
    I2CMasterDataPut(direccion_port, datoMS|LCD_BT_H);
    I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);// se cargga dato sin el eneable activo para que ingrese la fucnión
    while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
    delayUs(40);//espera en microsegundos

///////////////////// Envio de dato menos significativo //////////////////////
    I2CMasterDataPut(direccion_port, datoLS|LCD_BT_H);
    I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);// se carga dato sin el Eneable que ingresa la fución
    while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
    delayUs(40);//espera en microsegundos
    I2CMasterDataPut(direccion_port, datoLS|LCD_BT_H|LCD_E_H);
    I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);
    while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
    delayUs(40);//espera en microsegundos
    I2CMasterDataPut(direccion_port, datoLS|LCD_BT_H);
    I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_FINISH);
    while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
    delayUs(40);//espera en microsegundos
}

void I2C_LCD_INGRESO_CHAR (uint8_t dato1){
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        datoMS=datoLS=0;// separacion del bit ingresado
        datoMS= dato1 & 0xF0;
        datoLS= dato1<<4;
    ///////////////////// Envio de dato Más significativo //////////////////////
        I2CMasterSlaveAddrSet(direccion_port, direccion_disp, false);
        I2CMasterDataPut(direccion_port, datoMS|LCD_BT_H|LCD_RS_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_START);// se introducie el bit inicial
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);//espera en microsegundos
        I2CMasterDataPut(direccion_port, datoMS|LCD_BT_H|LCD_E_H|LCD_RS_H);// se repite pero ahora con el LCD E iniciado para cargar la función deseada
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);//espera en microsegundos
        I2CMasterDataPut(direccion_port, datoMS|LCD_BT_H|LCD_RS_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);// se envia la misma función pero ahora sin el E para que detecte el cambio de estado y acepte el comando enciado
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);//espera en microsegundos
        I2CMasterDataPut(direccion_port, datoLS|LCD_BT_H|LCD_RS_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);// se repite todo pero ahora con el bit menos significativo
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);//espera en microsegundos
        I2CMasterDataPut(direccion_port, datoLS|LCD_BT_H|LCD_E_H|LCD_RS_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_CONT);
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);//espera en microsegundos
        I2CMasterDataPut(direccion_port, datoLS|LCD_BT_H|LCD_RS_H);
        I2CMasterControl(direccion_port, I2C_MASTER_CMD_BURST_SEND_FINISH);// se envia la misma función pero ahora sin el E para que detecte el cambio de estado y acepte el comando enciado
        while(I2CMasterBusy(direccion_port)){}// se ve si hay uso del puerto
        delayUs(40);//espera en microsegundos
}

void I2C_LCD_PLANTILLA (void){// plantilla utilizada para los titulos
    while(I2CMasterBusy(direccion_port)){}
    int a;
    I2C_LCD_TEXTO (" T:'C");// imprime caracteres
    for (a=0;a<1;a++){//indicación de desplazamiento
        I2C_LCD_INGRESO_COMANDO (LCD_CUR_DER);
    }
    I2C_LCD_TEXTO ("PM:");//imprime caracteres
    for (a=0;a<2;a++){//indicación de desplazamiento
        I2C_LCD_INGRESO_COMANDO (LCD_CUR_DER);
    }
    I2C_LCD_TEXTO ("Ox:%");//imprime caracteres
}

void I2C_LCD_PLANTILLA_DAT(char valor1[],char valor2[],char valor3[]){// plantilla utlizada para los valores obtenidos
    int a;
    I2C_LCD_SET_CUR (2,1);
    I2C_LCD_TEXTO (valor1);// imprime el valor

    for (a=0;a<3;a++){//indicación de desplazamiento
        I2C_LCD_INGRESO_COMANDO (LCD_CUR_DER);
    }
    I2C_LCD_TEXTO (valor2);// imprime valor
    for (a=0;a<3;a++){//indicación de desplazamiento
        I2C_LCD_INGRESO_COMANDO (LCD_CUR_DER);
    }
    I2C_LCD_TEXTO (valor3);// imprime valor
}

void delayMs(uint32_t milisegundo) { // tiempo de espera para una mejor comprención de los datos en milisegundos
    uint32_t aux = 6*1000;
    SysCtlDelay(milisegundo * (SysCtlClockGet()/aux));
}

void delayUs(uint32_t microsegundos) {// tiempo de espera para una mejor comprención en microsegundos
    uint32_t aux=6*1000000;
    SysCtlDelay(microsegundos * (SysCtlClockGet()/aux));
}



