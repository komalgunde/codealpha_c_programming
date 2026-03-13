#include<stdio.h>
void main()
{
 int a,b;
 int add, sub, mul;
 float div;
 printf("enter two numbers: ");
 scanf("%d %d", &a, &b);
 add = a+b;
 sub = a-b;
 mul = a*b;
 div = (float)a/b;
 printf("\nAddition = %d", add);
 printf("\nSubstraction = %d", sub);
 printf("\nMultiflication = %d", mul);
 printf("\nDivision = %.2f", div);
}