/*
   Analisis Númerico 1
   Autor: José Juan Gurrola Cota
   Programa 3: programa que encuentra una aproximacion a la raiz positiva de una funcion por el metodo Newton-Raphson
   30/09/2014
*/

#include <iostream>
#include <cstdlib>
#include <math.h>
#include <stdio.h>

using namespace std;

double Fx(double);
double FFx(double);
double Error(double, double);


main(){
    double x,xa,p,tol;
    int Nmax;    //numero maximo de iteraciones.

        system("cls");
        cout<<"Programa que encuentra una aproximacion a la raiz positiva de la funcion f(x) = e^(x-1)-5x^3\n\n";  
    
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
    xa=1.0f;
    
    
    cout<<"n          xn          f(x)                 f'(x)             Error\n"; 
    while(i<=Nmax){
        x=xa-(Fx(xa)/FFx(xa));
        
        error=Error(x,xa);

        printf("%d   %10.14f  %10.14f  %10.14f  %10.14f \n",i,x,Fx(x),FFx(x),error);
        
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
    return exp(x-1)-(5*pow(x,3));
}
//----------------------------------------------------------------------
/*
   SALIDA: 
   ENTRADA: el numero a evaluar(x)
*/
double FFx(double x)
{
    return exp(x-1)-(15*pow(x,2));
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
    
    
    
