#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define   IR_PIN    7
#define   LED       0     
int main()
{
if ( wiringPiSetup() == -1 )
		exit( 1 );
pinMode(LED, OUTPUT);
pinMode(IR_PIN, INPUT);
while(1)
{
	if(!digitalRead(IR_PIN))
	{
		printf("obstacle detected\n");
		digitalWrite(LED, HIGH);
		delay(1000);
		digitalWrite(LED, LOW);
	}
}
}