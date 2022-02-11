#include <stdio.h>
#include <string.h>
#include <unistd.h>

int BUFFER=275;

int copy(char* input){
  char buffer[BUFFER];
  strcpy(buffer, input);

}

int main(int argc, char* argv[]){
    /* Main Function*/
	char buf[400];
  printf("Smash The Stack\n");
  //Get the data
 int r;
  r = read(0, buf, 400);  //Save Version
  
  int out = copy(buf);
  printf("Lose :(\n");
  return 0;
}
