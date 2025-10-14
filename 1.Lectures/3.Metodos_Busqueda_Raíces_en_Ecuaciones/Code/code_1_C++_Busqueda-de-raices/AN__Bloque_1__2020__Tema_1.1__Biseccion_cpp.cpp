#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

void lecturas(double* , double*, int*);
void biseccion(double , double, int);
double eval_funcion(double);
/****************************************************************************/
int main()
{
   double va, vb;
   int vn;
   lecturas(&va , &vb , &vn);
   biseccion(va , vb, vn);
   
   return 0;
}
/******************************************************************************/
void lecturas(double *a , double *b, int *N)
{
   cout<<" - B I S E C C I O N - "<<endl;
   cout<<"Digite el extremo inferior (a) : "; cin>>*a;
   cout<<"Digite el extremo superior (b) : "; cin>>*b;
   cout<<"Digite el numero de iteraciones : "; cin>>*N;
   
   while(*a>=*b)
   {
      cout<<"El extremo inferior (a) debe ser MENOR que el extremo (b) "<<endl;
      cout<<"Digite el extremo inferior (a) : "; cin>>*a;
      cout<<"Digite el extremo superior (b) : "; cin>>*b;
   }
   
   while(*N<=2)
   {
      cout<<"La cantidad de iteraciones debe ser positiva (>2) "<<endl;
      cout<<"Digite el numero de iteraciones : "; cin>>*N;
   }
}
/****************************************************************************/
void biseccion(double a , double b, int N)
{
   double TOL=0.0000001;
   int i = 1;
   double aux1=0.0;
   double  efa=0.0, efp = 0.0, er=0.0, Xanterior, Xnueva;
   cout.precision(10);
  
   //El Paso 1 fue inicializar i en 1.
   cout<<"\n"<<"n"<<"\t"<<"Raiz"<<"\t\t\t"<<"f(Raiz)"<<"\t\t\t"<<"Er";
   
   //Paso 2: calculo del primer punto medio y evaluacion
   Xanterior = (a + b)/2;
   efa = eval_funcion(a);
   efp = eval_funcion(Xanterior);
   aux1 = efa * efp;
   if(aux1>0){a = Xanterior;}  else {b = Xanterior;}
   
   //Paso 3:
   while(i <= N)
   {
      //Paso 4: Calculo y evaluacion de nueva raiz y calculo del error relativo
      Xnueva = (a + b)/2;    efp = eval_funcion(Xnueva);
      er = (Xnueva - Xanterior)/Xnueva;  if(er<0){er=er*(-1);}
      
      //Paso 5: Mostrar raiz aproximada si ha terminado
      if((efp==0)||(er<TOL))
      {
         cout<<"\n"<<i+1<<"\t";
         std::cout.setf( std::ios::fixed, std:: ios::floatfield );
         std::cout << Xnueva;
         std::cout.unsetf( std::ios::floatfield );
         std::cout.precision(10);
         std::cout<<"\t\t"; std::cout << efp;
         std::cout<<"\t\t"; std::cout << er;
         cout<<"\n"; system("pause"); exit(1);
      }
      
      //Paso 6: actualizar contador de iteraciones
      i = i + 1;
      
      //Adicional: Para mostrar resultados iteracion a iteracion
      //cuando aun debe seguir iterando
      cout<<"\n"<<i<<"\t";
      std::cout.setf( std::ios::fixed, std:: ios::floatfield );
      std::cout << Xnueva;
      std::cout.unsetf( std::ios::floatfield );
      std::cout.precision(10);
      std::cout<<"\t\t"; std::cout << efp;
      std::cout<<"\t\t"; std::cout << er;
      
      
      //Paso 7:  re-definicion del intervalo y actualizacion de raiz
      efa = eval_funcion(a);
      aux1 = efa*efp;   //f(a)*f(Xnueva)
      if(aux1>0){a = Xnueva; }   else {b = Xnueva;}
      Xanterior = Xnueva; //Actualizacion de raiz
   }
   
   //el "paso 8"
   if((i>N)&&(er>TOL)) {cout<<"\nEl metodo ha fracasado despues de "<<N<<" iteraciones";}
   
   cout<<"\n";  system("pause");
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
//Entradas a probar para Raiz: a = 1 , b = 2
double eval_funcion(double x)
{
   double r=0.0;
   r = (x*x*x) + (4*x*x) - 10;
   return r;
}
*/


//TERCERA
/*
//Entradas a probar para Raiz 1: a = -1 , b = -0.5
//Entradas a probar para Raiz 2: a =  1 , b =  1.5
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
//Entradas a probar para Raiz 1: a = -1   , b = -0.5
//Entradas a probar para Raiz 2: a =  0.5 , b =  1
//Entradas a probar para Raiz 3: a =  2   , b =  2.5
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
