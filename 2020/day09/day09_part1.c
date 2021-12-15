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

    const int INSTRUCOES_LEN = 5;
    long long instrucoes [INSTRUCOES_LEN];
    int i = 0;

    while (fgets(buffer, MAX_LENGTH, fp))
    {
        long long valor = atoll(buffer);
        if (i < INSTRUCOES_LEN)
        {
            instrucoes[i] = valor;
            i++;
        }
        else
        {
            bool existe_soma = false;
            int x;
            int y;
            for (x = 0; x < INSTRUCOES_LEN-1; x++)
                for (y = x+1; y < INSTRUCOES_LEN; y++)
                    if (instrucoes[x]+instrucoes[y] == valor)
                    {
                        existe_soma = true;
                    }
            if (existe_soma==true) {
                for (i = 0; i < INSTRUCOES_LEN; i++)
                    instrucoes[i] = instrucoes[i + 1];
                instrucoes[INSTRUCOES_LEN-1] = valor;
            }
            else 
            {
                printf("FALHOU NO %lld\n",valor);
                break;
            }
        }
    }
    return 0;
}