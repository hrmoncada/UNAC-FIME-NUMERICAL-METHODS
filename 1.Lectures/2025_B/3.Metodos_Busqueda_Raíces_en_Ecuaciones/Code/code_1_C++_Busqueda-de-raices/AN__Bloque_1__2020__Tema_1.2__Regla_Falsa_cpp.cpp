#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

void lecturas(double* , double*, int*);
void regla_falsa(double , double, int);
double eval_funcion(double);
/****************************************************************************/
int main()
{
 double vxi=0.0, vxs=0.0;
 int vn;
 lecturas(&vxi , &vxs , &vn);
 regla_falsa(vxi , vxs, vn);
 
 return 0;
}
/******************************************************************************/

void lecturas(double *xi , double *xs, int *N)
{
 cout<<" - R E G L A   F A L S A - "<<endl;
 cout<<"Digite el extremo inferior (Xi) : "; cin>>*xi;
 cout<<"Digite el extremo superior (Xs) : "; cin>>*xs;
 cout<<"Digite el numero de iteraciones : "; cin>>*N;

 while(*xi>=*xs)
 {
  cout<<"El extremo inferior (xi) debe ser MENOR que el extremo (xs) "<<endl;
  cout<<"Digite el extremo inferior (Xi) : "; cin>>*xi;
  cout<<"Digite el extremo superior (Xs) : "; cin>>*xs;
 }

 while(*N<=2)
 {
  cout<<"La cantidad de iteraciones debe ser positiva (>2) "<<endl;
  cout<<"Digite el numero de iteraciones : "; cin>>*N;
 }
}
/****************************************************************************/

void regla_falsa(double xi , double xs, int N)
{
 double TOL=0.0000001,  xr=0.0, xra=0.0, fxi=0.0 , fxs=0.0, fxr=0.0 ;
 double validador=0.0, exr=0.0, er=0.0, A=0.0 , B=0.0, C=0.0, D=0.0;
 int i = 1;
 cout.precision(10);

 fxi=eval_funcion(xi);    fxs=eval_funcion(xs);
 A = xi - xs;     B = fxs * A;     C = fxi - fxs;     D = B/C;
 xr = xs - D;   cout<<"\n XR : "<<xr;    fxr = eval_funcion(xr);
 
 cout<<"\n"<<"n"<<"\t"<<"Raiz"<<"\t\t\t"<<"f(Raiz)"<<"\t\t\t"<<"Er";

 while(i <= N)
 {
  xra = xr;
  validador = fxi * fxr;

  if(validador < 0) {   xs=xr;    }
  else              {   xi=xr;    }  //todo esto para reajustar el intervalo

  fxi=eval_funcion(xi);    fxs=eval_funcion(xs);
  A = xi - xs;     B = fxs * A;     C = fxi - fxs;     D = B/C;     xr = xs - D;
  fxr=eval_funcion(xr);

  //Calculo del error relativo
  exr = xr - xra;  er = exr/xr; if(er<0){er=er*(-1);}

  //presentacion de resultados iteracion a iteracion 
  cout<<"\n"<<i<<"\t";
  std::cout.setf( std::ios::fixed, std:: ios::floatfield );
  std::cout << xr;
  std::cout.unsetf( std::ios::floatfield );
  std::cout.precision(10);
  std::cout<<"\t\t"; std::cout << fxr;
  std::cout<<"\t\t"; std::cout << er;

  //si se tiene exito:
  if((fxr==0)||(er<TOL))
  {cout<<"\nProcedimiento completado satisfactoriamente\n"; system("pause"); exit(1);}

  i++;
 }
 if((i>N)&&(er>TOL)) {cout<<"\nEl metodo fracaso despues de "<<N<<" iteraciones";}
 cout<<"\n"; system("pause");
}
/****************************************************************************/

//PRIMERA
/*
//Entradas a probar para Raiz: a = 0.5 , b = 2
double eval_funcion(double v)
{
 double r=0.0 , ee=0.0, emx=0.0, logx=0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 logx = log(v);

 r = emx - logx;
 return r;
}
*/

//SEGUNDA
/*
//Entradas a probar para Raiz: a = 0 , b = 2
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) + (4*v*v) - 10;
 return r;
}
*/

//TERCERA
/*
//Entradas a probar para Raiz 1: a = -1   , b = 0
//Entradas a probar para Raiz 2: a =  0.5 , b =  2
double eval_funcion(double v)
{
 double r=0.0 , ee =0.0, emx = 0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 r = emx + (v*v) - 2;
 return r;
}
*/

//CUARTA
/*
//Entradas a probar para Raiz menor positiva: a = 0 , b = 2
double eval_funcion(double v)
{
 double r=0.0 , ee =0.0, emx = 0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 r = (2*emx) - sin(v);
 return r;
}
*/

//QUINTA
/*
//Entradas a probar para Raiz 1: a = -1   , b = 0
//Entradas a probar para Raiz 2: a =  0   , b =  1
//Entradas a probar para Raiz 3: a =  1.5 , b =  2.5
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) - (2*v*v) - v + 1;
 return r;
}
*/

//CASO ESPECIAL
/*
//Entradas a probar para Raiz 1: a = -1.2  , b = -0.8
//Entradas a probar para Raiz 2: a =  0.8  , b =  1.2
double eval_funcion(double v)
{
 double r=0.0 ,
 xd = pow(v,10);
 r = xd - 1;
 return r;
}
*/


//Ejercicio 8.37 del Libro de Chapra
//Encontrar el valor de t para que la velocidad del cohete sea 750 m/s
//f(t) = 2000 * ln[150000 / (150000 - 2700*t)] - (9.81 * t) - 750 = 0
//Entradas a probar para Raiz positiva: a = 20  , b = 25
/*
double eval_funcion(double t)
{
   double r=0.0, v1=0.0, v2= 0.0, v3=0.0, v4= 0.0;
   v1 = 150000 - 2700*t;
   v2 = log(150000 / v1);
   v3 = 2000*v2;
   v4 = 9.81*t;
   
   r =  v3 - v4 - 750;
   return r;
}
*/