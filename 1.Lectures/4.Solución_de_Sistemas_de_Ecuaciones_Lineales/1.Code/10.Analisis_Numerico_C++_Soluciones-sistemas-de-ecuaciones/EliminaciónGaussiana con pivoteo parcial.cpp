/*
   Analisis Númerico 1
   Autor: María Adriana Ochoa Verduzco
   Programa: Programa que resuelve un sistema de ecuaciones nxn con el metodo de 
   eliminación gaussiana con pivoteo parcial;
   19/10/2014
*/

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <math.h>


using namespace std;

void LeerArchivo(const char *, float A[]);
void EliminacionGPP(int n, int col, float A[]);
void Imprimir(int n,int col,float A[]);
float *Sustitucion(int n, int col, float A[]);
float Mayor(float a, float b);
void Encabezado();

 

int main()
{
    int n;		
    string str;

    Encabezado();
    
    do{
        cout<<"Ingrsa n [1-10]: ";
        cin>>n;
        if(n<1 || n>10) cout<<"Error el rango de n es [1-10]\n";
    }while(n<1 || n>10);
    cout<<"\nIngrese el nombre del archivo de la matriz aumentada "<<n<<"x"<<n<<" ('ejemplo.txt'):\n";
    cin>>str;
      
    float* A = new float[n*(n+1)]; //Se guarda la matriz aumentada
    float* X = new float[n];   //Se guarda X1,X2,X3,...,Xn
    int col=n+1;
    
    const char *archivo = str.c_str(); //Transformamos el string en const char * 
    
   	LeerArchivo(archivo, A);    
    cout<<"La matriz capturada es:\n";
    Imprimir(n,n+1,A);
     
    EliminacionGPP(n,col,A);
    cout<<"\nAplicando eliminacion gaussiana con pivoteo:\n";
    Imprimir(n,n+1,A);
    
    X=Sustitucion(n,col,A); 
    
    
    cout<<"Los resultados de la matriz son:\n"; 
     for(int i=0;i<n;i++){
         cout<<"X"<<i+1<<": "<<X[i]<<endl;
     }
    cout<<endl;
     
    delete[] A;
    delete[] X;
    system("pause");
    return(0);
}
//------------------------------------------------------------------------------
/*
    Función encargada de leer el archivo y pasar el numero a un arreglo dinamico
    ENTRADA: El nombre del archivo, el arreglo donde se guardará la matriz
    SALIDA: ----
*/
void LeerArchivo(const char * archivo, float A[])
{    
     FILE *arm=fopen(archivo,"r+"); //abrir archivo;

     int cont=0;
     float numero;  
     
     if (arm==NULL){ //Verificamos la lectura correcta del archivo
        cout<<"Error al leer el archivo...\n";
        system("pause");
        exit(0);
	}else{    
        while (feof(arm)==0){
            fscanf(arm, "%f", &numero);
	    	A[cont]=numero;   
            cont++;
	    }
        fclose(arm); //cerrar archivo    
    }
}
//------------------------------------------------------------------------------
/*
    Función Encargada de hacer el proceso de eliminación Gaussiana
    ENTRADA: Número de renglones n, Número de columnas, Arreglo de la matriz 
    SALIDA: ------
*/
void EliminacionGPP(int n, int col, float A[])
{
     float m=0.0f;
     int j;
     float* B = new float[col];for(int t=0;t<col;t++) B[t]=0;
     //Aqui verificamos si hacemos el primer pivoteo.
     for(int k=1;k<n;k++){
         if (A[col*k]==Mayor(A[0],A[col*k])){
            for(int i=0;i<col;i++){
                 j=(col*k)+i;
                 B[i]=A[i];
                 A[i]=A[j];
                 A[j]=B[i]; 
             }    
         }
     }
     
     int l,o;
     
     for(int i=0;i<n;i++){//Verificamos si en hay '0' en la diagonal y si es asi
            if(A[(i*col)+i]==0){ //hacemos pivoteo
                for(int l=0;l<col;l++){
                    o=(i*col)+l;
                    B[l]=A[o];
                    A[o]=A[o+col];
                    A[o+col]=B[l];
                }    
                       
            }   
            for(int j=i+1;j<n;j++){
                m = A[(j*col)+i]/A[(i*col)+i];            
                for(int k=i;k<col;++k) 
                    A[(j*col)+k]=A[(j*col)+k]-m*(A[(i*col)+k]);    
            }
                      
        }       
        
        if(A[((n*col)-2)]==0){
            cout<<"No existe solucion unica...\n\n";
            system("pause");
            exit(0); 
        }
}

//------------------------------------------------------------------------------
/*
    Función encargada de hacer la llamada sustitución hacia atras
    ENTRADA: numero de renglones n, numero de columnas y la matriz
    SALIDA: puntero del arreglo que contiene los resultados X1,X2,X3,...,Xn
*/
float *Sustitucion(int n, int col, float A[])
{
     float* X = new float[n]; //Aqui se guarda X1, X2,..., Xn
     float *p;
     float suma=0;
    //sustitucion hacia atras
     X[n-1]=A[(n*col)-1]/A[(n*col)-2];
     for(int i=(n-2);i>=0;i--){
         for(int j=i+1;j<n;j++)
             suma+=(A[(i*col)+j]*X[j]);                
         
         X[i]=(A[(i*col)+n]-suma)/A[(i*col)+i]; 
         suma=0;    
     }

     return X;
     delete[] X;
}
//------------------------------------------------------------------------------
/*
    Función que imprimé la matriz de cualquier dimensión
    ENTRADA: numero de renglones, número de columnas y la matriz
    SALIDA: ----
*/
void Imprimir(int r,int col, float A[])
{
   int j,i;
   cout<<char(218);
   
   for(int h=0; h<col; h++)    cout<<"           ";
   cout<<char(191)<<endl;  
           
   for(i=0; i<r; i++){
        cout<<char(179);
        for(j=0; j<col; j++)
            printf("%10.6f ",A[(i*col)+j]);
            
        cout<<char(179)<<endl; 
   } 
       
   cout<<char(192);
   for(int h=0; h<col; h++)    cout<<"           ";
   cout<<char(217)<<endl;  
}
//------------------------------------------------------------------------------
/*
    Función que compara 2 numeros y devuelve el mayor
    ENTRADA: 2 numeros a comparar.
    SALIDA: El mayor de ambos numeros.
*/
float Mayor(float a, float b)
{
    float aa=fabs(a), ab=fabs(b), m=a;
    if(aa<ab) m=b;
    return m;
}   
//------------------------------------------------------------------------------
/*
    Función que imprime el encabezado del programa
    ENTRADA: -----
    SALIDA: -----
*/
void Encabezado()
{
     for(int i=0; i<80; i++) cout<<char(205); 
     cout<<"\t\tPrograma que resuelve un sistema de ecuaciones nxn\n\t   con el metodo de eliminacion gaussiana con pivoteo parcial\n";   
     for(int i=0; i<80; i++) cout<<char(205); 
}


