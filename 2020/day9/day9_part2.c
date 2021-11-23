#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
    char *filename = "input.txt";
    FILE *fp = fopen(filename, "r");

    if (fp == NULL)
    {
        printf("Error: could not open file %s", filename);
        return 1;
    }
    const int MAX_LENGTH = 256;
    char buffer[MAX_LENGTH];

    long long falhou = 1212510616;
    long long total;
    long long menor;
    long long maior;
    int i = 0;
    int j;
    bool passou = false;

    while (passou == false)
    {
        total = 0;
        j = 0;
        while (fgets(buffer, MAX_LENGTH, fp))
        {
            if (j>=i) 
            {
                long long valor = atoll(buffer);
                if (j==i) 
                {
                    maior = valor;
                    menor = valor;
                }
                if (valor>maior) 
                {
                    maior = valor;
                }
                if (valor<menor) 
                {
                    menor = valor;
                }
                total += valor;
                if (total==falhou) {
                    printf("ENCONTREI: %lld - %lld\n",menor,maior);
                    printf("%lld",menor+maior);
                    passou=true;
                    break;
                }
                if (total>falhou) {
                    break;
                }  
            }
            j++;
        }
        i++;
        rewind(fp);
    }
    return 0;
}