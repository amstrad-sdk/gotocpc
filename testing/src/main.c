// Demo program for ccz80
// Open this file in ccz80 IDE and use compile option
// or compile in command line with ccz80 HelloWord.ccz80 /org=#A000

include "cpc464.ccz80";

byte i;

cls();
for (i = 1; i <= 10; ++i)
{
  locate(i, i);
  prints("Hello World");
}
return;
