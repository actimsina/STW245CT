#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int BUFFER=150;

void win(void){
    /*Win Condition
      We Want to jump here
    */
    printf("\n ===== Win ===== \n\n");
    system("/bin/sh");  //Tradition to get a shell
}

void lose(void){
    /* Lose Condition */
    printf("Current Memory Address is %p\n",lose);
    printf("Aim for %p\n", win);    
    printf("Lose :(\n");
}

int main(int argc, char* argv[]){
    /* Main Function*/
    
    //Pointer to the lose function
    void (*fp)(void) = lose;

    char buffer[BUFFER];
    printf("Overflow the Buffer\n");

    if (argc != 2){
	printf("Overflow the buffer\n");
	printf("Hint! Try `python -c \"print 'A'*100\"`\n");
	return -1;
    }
      
    memcpy(buffer, argv[1], strlen(argv[1]));
    printf("Off to %p\n",fp);
    fp();
    
    return 0;
}
