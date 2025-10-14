#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

void lecturas(double* , int*);
void newton(double , int);
double eval_funcion(double);
double eval_derfuncion(double);
/****************************************************************************/

int main()
{
 double vpo;
 int vn = 0 ;
 lecturas(&vpo , &vn);
 newton(vpo , vn);
 
 return 0;
}
/*****************************************************************************/

void lecturas(double *po , int *N)
{
 cout<<" - N E W T O N - "<<endl;
 cout<<"Digite la aproximacion inicial : "; cin>>*po;
 cout<<"Digite el numero de iteraciones : "; cin>>*N;

 while(*N<=2)
 {
  cout<<"La cantidad de iteraciones debe ser positiva (>2) "<<endl;
  cout<<"Digite el numero de iteraciones : "; cin>>*N;
 }
}
/****************************************************************************/

void newton(double po, int N)
{
 double TOL=0.0000001 , ef=0.0 , edf=0.0, Er=0.0 , p=0.0 , c=0.0 , efp=0.0;
 int i = 1 ; //el "paso 1"
 cout<<"\n"<<"\t -- p -- "<<"\t\t -- f(p) -- "<<"\t\t-- Er -- ";

 //el "paso 2"
 while(i <= N)
 {
  ef = eval_funcion(po);
  edf = eval_derfuncion(po);
  c = ef / edf ; //   f(po) / f'(po)
  p = po - c;    //el "paso 3"
  efp = eval_funcion(p);
  Er = (p - po)/p;    if(Er<0) Er=Er*(-1); //esto es para ayudar al paso 4


  //presentacion de resultados iteracion a iteracion 
  cout<<"\n"<<i<<"\t";
  std::cout.setf( std::ios::fixed, std:: ios::floatfield );
  std::cout << p;
  std::cout.unsetf( std::ios::floatfield );
  std::cout.precision(10);
  std::cout<<"\t\t"; std::cout << efp;
  std::cout<<"\t\t"; std::cout << Er;

  //el "paso 4"
  if(Er<TOL) {cout<<"\n\nProcedimiento completado satisfactoriamente\n"; system("pause"); exit(1);}

  //el "paso 5"
  i = i + 1;

  //el "paso 6"  redefinicion de po
  po = p;
 }

 //el "paso 7"
 if((i>N)||(Er>TOL)) {cout<<"\nEl metodo fracaso despues de "<<N<<" iteraciones";}
 cout<<"\n"; system("pause");
}
/****************************************************************************/

//PRIMERA
//Entrada a probar para Raiz: po =  0.5
//Entrada a probar para Raiz: po = 30 (¿Sirve?)
/*
double eval_funcion(double v)
{
 double r=0.0, ex=0.0 , emx=0.0 , lnx=0.0;
 ex = pow(2.718281828,v); emx=1/ex;
 lnx = log(v);
 r = emx - lnx;
 return r;
}

double eval_derfuncion(double z)
{
 double r=0.0, ex=0.0 , emx=0.0, memx=0.0;
 ex = pow(2.718281828,z); emx=1/ex; memx=(-1)*emx;
 r = memx - (1/z);
 return r;
}
*/

//SEGUNDA
//Entrada a probar para Raiz: po =   1
//Entrada a probar para Raiz: po =   0   (¿Sirve?)
//Entrada a probar para Raiz: po =  -2.5 (¿Sirve?)
/*
double eval_funcion(double v)
{
 double r=0.0 , a1 = 0.0, a2 = 0.0;
 a1 = v*v*v;
 a2 = 4*v*v;
 r = a1 + a2 - 10;
 return r;
}

double eval_derfuncion(double z)
{
 double s=0.0, a1 = 0.0, a2 = 0.0;
 a1 = 3*z*z;
 a2 = 8*z;
 s = a1 + a2;
 return s;
}
*/

//TERCERA
//Entrada a probar para Raiz1: po = -1
//Entrada a probar para Raiz2: po =  1
//Entrada a probar para Raiz:  po =  0.35 (¿Sirve?)
/*
double eval_funcion(double v)
{
 double r=0.0 , ee =0.0, emx = 0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 r = emx + (v*v) - 2;
 return r;
}

double eval_derfuncion(double z)
{
 double r=0.0, ex=0.0 , emx=0.0, memx=0.0;
 ex = pow(2.718281828,z); emx=1/ex; memx=(-1)*emx;
 r = memx + (2*z);
 return r;
}
*/

