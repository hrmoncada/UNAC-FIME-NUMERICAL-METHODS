/*
   Analisis Númerico 1
   Autor: José Juan Gurrola Cota
   Programa: programa que encuentra una aproximacion a la raiz positiva de una funcion por el metodo de la secante
   08/10/2014
*/

#include <iostream>
#include <cstdlib>
#include <math.h>
#include <stdio.h>

using namespace std;

double Fx(double);
double Error(double, double);


main(){
    double x,xa,xaa,p,tol;
    int Nmax;    //numero maximo de iteraciones.

        system("cls");
        cout<<"Programa que encuentra una aproximacion a la raiz positiva de la funcion f(x) = arcsen x - e^-2x\n\n";  
    
    do{//Pedimos al usuario el numero de iteraciones y evaluamos a que sea positivo
       cout<<"Ingresa el numero maximo de iteraciones: ";
       cin>>Nmax;
       if(Nmax<=0) cout<<"El numero maximo de iteraciones tiene que ser mayor a 0\n\n";
    }while(Nmax<=0);
    
    do{ 
        cout<<"Ingresa el numero de cifras significativas para la tolerancia: ";
        cin>>tol;
        if(tol<=0) cout<<"Error numero de cifras significativas incorrecto";                
    }while(tol<=0);
    
    tol=pow(10,-tol);
    
    int i=1; 
    double error=100; 
    xa=0.4f;
    xaa=0.6f;
    
    cout<<"n.........xn-1.........xn..........f(xn-1)......f(xn).......error\n"; 
    while(i<=Nmax){
        
        x=xa-((Fx(xa)*(xa-xaa))/(Fx(xa)-Fx(xaa)));
        
        error=Error(x,xa);

        printf("%d   %10.10f  %10.10f  %10.10f  %10.10f %10.10f \n",i,xa,x,Fx(xa),Fx(x),error);
        
        if(error<tol){
            printf("\n\nEl valor aproximado es: %10.15f\n\n",x);
            i=Nmax+1;
        }
 
        i++;
        xa=x;          
    };
    if(error>tol)    cout<<"Error, no se encontro una aproximacion\n\n";  
    
    system("pause");
}

//----------------------------------------------------------------------
/*
   SALIDA: 
   ENTRADA: el numero a evaluar(x)
*/
double Fx(double x)
{
    return asin(x)-exp(-2*x);
}
//----------------------------------------------------------------------
/*
   SALIDA: el valor del error  relativo aproximado
   ENTRADA: el valor de la aproximacion y el valor de la aproximacion anterior
*/
double Error(double x, double x_ant)
{
    return fabs((x-x_ant)/x); 
}
