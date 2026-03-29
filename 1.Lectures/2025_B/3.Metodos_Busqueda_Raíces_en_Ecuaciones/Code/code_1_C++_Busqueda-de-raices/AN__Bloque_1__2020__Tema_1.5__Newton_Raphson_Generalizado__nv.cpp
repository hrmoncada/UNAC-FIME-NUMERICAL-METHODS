#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

void lecturas(double* , int*);
void newton_generalizado(double , int);
double eval_funcion(double);
double eval_derfuncion(double);
double eval_segderfuncion(double);
/*******************************************************************************/

int main()
{
 double vpo;
 int vn;
 lecturas(&vpo , &vn);
 newton_generalizado(vpo , vn);

 return 0;
}
/*****************************************************************************/

void lecturas(double *po , int *N)
{
 cout<<" - N E W T O N   G E N E R A L I Z A D O - "<<endl;
 cout<<"Digite la aproximacion inicial : "; cin>>*po;
 cout<<"Digite el numero de iteraciones : "; cin>>*N;

 while(*N<=2)
 {
  cout<<"La cantidad de iteraciones debe ser positiva (>2) "<<endl;
  cout<<"Digite el numero de iteraciones : "; cin>>*N;
 }
}
/*******************************************************************************/
void newton_generalizado(double po, int N)
{
 double TOL=0.0000001 , ef=0.0 , edf=0.0, Er=0.0 , p=0.0 , c=0.0 , efp=0.0;
 double esdf = 0.0, t1=0.0 , t2=0.0 , t3=0.0 , t4=0.0;
 int i = 1 ; //el "paso 1"
 cout.precision(10);
 cout<<"\n"<<"\t -- p -- "<<"\t\t -- f(p) -- "<<"\t\t-- Er -- ";

 //el "paso 2"
 while(i <= N)
 {
  ef = eval_funcion(po);
  edf = eval_derfuncion(po);
  esdf = eval_segderfuncion(po);

  t1 = ef * edf ;  //  f(po) * f'(po)
  t2 = ef * esdf ; //  f(po) * f''(po)
  t3 = edf * edf;  //  [f'(po)]^2
  t4 = t3 - t2 ;   //  [f'(po)]^2  -  [f(po) * f''(po)]
  c  = t1 / t4 ;   //  [f(po) * f'(po)] / [f'(po)]^2  -  [f(po) * f''(po)]
  p = po - c;      //el "paso 3"

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

////////////////////////////////////////////////////////////////////////////////////////////////////////

//PARA EL CASO DE LAS RAICES MULTIPLES:

//EJEMPLO RM1: funcion con raiz de multiplicidad 2.
//f(x) = (x – 3)  (x – 1)   (x – 1)
//f(x) = x^3 – 5x^2 + 7x - 3
//Entrada a probar para Raiz: po =  0.5
//Entrada a probar para Raiz: po =  1.5

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

double eval_segderfuncion(double y)
{
 double r=0.0, a1 = 0.0;
 
 a1 = 6*y;
 r = a1 - 10;
 return r;
}


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

double eval_segderfuncion(double y)
{
 double r=0.0, a1 = 0.0, a2 = 0.0;
 a1 = 12*pow(y,2);
 a2 = 36*y;
 r = a1 - a2 + 24;
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

double eval_segderfuncion(double y)
{
 double r=0.0, a1 = 0.0;
 a1 = 12*y*y;
 r = a1 - 8;
 return r;
}
*/