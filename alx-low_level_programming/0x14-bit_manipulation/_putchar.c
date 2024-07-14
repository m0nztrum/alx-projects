#include "main.h"
#include <unistd.h>
/**
 * _putchar - writes the char to the STDOUT
 * @c - the character to be printed
 *
 * Return - 0 on success. and -1 on error
 */
int _putchar(char c){
    return (write(1, &c, 1));
}
