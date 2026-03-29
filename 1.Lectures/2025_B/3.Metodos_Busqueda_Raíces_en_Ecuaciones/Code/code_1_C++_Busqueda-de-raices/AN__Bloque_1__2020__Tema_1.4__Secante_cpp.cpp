#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

void lecturas(double* , double* , int*);
void secante(double , double , int);
double eval_funcion(double);
/*******************************************************************************/
int main()
{
 double vx0, vx1;
 int vn;
 lecturas(&vx0 , &vx1 , &vn);
 secante(vx0 , vx1, vn);

 return 0;
}
/*******************************************************************************/

void lecturas(double *x0 ,  double *x1 , int *N)
{
 cout<<" - S E C A N T E - "<<endl;
 cout<<"Digite Xo : "; cin>>*x0;
 cout<<"Digite X1 : "; cin>>*x1;
 cout<<"Digite el numero de iteraciones : "; cin>>*N;

 while(*N<=2)
 {
  cout<<"La cantidad de iteraciones debe ser positiva (>2) "<<endl;
  cout<<"Digite el numero de iteraciones : "; cin>>*N;
 }
}
/*******************************************************************************/

void secante(double x0 , double x1 , int N)
{
 double TOL=0.0000001,  xr=0.0, xra=0.0, fx0=0.0 , fx1=0.0, fxr=0.0 ;
 double exr=0.0, er=0.0, A=0.0 , B=0.0, C=0.0, D=0.0;
 int i = 1;
 cout.precision(10);

 fx0=eval_funcion(x0);    fx1=eval_funcion(x1);
 A = x0 - x1;     B = fx1 * A;     C = fx0 - fx1;     D = B/C;   xr = x1 - D;
 cout<<"\n XR : "<<xr;    fxr = eval_funcion(xr);
 cout<<"\n"<<"n"<<"\t"<<"Raiz"<<"\t\t\t"<<"f(raiz)"<<"\t\t\t"<<"Er";

 while(i <= N)
 {
   xra = xr;
   x0 = x1;   x1 = xr;  //reajuste
   fx0=eval_funcion(x0);    fx1=eval_funcion(x1);
   A = x0 - x1;     B = fx1 * A;     C = fx0 - fx1;     D = B/C;     xr = x1 - D;
   fxr=eval_funcion(xr);

  //Calculo del error relativo
  exr = xr - xra;  er = exr/xr; if(er<0){er=er*(-1);}

  //presentacion de resultados iteracion a iteracion 
  cout<<"\n"<<i<<"\t";
  std::cout.setf( std::ios::fixed, std:: ios::floatfield );
  std::cout << xr<<"\t";
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
/*******************************************************************************/

//EJEMPLO
//Entradas a probar para Raiz: Xo = -0.5 , X1 = 0.5
/*
double eval_funcion(double v)
{
 double r=0.0 , ee=0.0, emx=0.0;
 ee = pow(2.718281828,v*v); emx = 1/ee;
 r = emx - v;
 return r;
}
*/


//PRIMERA
//Entradas a probar para Raiz: Xo =  3 , X1 =  1.5
//Entradas a probar para Raiz: Xo = 35 , X1 = 30   (¿Sirven?)
/*
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
//Entradas a probar para Raiz: Xo =  0 , X1 =  1
/*
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) + (4*v*v) - 10;
 return r;
}
*/


//TERCERA
//Entradas a probar para Raiz 1: Xo = 0   , X1 = -0.5
//Entradas a probar para Raiz 2: Xo = 0.5 , X1 =  1
/*
double eval_funcion(double v)
{
 double r=0.0 , ee =0.0, emx = 0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 r = emx + (v*v) - 2;
 return r;
}
*/


//CUARTA
//Entradas a probar para Raiz: Xo =  2 , X1 =  1.2
/*
double eval_funcion(double v)
{
 double r=0.0 , ee =0.0, emx = 0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 r = (2*emx) - sin(v);
 return r;
}
*/


//QUINTA
//Entradas a probar para Raiz 1: Xo =  -0.3 , X1 = -0.6  
//Entradas a probar para Raiz 2: Xo =     0 , X1 =  0.3
//Entradas a probar para Raiz 3: Xo =  1.5  , X1 =  2
/*
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) - (2*v*v) - v + 1;
 return r;
}
*/


//CASO ESPECIAL
//Entradas a probar para Raiz 1: Xo =  0.8 , X1 =  0.9
//Entradas a probar para Raiz 2: Xo = -0.8 , X1 = -0.9
/*
double eval_funcion(double v)
{
 double r=0.0, xd;
 xd = pow(v,10);
 r = xd - 1;
 return r;
}
*/

////////////////////////////////////////////////////////////////////////////////////////////////////////

//PARA EL CASO DE LAS RAICES MULTIPLES:

//EJEMPLO RM1: funcion con raiz de multiplicidad 2.
//f(x) = (x – 3)  (x – 1)   (x – 1)
//f(x) = x^3 – 5x^2 + 7x - 3
//Entradas a probar para Raiz: Xo =  0.3 , X1 =  0.7
//Entradas a probar para Raiz: Xo =  1.5 , X1 =  1.1
/*
double eval_funcion(double v)
{
 double r=0.0 , a1 = 0.0, a2 = 0.0, a3 = 0.0;
 
 a1 = pow(v,3);
 a2 = 5*pow(v,2);
 a3 = 7*v;
 r = a1 - a2 + a3 - 3;
 return r;
}
*/

//EJEMPLO RM2: funcion con raiz de multiplicidad 3.
//f(x) = (x – 3) (x – 1) (x – 1) (x – 1)
//f(x) = x^4 - 6x^3 + 12x^2 - 10x + 3
//Entradas a probar para Raiz: Xo =  0.4 , X1 =  0.7
//Entradas a probar para Raiz: Xo =  1.6 , X1 =  1.3
/*
double eval_funcion(double v)
{
 double r=0.0 , a1 = 0.0, a2 = 0.0, a3 = 0.0, a4 = 0.0;
 
 a1 = pow(v,4);
 a2 = 6*pow(v,3);
 a3 = 12*pow(v,2);
 a4 = 10*v;
 r = a1 - a2 + a3 - a4 + 3;
 return r;
}
*/

//EJEMPLO RM3: funcion con raiz de multiplicidad 2.
//f(x) = (x^2 – 2) (x^2 – 2)
//f(x) = x^4 - 4x^2 + 4
//Entradas a probar para Raiz POSITIVA: Xo =  1.8 , X1 =  1.6
//Entradas a probar para Raiz POSITIVA: Xo =  1.0 , X1 =  1.3
/*
double eval_funcion(double v)
{
 double r=0.0 , a1 = 0.0, a2 = 0.0;
 a1 = pow(v,4);
 a2 = 4*v*v;
 r = a1 - a2 + 4;
 return r;
}
*/