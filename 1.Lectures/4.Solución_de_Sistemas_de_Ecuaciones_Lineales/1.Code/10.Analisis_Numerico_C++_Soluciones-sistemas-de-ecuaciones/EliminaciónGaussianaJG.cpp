/*
   Analisis Númerico 1
   Autor: José Juan Gurrola Cota
   Programa: Programa que resuelve un sistema de ecuaciones nxn con el metodo de Gauss-Seidel
   12/10/2014
*/

#include <iostream>
#include <cstdlib>
#include <stdio.h>


using namespace std;

void LeerArchivo(const char *, float A[]);
void EliminacionG(int n, int col, float A[]);
void Imprimir(int n,int col,float A[]);
float *Sustitucion(int n, int col, float A[]);
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
    EliminacionG(n,col,A);
    cout<<"\nAplicando eliminacion gaussiana:\n";
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
void EliminacionG(int n, int col, float A[])
{
     float m=0.0f;
     
     for(int i=0;i<n;i++){//Proceso de eliminación
            if(A[(i*col)+i]==0){
                cout<<"No existe solucion unica...\n\n";
                system("pause");
                exit(0); 
            }

            for(int j=i+1;j<n;j++){
                m = A[(j*col)+i]/A[(i*col)+i];            
                for(int k=i;k<col;++k) 
                    A[(j*col)+k]=A[(j*col)+k]-m*(A[(i*col)+k]);    
            }          
        }       
        
        if(A[n*(n+1)-1]==0){
            cout<<"No existe solucion unica...\n\n";
            system("pause");
            exit(0); 
        }
}

//------------------------------------------------------------------------------
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
void Encabezado()
{
     for(int i=0; i<80; i++) cout<<char(205); 
     cout<<"\t\tPrograma que resuelve un sistema de ecuaciones nxn\n\t\t\tcon el metodo de eliminacion gaussiana\n";   
     for(int i=0; i<80; i++) cout<<char(205); 
}


