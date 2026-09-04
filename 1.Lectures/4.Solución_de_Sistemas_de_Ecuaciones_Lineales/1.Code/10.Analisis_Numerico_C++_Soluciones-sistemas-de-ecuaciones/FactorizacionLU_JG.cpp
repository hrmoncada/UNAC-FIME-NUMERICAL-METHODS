#include <iostream>
#include <cstdlib>
#include<math.h>
#include <fstream>

#define VALOR 30
#define MAXREN 10
#define MAXCOL 10

using namespace std;

//funciones de factorizacion LU
void imprimir_matriz(float *p, int n);
float hacer_ceroslu(float *p,float *q,int m);
void iniciar_U(float *p,int n,float *q);
void iniciar_L(float *p,int n);
void completar_matriz_L(float *q1,float pivotecero);
void resolver_matrizlu(float *p,float *v,int n,int c);
void imprimir_vector(float *v,int n);


int main()
{
    float *p, *q,*r, *p1, *q1, *k, *k1, *a, *v, *y;
    float pivote, pivotecero, respuesta;
    int i, j, l, m, n, c;

    char nom_archivo[VALOR];
    ifstream entrada;

    cout<<"\t\t\tFactorizacion LU\n\n\n";
    cout<<"\tIngrese el Nombre del Archivo : ";
    cin>>nom_archivo;

    entrada.open(nom_archivo,ifstream::in);

    if(!entrada.good()){
        cout<<"\n\tNo se pudo abrir el archivo ingresado."<<endl;
        exit(0);
    }

    entrada>>n;

    float M[n][n+1],A[n][n],A1[n][n],X[n],U[n][n],L[n][n],Y[n],b[n];
    float I[n][n];

    for(int i=0;i<n;i++){
        for(int j=0;j<n+1;j++){
            entrada>>M[i][j];   //matriz aumentada
        }
    }
    entrada.close();
    //separar matriz
    p=&M[0][0];
    q=&A[0][0];
    a=&A1[0][0];

    for(int i=0;i<n;i++,p++){
        for(int j=0;j<n;j++,p++,q++,a++){
            *q=*p;
            *a=*p;
        }
    }
    q=&A[0][0];

    cout<<"Matriz A: "<<endl;
    imprimir_matriz(q,n);
    cout<<endl;

    p=&M[0][n];
    y=&Y[0];

    for(int i=0;i<n;i++,y++){
        *y=*p;
        p=p+n+1;
    }

    y=&Y[0];

    cout<<"Vector Y: "<<endl;
    imprimir_vector(y,n);
    cout<<endl;

    iniciar_U(&A[0][0],n,&U[0][0]);
    iniciar_L(&L[0][0],n);

    p=&U[0][0];
    q=p+n;
    p=&U[0][0];
    p1=&L[0][0];

    for(int i=0;i<n;i++){
        q1=p1+n;
        q=p+n;
        m=n-i;
        for(int j=0;j<m-1;j++){
            pivotecero=hacer_ceroslu(p,q,n);
                pivotecero=(pivotecero)*(-1);
                *q1=pivotecero;

            q=q+n;
            q1=q1+n;
        }
        p=p+n+1;
        p1=p1+n+1;
    }

    cout<<"Matriz U: "<<endl;
    imprimir_matriz(&U[0][0],n);
    cout<<endl;

    cout<<"Matriz L: "<<endl;
    imprimir_matriz(&L[0][0],n);
    cout<<endl;

    //resolver vector
    v=&Y[0];
    c=n-1;
    for(int i=0;i<c;i++){
        p=&L[0][0]+n;
        p=p+(n*i)+i;
        resolver_matrizlu(p,v,n,c);
        v=v+1;
    }

    cout<<"Vector Y:"<<endl;
    imprimir_vector(&Y[0],n);
    cout<<endl;

    for(int i=n-1;i>=0;i--){
        respuesta=0;
        for(int j=n-1;j>=i+1;j--)
            respuesta=respuesta+(U[i][j]*X[j]);
        X[i]=(Y[i]-respuesta)/U[i][i];
    }
    cout<<"Vector Solucion: "<<endl;
    imprimir_vector(&X[0],n);

    cout<<endl<<endl;
}

float  hacer_ceroslu(float *p,float *q,int m){
    float pivotecero;

    pivotecero=((*q)*(-1))/(*p);

    for(int i=0;i<m;i++,p++,q++)
        *q=(pivotecero*(*p))+(*q);

    return pivotecero;
}

void iniciar_U(float *p,int n,float *q){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++,p++,q++)
        *q=*p;
    }
}

void iniciar_L(float *p,int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++,p++){
            if(i==j)*p=1;
            if(j>i)*p=0;
        }
    }
}



void resolver_matrizlu(float *p,float *v,int n,int c){//i posicion del elemento del vector
     float *w;
     w=v+1;

     for(int i=1;i<=c;i++){
        *w=*w-((*v)*(*p));
        *p=0;
        p=p+n;
        w++;
    }
}

void imprimir_vector(float *v,int m){
     for(int c=0;c<m;c++,v++){
             cout<<*v<<' ';
     }
     cout<<endl;
}

void imprimir_matriz(float *p, int n){
    for(int c=0;c<n;c++){
        for(int b=0;b<n;b++,p++)
            cout<<*p<<'\t';
    cout<<endl;
    }
}

