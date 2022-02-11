#include <stdio.h>
#include <string.h>

void main(void){
  char theString[15];
  //Copy a String that is longer than the space allocated
  strcpy(theString, "Hello World, This Is A Long String");
  printf("%s", theString);
}
