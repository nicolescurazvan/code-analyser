/*
    This code counts prime numbers in the interval [1, n]
    where n is given as an argument
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int n = atoi(argv[1]), i, j;
    char *isprime = malloc(n + 1);
    memset(isprime, 1, n + 1);
    for (int i = 2; i <= n; i++)
    {
        if (isprime[i] == 1)
        {
            for (int j = 2 * i; j <= n; j += i)
                isprime[j] = 0;
        }
    }

    int s = 0;
    for (i = 2; i <= n; i++)
        s += (int)isprime[i];

    FILE *f = fopen("trubaduru.txt", "w");
    fprintf(f, "There are %d prime numbers in the interval [1, %d]", s, n);
    fclose(f);
    return 0;
}
