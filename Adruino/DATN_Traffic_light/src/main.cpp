#include <Arduino.h>
#include <TimerOne.h>
#define		green1	2
#define		yellow1	3
#define		red1	4
#define		green2	5
#define		yellow2	6
#define		red2	7

const uint8_t green_time = 10;
const uint8_t yellow_time = 3;
const uint8_t plus_time = 5;
boolean priority = 0;
int  pc = 0, pc_tmp = 0;
String buff;
volatile uint8_t count = green_time, plus = 0;
void light_control(uint8_t x)
{
	digitalWrite(green1, x & 0x01);
	digitalWrite(yellow1, (x>>1) & 0x01);
	digitalWrite(red1, (x>>2) & 0x01);
	digitalWrite(green2, (x>>4) & 0x01);
	digitalWrite(yellow2, (x>>5) & 0x01);
	digitalWrite(red2, (x>>6) & 0x01);
}

void ISR_timer (void) 
{
    count++;
	digitalWrite(red2, (count & 1) ^ 1);
	Serial.println(static_cast <String> (count));
}

void setup() {

  // put your setup code here, to run once:
  pinMode(green1, OUTPUT);
  pinMode(yellow1, OUTPUT);
  pinMode(red1, OUTPUT);
  pinMode(green2, OUTPUT);
  pinMode(yellow2, OUTPUT);
  pinMode(red2, OUTPUT);

  if(pc) light_control(0x14);
  else light_control(0x41);
  light_control(0x00);
  Serial.begin(9600);
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(ISR_timer);

}
void loop() {
	if (Serial.available()) //Nếu có tín hiệu từ Pi
	{
		buff = Serial.readStringUntil('\r'); //Đọc vào đến khi gặp \r (xuống dòng)
		
		if (buff=="turn on all led")             
		{
			light_control(0xff);    
		}if (buff=="turn off all led")             
		{
			light_control(0x00); 
		}
	}
	
}
/*
// put your main code here, to run repeatedly:
  while (Serial.available())
  {
	  pc_tmp = Serial.read();
  }
  
  if(count > 0)count--;
  delay(1000);
  if(count == 0)
  {
	  
	if(priority) 
	{
		if(pc == '1') pc_tmp = '0';
		else pc_tmp = '1';
		priority = 0;
	}
	if(pc != pc_tmp)
	{
		pc = pc_tmp;
		if(pc == '1') 
		{
			light_control(0x42);
			delay(yellow_time*1000);
			light_control(0x14);
		}else
		{
			light_control(0x24);
			delay(yellow_time*1000);
			light_control(0x41);
		}
		count = green_time;
	  
 	}else
	 {
		 if(plus < 3)
		 {
			count += plus_time;
		 	plus++;
		 }else
		 {
			 plus = 0;
			 priority = 1;
		 }
		 
	 }
	 
  }
*/
