/*
   Analisis Númerico 1
   Autor: José Juan Gurrola Cota
   Programa 3: programa que encuentra una aproximacion a la raiz positiva de una funcion por el metodo de PUNTO FIJO
   26/009/2014
*/

#include <iostream>
#include <cstdlib>
#include <math.h>
#include <stdio.h>

using namespace std;

double Fx(double);
double Gx(double);
double Error(double, double);

int main(){
    double a,b,x,p,tol;
    int Nmax;    //numero maximo de iteraciones.
    do{    //Pedimos el interbalo [a,b] y evaluamos que f(a) y f(b) tengan signos opuestos y su evaluacion correspondiente.
        system("cls");
        cout<<"Programa que encuentra una aproximacion a la raiz positiva de la funcion f(x) = 3x^2 - e^x en un intervalo [a,b]\n\n";  
        cout<<"Ingresa el punto 'a' del intervalo: ";
        cin>>a;     
        cout<<"Ingresa el punto 'b' del intervalo: ";
        cin>>b;
        if(Fx(a) < 0 && Fx(b) < 0){ 
            cout<<"No es posible encontrar raiz con el intervalo ["<<a<<", "<<b<<"]\n\n\n\n\n\n";
            system("pause");
        }
        if(Fx(a) > 0 && Fx(b) > 0){ 
            cout<<"No es posible encontrar raiz con el intervalo ["<<a<<", "<<b<<"]\n\n\n\n\n\n"; 
            system("pause");
        }  
    }while((Fx(a) < 0 && Fx(b) < 0) || (Fx(a) > 0 && Fx(b) > 0));
    
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
    x=(a+b)/2;
    cout<<"n          pn                  f(pn)          Error\n"; 
    while(i<Nmax){
        p=Gx(x);
        
        error=Error(p,x);

        printf("%d   %10.15f  %10.15f  %10.15f \n",i,x,p,error );
        
        if(error<tol){
            printf("\n\nEl valor aproximado es: %10.15f\n\n",p);
            i=Nmax+1;
        }
        x=p;
        i++;          
    };
    if(error>tol)    cout<<"Error, no se encontro una aproximacion\n\n";  
    
    system("pause");
}

//----------------------------------------------------------------------
/*
   SALIDA: el valor de la funcion f(x) = (3x^2)-e^x  evaluado en x
   ENTRADA: el numero a evaluar(x)
*/
double Fx(double x)
{
    return (3*x*x)-(exp(x));
}
//----------------------------------------------------------------------
/*
   SALIDA: el valor de la funcion g(x) = sqrt(e^x/3)=x
   ENTRADA: el numero a evaluar(x)
*/
double Gx(double x)
{
    return sqrt((exp(x))/3);
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
    
    
    
