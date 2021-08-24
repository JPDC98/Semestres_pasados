//////////////////////////////////////////////// LIBREIRAS Y DEFINICIONES //////////////////////////////////////////////////////////
#include <stdint.h> // nos permitira interactuar on enteros
#include <stdbool.h> //podremos usar balores boleanos y operaciones con ellos
#include <string.h> // libreira estastandar de inicializaicón
#include <stdio.h>  //libreira de inicialización principal
#include <stdlib.h> // libreria de inicialización que nos permite usar libreiras escenciales
#include <math.h> // libreria que nos permite usar calculos matematicos sin ningun problema

#include "inc/hw_types.h" // libreira que usan las demas libreiras como complemento
#include "inc/hw_memmap.h"// esta es una libreira que mapea los perifericos y nos permite configurarlos
#include "driverlib/gpio.h"// esta libreira nos permite manipular los GPIO
#include "driverlib/pin_map.h"// esto nos permite modificar los pines en especifico de cierto puerto
#include "driverlib/timer.h"// esto nos da la capacidade de usar timers
#include "driverlib/interrupt.h"// libreria que nos da la capacidad de usar interrupciones en nuestro programa
#include "inc/tm4c123gh6pm.h" // libreria que contiene los comandos para la configuraciones de nuestra tiva TM4g123gh6pm
#include "driverlib/sysctl.h"// esta libreria se encarga de sincronizar todo y manipular los relojes internos

#include "driverlib/adc.h"// esta libreria nos ayudara a implementar el conversor analogo digital
#include "driverlib/i2c.h"// nos dota de herramientas para controlar la información de i2c
#include "driverlib/uart.h"// nos da herramientas que nos permiten controlar el envio de información pormedio de UART
#include "float_to_string.h"// nos permite hacer la confersion de una variable flotante a un string

#include "i2c_lcd.h"// libreira desarrollada por José Palacios  carnet 201801216, USAC, para el control del i2c
#include "bluetooth.h"// libreira utilizada para el control del bluetooth desarrollada por José Palacios  carnet 201801216, USAC
#include "i2c_max30100.h"// libreira que nos permite configurar el sensor de ritmo cardiaco y oxigeno en sangre

#define ldc_dir   0x27 // direcion del modulo i2c

///////////////////////////////////////////////////// VARIABLES Y CONSTANTES /////////////////////////////////////////////////////////////////

uint32_t dato[4]; // datos en donde se guarda las muestras
uint8_t dato1[];
int cuenta,cuenta2; // nos funcionara como una variable auxiliar
volatile float valor=0;// valor que servira para mostrarse en la lcd
volatile float temp_total=0;//variable que sera utilizada en el calculo de temperatura
volatile float temp_promedio =0;//variable que sera utilizada en el calculo de temperatura
char valor_f[100],valor_p[100],valor_ox[100];//variable que sera utilizada en el envio de datos
float dato_p,dato_ox;// datos que son para guardar los resultados obtenidos

unsigned int intensidad;
int RED;

////////////////////////////////////////////////////// VOID DE INICIO //////////////////////////////////////////////////////////////

void init_i2c ();// funcion que inicializara el i2c
void init_uart ();//funcion que inicializara el uart
void init_ADC ();// función que inicializara el controlador analogo digital
void adc_inter (); // funcion que inicializara la interrución del analgo digital
void contrl_inter ();// funcion que tendra que controlar la interrupon producida por el ADC
//////////////////////////////////////////////////////////// FUNCION PRINCIPAL //////////////////////////////////////////////////////////////

int main(void)
{
    SysCtlClockSet(SYSCTL_USE_PLL|SYSCTL_OSC_MAIN|SYSCTL_XTAL_16MHZ|SYSCTL_SYSDIV_2_5);// se icicializa el reloj
    init_i2c();// se inicializa el i2c

    I2C_LCD_INIT (I2C0_BASE,ldc_dir);// se inicializa el modulo que comunicara por medio de i2c nuestro controlador con la tiva c
    init_uart ();// se inicializara la transimision de datos por medio de uart, utilizando el modulo bluetooth
    init_ADC ();// se inicializa el adc
    I2C_LCD_PLANTILLA ();// se inicializa una plantilla que despelagara la información
    I2C_M30100_INIT (I2C0_BASE, MAX30100_DIRECCION);// se inicaliza el modulo que tomara la captura de los signos vitales
    adc_inter ();//se activa la interrupción

    while (1){

        I2C_M30100_RESEPCION (MAX30100_INTERRUPCION_ESTADO,1, dato1);
        I2C_M30100_RESEPCION (MAX30100_FIFO_DATOS,4, dato1);
        intensidad = dato1[0];
        intensidad = dato1[1]|intensidad<<8;
  //      ftoa(intensidad,valor_p,0);
    }
}

