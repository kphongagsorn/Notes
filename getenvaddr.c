/*
Another way to retrieve the address of an environment variable is to write a simple helper program. This program can simply use the well-documented getenv() function to look for the first program argument in the environment. If it can't find anything, the program exits with a status message, and if it finds the variable, it prints out the address of it.
getenvaddr.c code
The following shows the getenvaddr.c program's compilation and execution to find the address of the environment variable SHELLCODE.

$ gcc -o getenvaddr getenvaddr.c
$ ./getenvaddr SHELLCODE
SHELLCODE is located at 0xbffffcec

 The code is from Page 147 and 148 of Hacking: The Art of Exploitation, 2nd Edition by Jon Erickson

*/

#include <stdlib.h>

int main(int argc, char *argv[])
{
   char *addr;
   if(argc < 2)
   {
      printf("Usage:\n%s <environment variable name>\n", argv[0]);
      exit(0);
   }
   addr = getenv(argv[1]);
   if(addr == NULL)
      printf("The environment variable %s doesn't exist.\n", argv[1]);
   else
      printf("%s is located at %p\n", argv[1], addr);
   return 0;
}
