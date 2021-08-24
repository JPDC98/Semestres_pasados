/*
 * i2c_max30100.c
 *
 *  Created on: 18/10/2020
 *      Author: jdp_p
 */
#include <stdint.h>
#include <stdbool.h>

#include "inc/tm4c123gh6pm.h"
#include "inc/hw_types.h"
#include "inc/hw_memmap.h"
#include "driverlib/sysctl.h"
#include "driverlib/gpio.h"
#include "driverlib/pin_map.h"

#include "driverlib/i2c.h"
#include "i2c_max30100.h"

uint32_t direccion_port1;
uint8_t direccion_disp1;

uint8_t suma[];
int muestras;

void I2C_M30100_INIT (uint32_t port_I2C , uint8_t direccion_modulo){// esto inicializa el modulo para que capte toda la infomración resivida
    direccion_port1 = port_I2C;
    direccion_disp1 = direccion_modulo;
    I2C_M30100_COMANDO (MAX30100_CONFIGURACION_MODO,MAX30100_PULSO_ACTIVAR );// activa el modo de detecion de pulso
    delayMils(40);
    while(I2CMasterBusy(direccion_port1)){}
    I2C_M30100_COMANDO (MAX30100_INTERRUPCION_ACTIVA, MAX30100_PULSO_LISTO);// activacion del la interrupcicon por pulso
    delayMils(40);
    while(I2CMasterBusy(direccion_port1)){}
    I2C_M30100_COMANDO (MAX30100_CONFIGURACION_LED, MAX30100_ROJO_0|MAX30100_INFRARROJO_50000);// apaga el led y solo deja funcionando el infrarojo
    delayMils(40);
    while(I2CMasterBusy(direccion_port1)){}
    I2C_M30100_COMANDO (MAX30100_CONFIGURACION_SPO2, MAX30100_ALTA_RESOLUCION|MAX30100_PULSO_100_MPS|MAX30100_TIEMPO_LED_1600);// configuración para muestreo rapido de oxigeno en sangre
    delayMils(40);
    while(I2CMasterBusy(direccion_port1)){}
}

void I2C_M30100_COMANDO (uint8_t comando, uint8_t valor){
        while(I2CMasterBusy(direccion_port1)){}
        I2CMasterSlaveAddrSet(direccion_port1, direccion_disp1, false);// envio del maestro para escribir en el esclavo
        I2CMasterDataPut(direccion_port1, comando);// se carga el comando a enviar
        I2CMasterControl(direccion_port1,I2C_MASTER_CMD_BURST_SEND_START);// envio de datos
        while(I2CMasterBusy(direccion_port1)){}// se ve si hay uso del puerto
        I2CMasterDataPut(direccion_port1, valor);//se ingresa la configuración
        I2CMasterControl(direccion_port1,I2C_MASTER_CMD_BURST_SEND_FINISH);// se envia la señal de parada para la emisión de datos
        while(I2CMasterBusy(direccion_port1)){}// se ve si hay uso del puerto
}



void I2C_M30100_RESEPCION (uint8_t comandito,int muestra, uint8_t *deteccion){
    int a;
       int aux_suma=0;
       while(I2CMasterBusy(direccion_port1)){}
       I2CMasterSlaveAddrSet(direccion_port1, direccion_disp1, false);
       I2CMasterDataPut(direccion_port1, comandito);
       I2CMasterControl(direccion_port1, I2C_MASTER_CMD_BURST_SEND_START);
           for(a=0;a<muestras;a++){
               while(I2CMasterBusy(direccion_port1)){}
               I2CMasterSlaveAddrSet(direccion_port1, direccion_disp1, true);
               I2CMasterControl(direccion_port1, I2C_MASTER_CMD_SINGLE_RECEIVE );
               suma[a] = I2CMasterDataGet(direccion_port1);
           }
           for(a=0;a<muestras;a++){
               aux_suma = aux_suma + suma[a];
           }

           deteccion = (aux_suma/muestras);
    }



void delayMils(uint32_t milis) {// fución que ayuda con los retardos
    uint32_t aux=6*1000;
    SysCtlDelay(milis * (SysCtlClockGet()/aux));
}