//////////////////////////////////////////////////////////// Prototipos ////////////////////////////////////////////////////////////////////////
void init_i2c (){
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOB);// se activa el puerto B
    SysCtlPeripheralEnable(SYSCTL_PERIPH_I2C0);// se activa el i2c 0
    GPIOPinConfigure(GPIO_PB2_I2C0SCL);// se configura un reloj
    GPIOPinConfigure(GPIO_PB3_I2C0SDA);// se configura un transmisor de datos
    GPIOPinTypeI2CSCL(GPIO_PORTB_BASE,GPIO_PIN_2);// se  especifica el pin que sera el reloj
    GPIOPinTypeI2C(GPIO_PORTB_BASE,GPIO_PIN_3); // se especifica el pin que sera el transmisor de datos
    I2CMasterInitExpClk(I2C0_BASE, SysCtlClockGet(),false);// se configura la velocidad del relo
}

void init_uart (){
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOC);// se inicializa el puerto C
    SysCtlPeripheralEnable(SYSCTL_PERIPH_UART3);// es inicializa el uart 3
    GPIOPinConfigure(GPIO_PC6_U3RX);// se especifica un receptor el cual no se utilizara
    GPIOPinConfigure(GPIO_PC7_U3TX);// se especifica un transmios el cual nos serviara para enviar los datos obtenidos de los demás perifericos
    GPIOPinTypeUART(GPIO_PORTC_BASE,GPIO_PIN_6|GPIO_PIN_7);// se especifican los pines utilizados en la comunciación uart
    UARTConfigSetExpClk(UART3_BASE,SysCtlClockGet(),9600,(UART_CONFIG_WLEN_8 | UART_CONFIG_STOP_ONE |UART_CONFIG_PAR_NONE)); // se configura el reloj y cuanta información mandara por segundo
    UARTEnable(UART3_BASE); // se activa el uart
}

void init_ADC (){
    GPIOPinTypeADC(GPIO_PORTB_BASE, GPIO_PIN_5);// se activa el pin 5
    SysCtlPeripheralEnable(SYSCTL_PERIPH_ADC0);// se inical el adc 0
    SysCtlPeripheralEnable(SYSCTL_PERIPH_TIMER0);// se activa el time0 que nos seriviara para la interrupción
    TimerConfigure(TIMER0_BASE, TIMER_CFG_A_PERIODIC);// se quiere un muestreo constante
    TimerLoadSet(TIMER0_BASE, TIMER_A,39999);// se especifica el tiempo que debe de tardar en activarse la interrupción
    TimerControlTrigger(TIMER0_BASE, TIMER_A, true);// se activa el dispero de la interrupción
    TimerEnable(TIMER0_BASE, TIMER_A);// se activa el timer finalmente

    ADCSequenceDisable(ADC0_BASE,1);// se desabilita temporalmente el adc
    ADCSequenceConfigure(ADC0_BASE, 1, ADC_TRIGGER_TIMER,0);// se le infomra que timer activara la interrupción
    ADCSequenceStepConfigure(ADC0_BASE,1, 0, ADC_CTL_CH11);// se activa la primera muestra
    ADCSequenceStepConfigure(ADC0_BASE,1, 1, ADC_CTL_CH11);// se configura la segunda muestra
    ADCSequenceStepConfigure(ADC0_BASE,1, 2, ADC_CTL_CH11);// se configura la tercera muestra
    ADCSequenceStepConfigure(ADC0_BASE,1, 3, ADC_CTL_CH11|ADC_CTL_IE|ADC_CTL_END);//se configura la cuarta muestar y que la interupción
    ADCSequenceEnable(ADC0_BASE,1);
}

void adc_inter (){
    ADCIntEnable(ADC0_BASE, 1);//se da aviso que se activo la interrupción
    ADCIntRegister(ADC0_BASE,1,contrl_inter);// se asigna una función que controlara la interrupción
    IntEnable(INT_ADC0SS1);// se activa la interrupción
    IntMasterEnable();// se activa el control general de las interrupciónes
}


void contrl_inter (){
    ADCIntClear(ADC0_BASE,1);// se limpia la interrupción
    ADCSequenceDataGet(ADC0_BASE,1,dato);// se piden las mustras obtenidas del adc
        if (cuenta<=1000){// se muestrea 1000 veces
            valor = ((float)(3.3*(dato[0]+dato[1]+dato[2]+dato[3])/4)/4096)*(100);// aca se obtiene el promedio de temperatura tomando en cuenta que por cada grado tenemos 10mV
            temp_total = temp_total + valor;//se empiaza a sumar todas las muestras obtenidas
            cuenta++;// se aumenta el contador
        }
        else{
           temp_promedio = temp_total/1000;// se saca el promedio de temperatura
           temp_total=0;// se limpia la variable
           cuenta = 0;//y tambien el contador
           dato_p = 78;
           dato_ox = 96;
           ftoa(temp_promedio,valor_f,1);//se pasa de flotante a una cadena de caracteres
           ftoa(dato_p,valor_p,0);//se pasa de flotante a una cadena de caracteres
           ftoa(dato_ox,valor_ox,0);//se pasa de flotante a una cadena de caracteres
           I2C_LCD_PLANTILLA_DAT(valor_f,valor_p,valor_ox);// se despliega en lalantilla a utilizar
           concatenar (valor_f,valor_p,valor_ox);// se manda por bluetooth a la aplicación descrita anteriormente
        }
}
