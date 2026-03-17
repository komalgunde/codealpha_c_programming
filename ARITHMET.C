#include<stdio.h>
void main()
{
 int a, b, choice;
 float result;
 printf("enter two numbers: ");
 scanf("%d%d", &a, &b);
 printf("\nSelection operation: ");
 printf("\n1. Addition");
 printf("\n2. Substraction");
 printf("\n3. Multiplication");
 printf("\n4. Division");
 printf("\nEnter your choice: ");
 scanf("%d", &choice);
 switch(choice)
 {
  case 1:
       result = a + b;
       printf("\nAddition = %.2f",result);
       break;
  case 2:
       result = a - b;
       printf("\nSubstraction = %.2f",result);
       break;
  case 3:
       result = a * b;
       printf("\nMultiplication = %.2f",result);
       break;
  case 4:
       if(b != 0)
       {
	 result = (float)a / b;
	 printf("\nDivision = %.2f",result);
       }
       else
       {
	 printf("\nError:Division by zero!");
       }
       break;
  default:
       printf("\nInvalid choice!");
 }
}