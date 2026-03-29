/*
   Analisis Númerico 1
   Autor: José Juan Gurrola Cota
   Programa: Programa que resuelve un sistema de ecuaciones nxn con el metodo de 
   eliminación gaussiana;
   02/11/2014
*/
#include <iostream>
#include <cstdlib>
#include<math.h>
#include <fstream>
#define VALOR 30
#define MAXREN 10
#define MAXCOL 10

using namespace std;

void capturar_matriz(int* ,float [MAXREN][MAXCOL]);
void separar_matriz_vector(int n, float [][MAXCOL],float [][10],float [MAXREN][MAXCOL],float [MAXREN]);
void imprimir_vectorseidel(float V[MAXREN],int n);
void iniciarlizar_vector_x(float X[MAXREN],int n){ for(int i=0;i<n;i++)    X[i]=0;}
void calcular_x(float A[MAXREN][MAXREN],float X[MAXREN],float V[MAXREN],float X0[MAXREN],int n);
bool revisar_dominante(float A[MAXREN][MAXREN],int n);
bool calcular_vector_errores(float X[MAXREN],float X0[MAXREN],float E[MAXREN],int n,float tolerancia);
void cambiar_vectores(float X[MAXREN],float X0[MAXREN],int n){ for(int i=0;i<n;i++) X0[i]=X[i]; }
//------------------------------------------------------------------------------
int main()
{
   float X[MAXREN],X0[MAXREN],M[MAXREN][MAXCOL],A1[MAXREN][MAXCOL],V[MAXREN],A[MAXREN][MAXCOL],E[MAXREN],respuesta,tolerancia;
    int n,parar=0;
    bool error=0;
    
    capturar_matriz(&n,M);
    cout<<"Ingrese la tolerancia deseada(ejemplo:0.001): ";
    cin>>tolerancia;
    tolerancia=tolerancia*100;
    
    separar_matriz_vector(n,M,A,A1,V);
    respuesta=revisar_dominante(A,n);
    
    if(respuesta){
        iniciarlizar_vector_x(X0,n);
        for(int i=0;parar!=1;i++){  
            calcular_x(A,X,V,X0,n);
            cout<<endl<<"X"<<i+1<<":"<<endl;
            imprimir_vectorseidel(X,n);
            cout<<endl<<"Error "<<i+1<<":"<<endl;
            error=calcular_vector_errores(X,X0,E,n,tolerancia);
            if(error)   parar=1;
            cambiar_vectores(X,X0,n);     
        }
        cout<<"\nLa respuesta es:\n";
        imprimir_vectorseidel(X,n);    
    }
  else
      cout<<"la matriz NO es diagonalmente dominante"<<endl<<endl<<endl; 
      system("pause");
}
//------------------------------------------------------------------------------
void imprimir_vectorseidel(float V[MAXREN],int n)
{
    for(int i=0;i<n;i++){
        cout<<endl;
        printf("%10.7f",V[i]);    
    }
    cout<<endl;    
}
//------------------------------------------------------------------------------
void capturar_matriz(int *punteron,float M[MAXREN][MAXCOL])
{
    char nom_archivo[VALOR];
    ifstream entrada;
    int n;
    
    cout<<"\n\t\t\t  Metodo de Gauss-Seidel"<<endl<<endl<<endl;
     
    cout<<"Ingrese el Nombre del Archivo : ";
    cin>>nom_archivo;

    entrada.open(nom_archivo,ifstream::in);

    if(!entrada.good()){
        cout<<"\nNo se pudo abrir el archivo ingresado."<<endl;
        system("pause");
        exit(0);
    }
    
    entrada>>n;    
    *punteron=n;              
    for(int i=0;i<n;i++){
       for(int j=0;j<n+1;j++){
          entrada>>M[i][j];   //matriz aumentada
       }
    }
    entrada.close();
}
//------------------------------------------------------------------------------
void separar_matriz_vector(int n,float M[][MAXCOL],float A[MAXREN][MAXCOL],float A1[MAXREN][MAXCOL],float V[MAXREN])
{
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){    
            A[i][j]=M[i][j];
            A1[i][j]=M[i][j];
        }   
    }
    for(int i=0;i<n;i++)    V[i]=M[i][n];
}
//------------------------------------------------------------------------------       
void calcular_x(float A[MAXREN][MAXREN],float X[MAXREN],float V[MAXREN],float X0[MAXREN],int n)
{ 
    float diferencia,elemento;
    
    for(int i=0;i<n;i++){
        diferencia=0;    
        for(int j=0;j<n;j++){
            if(j==i)    j++;
            if(j>i)    elemento=X0[j];
            if(j<i)    elemento=X[j];
            diferencia=diferencia+(A[i][j]*elemento);
        }
         X[i]=(V[i]-diferencia)/A[i][i];
    }    
}   
//------------------------------------------------------------------------------  
bool revisar_dominante(float A[MAXREN][MAXREN],int n)
{
      int dominante=0;
      float suma;

      for(int i=0;i<n;i++){
          suma=0;
          for(int j=0;j<n;j++){
              if(i==j)j++;
              suma=suma+fabs(A[i][j]);
              }
          if(fabs(A[i][i])>fabs(suma))dominante++;
     }
     
     if(dominante=(n-1))return true;
     else return false; 
}  
//------------------------------------------------------------------------------
bool calcular_vector_errores(float X[MAXREN],float X0[MAXREN],float E[MAXREN],int n,float tolerancia)
{ 
     int errores=0;
     
     for(int i=0;i<n;i++){
         E[i]=(fabs(X[i]-X0[i])/fabs(X[i]));
         printf("%10.10f",E[i]*100);    
         cout<<endl;
         if((E[i]*100)<=tolerancia)errores++;
     }   
     
     if(errores==(n-1))return true;
     else return false;    
} 