//CUARTA
//Entrada a probar para Raiz menor positiva: po =  1.5
//Entrada a probar para Raiz menor positiva: po =  1.88 (¿Sirve?)
/*
double eval_funcion(double v)
{
 double r=0.0 , ee =0.0, emx = 0.0;
 ee = pow(2.718281828,v); emx = 1/ee;
 r = (2*emx) - sin(v);
 return r;
}

double eval_derfuncion(double z)
{
 double r=0.0, ex=0.0 , emx=0.0, memx=0.0;
 ex = pow(2.718281828,z); emx=1/ex; memx=(-1)*emx;
 r = 2*memx - cos(z);
 return r;
}
*/


//QUINTA
//Entrada a probar para Raiz 1: po = -0.5
//Entrada a probar para Raiz 2: po =  0
//Entrada a probar para Raiz 3: po =  2
//Entrada a probar para Raiz:   po = -0.215 (¿Sirve?)
//Entrada a probar para Raiz:   po =  1.55  (¿Sirve?)
/*
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) - (2*v*v) - v + 1;
 return r;
}

double eval_derfuncion(double z)
{
 double s=0.0, a1 = 0.0, a2 = 0.0;
 a1 = 3*z*z;
 a2 = 4*z;
 s = a1 - a2 - 1;
 return s;
}
*/

//CASO ESPECIAL
//Entrada a probar para Raiz 1: po =  0.9
//Entrada a probar para Raiz 2: po = -0.9
//Entrada a probar para Raiz:   po =  0.2 (¿Sirve?)
/*
double eval_funcion(double v)
{
 double r=0.0, xd;
 xd = pow(v,10);
 r = xd - 1;
 return r;
}

double eval_derfuncion(double z)
{
 double r=0.0, xd;
 xd = pow(z,9);
 r = 10 * xd;
 return r;
}
*/

////////////////////////////////////////////////////////////////////////////////////////////////////////

//PARA EL CASO DE LAS RAICES MULTIPLES:

//EJEMPLO RM1: funcion con raiz de multiplicidad 2.
//f(x) = (x – 3)  (x – 1)   (x – 1)
//f(x) = x^3 – 5x^2 + 7x - 3
//Entrada a probar para Raiz: po =  0.5
//Entrada a probar para Raiz: po =  1.5
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

double eval_derfuncion(double z)
{
 double r=0.0, a1 = 0.0, a2 = 0.0;
 a1 = 3*pow(z,2);
 a2 = 10*z;
 r = a1 - a2 + 7;
 return r;
}
*/

//EJEMPLO RM2: funcion con raiz de multiplicidad 3.
//f(x) = (x – 3) (x – 1) (x – 1) (x – 1)
//f(x) = x^4 - 6x^3 + 12x^2 - 10x + 3
//Entrada a probar para Raiz: po =  0.5
//Entrada a probar para Raiz: po =  1.5
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

double eval_derfuncion(double z)
{
 double r=0.0, a1 = 0.0, a2 = 0.0, a3 = 0.0;
 a1 = 4*pow(z,3);
 a2 = 18*pow(z,2);
 a3 = 24*z;
 r = a1 - a2 + a3 - 10;
 return r;
}
*/

//EJEMPLO RM3: funcion con raiz de multiplicidad 2.
//f(x) = (x^2 – 2) (x^2 – 2)
//f(x) = x^4 - 4x^2 + 4
//Entrada a probar para Raiz POSITIVA: po =  1.6
//Entrada a probar para Raiz POSITIVA: po =  1.2

//Entrada a probar para Raiz: po =  0 (¿Sirve?)

/*
double eval_funcion(double v)
{
 double r=0.0 , a1 = 0.0, a2 = 0.0;
 a1 = pow(v,4);
 a2 = 4*v*v;
 r = a1 - a2 + 4;
 return r;
}

double eval_derfuncion(double z)
{
 double r=0.0, a1 = 0.0, a2 = 0.0;
 a1 = 4*z*z*z;
 a2 = 8*z;
 r = a1 - a2;
 return r;
}
*/
