/*
   Analisis Númerico 1
   Autor: José Juan Gurrola Cota
   Programa 3: programa que encuentra una aproximacion a la raiz positiva de una funcion por el metodo de BISECCION
   14/09/2014
*/

#include <iostream>
#include <cstdlib>
#include <math.h>
#include <stdio.h>

using namespace std;

double Funcion(double);
double Error(double, double);
int signo(double);

int main(){
    double a,b,p, tolerancia=0.0001;
    int Nmax;    //numero maximo de iteraciones.
    do{    //Pedimos el interbalo [a,b] y evaluamos que f(a) y f(b) tengan signos opuestos y su evaluacion correspondiente.
        system("cls");
        cout<<"Programa que encuentra una aproximacion a la raiz positiva de la funcion f(x) = (e^-x)+(4x^3)-5 (tolerancia de 10^-4)\n\n";
        cout<<"Ingresa el punto 'a' del intervalo: ";
        cin>>a;
        cout<<"Ingresa el punto 'b' del intervalo: ";
        cin>>b;
        if(Funcion(a) < 0 && Funcion(b) < 0){
            cout<<"No es posible encontrar raiz con el intervalo ["<<a<<", "<<b<<"]\n\n\n\n\n\n";
            system("pause");
        }
        if(Funcion(a) > 0 && Funcion(b) > 0){
            cout<<"No es posible encontrar raiz con el intervalo ["<<a<<", "<<b<<"]\n\n\n\n\n\n";
            system("pause");
        }
    }while((Funcion(a) < 0 && Funcion(b) < 0) || (Funcion(a) > 0 && Funcion(b) > 0));

    do{//Pedimos al usuario el numero de iteraciones y evaluamos a que sea positivo
       cout<<"Ingresa el numero maximo de iteraciones: ";
       cin>>Nmax;
       if(Nmax<=0) cout<<"El numero maximo de iteraciones tiene que ser mayor a 0\n\n";
    }while(Nmax<=0);


    int i=1;
    cout<<"\nn       an          bn          pn          f(an)       f(pn)      error"<<endl<<endl; //Encabezado de la tabla
    while(i<=Nmax){
        p=a+((b-a)/2);

        printf("%d   %10.7f  %10.7f  %10.7f  %10.7f  %10.7f  %10.7f\n",i,a,b,p,Funcion(a),Funcion(p),Error(a,b));  //Se imprime la linea de la tabla respectiva a cada iteración

        if(Funcion(p)==0 || Error(a,b)<=tolerancia){ //Revisamos a que lleguemos a una aproximacion apropiada entorno a la tolerancia
            printf("\n\nEl valor aproximado es: %10.7f\n\n",p);
            i=Nmax+1;
        }
        if((signo(Funcion(a))*signo(Funcion(b)))<0){ //Hacemos el intervalo mas pequeño, para esto se verifica si a o b tomaran el valor de p
            b=p;
        }else a=p;

        i+=1;

    };

    if(Error(a,b)>tolerancia){  //Si despues de que el numero de iteraciones no se encuentra un valor menor a la tolerancia, mandamos mensaje de error
            cout<<"\n\n\n\nNo se encontro un numero aproximado con el numero de iteraciones dadas\n\n\n";
        }

    system("pause");
}
//----------------------------------------------------------------------
/*
   SALIDA: el valor de la funcion f(x) = (e^-x)+(4x^3)-5  evaluado en x
   ENTRADA: el numero a evaluar(x)
*/
double Funcion(double x){
    //return (exp(-x))+(4*(pow(x,3)))-5;
    return exp(x)+x;
}
//----------------------------------------------------------------------
/*
   SALIDA: el valor calculado del error
   ENTRADA: el rango [a,b] con el que se calcula el error
*/
double Error(double a, double b){
    return (b-a)/2;
}
//-----------------------------------------------------------------------
/*
   SALIDA: entero con el cual se identifica si es negativo, positivo o 0
   ENTRADA: el numero dado por la funcion "funcion(dobule x)"
*/
int signo(double x){
    if(x<0) return -1;
    if(x=0) return 0;
    if(x>0) return 1;
}
//-----------------------------------------------------------------------

