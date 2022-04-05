#include<stdio.h>
#include<stdlib.h>
/*
Goal: Creating a file which contains points A =(0,5) B=(3,0) C=(1,0) D=(1,-5) and their points of reflections about y-axis.*/

// Function to write the points into a file.
void load(int data[],int d,FILE*fp){
    int i;
    for(i=0;i<d;i++){
        fprintf(fp,"%d ",data[i]); // writing the point vectors into a file using the fprintf function.
    }
    fprintf(fp,"\n");
    return;
}
// Function takes two vectors and their dimension as arguments and returns the dot product.
int dot(int vec1[],int vec2[],int d){
    int i;
    int dot_product=0;
    for(i=0;i<d;i++){
         dot_product+=vec1[i]*vec2[i];
    }
    return dot_product;
}
// norm_square function returns the square of the norm of a vectior of 'd' dimensions.(Here components of vector is represented as elements of an array) 
int norm_square(int vec[],int d){
    int i;
    int k=0;
    for(i=0;i<d;i++)k += vec[i]*vec[i];
    return k;
}
// Function used for finding the point of reflection about a plane ( nTx = c) and storing it in a file.   
void reflect(int point[],int normal[],int c,int d,FILE*fp){
    int i;
    int* ref = (int*)malloc(sizeof(int)*d);//DMA.
    for(i=0;i<d;i++){
          ref[i] = point[i] + 2*((c-dot(normal,point,2))/(norm_square(normal,d)))*normal[i];
    }
    load(ref,d,fp);
    free(ref); // heap memory is freed here.
   return;

}

int main(){
    FILE* fp = fopen("data.txt","w");// File is opened in writing mode.
    // Point vectors are represented as arrays.
    int A[] ={0,5};
    int B[] ={3,0};
    int C[] ={1,0}; 
    int D[] ={1,-5};

    int d = 2; // Dimensions of the vector.
    // For y axis (x=0) 
    int n[] = {1,0};
    int c =0;
    // Storing the orginal point vectors.
  load(A,2,fp);
  load(B,2,fp);
  load(C,2,fp);
  load(D,2,fp);
    // Storing the point vectors after the reflection.
   reflect(B,n,c,d,fp);
   reflect(C,n,c,d,fp);
   reflect(D,n,c,d,fp);
    
   fclose(fp); // File is closed.

return 0;
}
