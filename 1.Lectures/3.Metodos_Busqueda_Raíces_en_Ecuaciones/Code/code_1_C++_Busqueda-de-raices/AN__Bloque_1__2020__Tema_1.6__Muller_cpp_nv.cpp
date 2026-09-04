#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

void lecturas(double* , double* , double* , int*);
void muller(double , double , double , int);
double eval_funcion(double);
/****************************************************************************/

int main()
{
 double vx0 , vx1 , vx2;
 int vn ;
 lecturas(&vx0 , &vx1 , &vx2 , &vn);
 muller(vx0 , vx1 , vx2 , vn);

 return 0;
}
/****************************************************************************/

void lecturas(double *X0 , double *X1, double *X2, int *N)
{
 cout<<" - M U L L E R - "<<endl;
 cout<<"Digite el valor X0 : "; cin>>*X0;
 cout<<"Digite el valor X1 : "; cin>>*X1;
 cout<<"Digite el valor X2 : "; cin>>*X2;
 cout<<"Digite el numero de iteraciones : "; cin>>*N;

 while(*N<=2)
 {
  cout<<"La cantidad de iteraciones debe ser positiva (>2) "<<endl;
  cout<<"Digite el numero de iteraciones : "; cin>>*N;
 }
}
/****************************************************************************/
void muller(double X0, double X1, double X2, int N)
{
 double TOL=0.0000001, efX0 , efX1 , efX2;
 double h1 , h2 , d1 , d2 , a , D , E , h , p;
 double b , Z , srD , k1, k2 , xh, Er;
 int i;
 cout.precision(10);

//evaluacion INICIAL de la expresion particular
 efX0 = eval_funcion(X0);   efX1 = eval_funcion(X1);   efX2 = eval_funcion(X2);

//El "paso 1"
 h1 = X1 - X0; h2 = X2 - X1;
 d1 = (efX1 - efX0)/h1; d2 = (efX2 - efX1)/h2;
 a = (d2 - d1)/(h2 + h1);
 i = 2;

 cout<<"\n"<<"n"<<"\t"<<"Raiz"<<"\t\t\t\t"<<"f(raiz)"<<"\t\t\t"<<"COTA DE ERROR";

 while(i <= N) //El "paso 2"
 {
  //El "paso 3"
  b = d2 + (h2*a);
  Z = 4*efX2*a;   srD = (b*b)-Z;   D = sqrt(srD);

  k1 = b-D; if(k1<0) k1=k1*(-1);
  k2 = b+D; if(k2<0) k2=k2*(-1);

  //El "paso 4"
  if(k1<k2){ E = b+D;}
  else { E = b-D;}

  //El "paso 5"
  h = (-2*efX2)/E;  p = X2 + h;

  //El "paso 6"
  Er = (p - X2)/p;  if(Er<0){Er=Er*(-1);}
  
  //Para mostrar resultados iteracion a iteracion
  //cout<<"\n"<<i<<"\t"<<X2<<"\t"<<efX2<<"\t\t\t"<<Er;

  //presentacion de resultados iteracion a iteracion 
  cout<<"\n"<<i<<"\t";
  std::cout.setf( std::ios::fixed, std:: ios::floatfield );
  std::cout << X2<<"\t";
  std::cout.unsetf( std::ios::floatfield );
  std::cout.precision(10);
  std::cout<<"\t\t"; std::cout << efX2;
  std::cout<<"\t\t"; std::cout << Er;

  if (Er<TOL) { cout<<"\nprocedimiento completado satisfactoriamente\n"; system("pause"); exit(1);    }

  //El "paso 7" preparar para la siguiente iteracion
  X0 = X1; X1 = X2; X2 = p;
  h1 = X1 - X0; h2 = X2 - X1;

  //evaluacion de la expresion particular
  efX0 = eval_funcion(X0);  efX1 = eval_funcion(X1);   efX2 = eval_funcion(X2);

  d1 = (efX1 - efX0)/h1; d2 = (efX2 - efX1)/h2;
  a = (d2 - d1)/(h2 + h1);
  i = i + 1;
 }

 //El "paso 8"
 if((i>N)&&(xh>TOL)) {cout<<"\nEl metodo fracaso despues de "<<N<<" iteraciones";}
 cout<<"\n"; system("pause");
}
/****************************************************************************/

//PRIMERA
//{xo = 0.3 , x1 = 0.7 , x2 = 3.2}
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
//Raiz: {xo =-0.4 , x1 = 0.8 , x2 = 2}
/*
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) + (4*v*v) - 10;
 return r;
}
*/


//TERCERA
//Raiz1: {xo =-0.1 , x1 = -0.3 , x2 = -0.8}
//Raiz2: {xo =   2 , x1 =  0.5 , x2 =  1.5}
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
//Raiz: {xo = 0.2 , x1 = 1.6 , x2 = 1}
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
//Entradas a probar para Raiz 1: {xo = -0.2 , x1 = -0.5 , x2 = -0.7}
//Entradas a probar para Raiz 2: {xo = -0.3 , x1 =  0   , x2 =  0.4}
//Entradas a probar para Raiz 3: {xo =  1.4 , x1 =  1.8 , x2 =  2.1}
/*
double eval_funcion(double v)
{
 double r=0.0;
 r = (v*v*v) - (2*v*v) - v + 1;
 return r;
}
*/

//CASO ESPECIAL
//Raiz 1: {xo = 0.5 , x1 = 1.15 , x2 = 0.9}
//Raiz 2: {xo =-0.5 , x1 = 1.15 , x2 = 0.9}
/*
double eval_funcion(double v)
{
 double r=0.0 ,
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
//Entradas a probar para Raiz: {xo = 0.1 , x1 = 0.3 , x2 = 0.95}
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
//Entradas a probar para Raiz: {xo = 0.3 , x1 = 0.5 , x2 = 0.8}
//Entradas a probar para Raiz: {xo = 1.9 , x1 = 1.7 , x2 = 1.1}
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
//Entradas a probar para Raiz POSITIVA: {xo =  0.4 , x1 =  1.9 , x2 =  1.4}
//Entradas a probar para Raiz NEGATIVA: {xo = -0.4 , x1 = -1.9 , x2 = -1.4}
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


//EJEMPLO RM4
//Raiz 1 (-4): {xo = -3   , x1 = -3.4 , x2 = -4.2 }  
//Raiz 2 (-1): {xo =  1.1 , x1 = -2.1 , x2 = -1.4 }  RM2
//Raiz 3 ( 2): {xo =  3.6 , x1 =  3.1 , x2 =  2.3 }  RM3
/*
double eval_funcion(double v)
{
 double r=0.0 , a1 = 0.0, a2 = 0.0, a3= 0.0, a4=0.0, a5=0.0;
 a1 = pow(v,6);
 a2 = 15*pow(v,4);
 a3 = 14*pow(v,3);
 a4 = 36*pow(v,2);
 a5 = 24*v;
 r = a1 - a2 + a3 + a4 - a5 - 32;
 return r;
}
*/


//EJEMPLO RM5
//Funcion con raiz de multiplicidad 3.
//f(x) = x^4 - 6x^3 + 12x^2 - 10x + 3
//Para raiz x = 1  {xo = 0.1 , x1 = 0.4 , x2 = 0.9 } RM3
//Para raiz x = 3  {xo = 3.5 , x1 = 3.2 , x2 = 2.8 }
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
