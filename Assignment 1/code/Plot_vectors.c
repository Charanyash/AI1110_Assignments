#include<stdio.h>
#include<stdlib.h>
void load(int data[],int d,FILE*fp){
    int i;
    for(i=0;i<d;i++){
        fprintf(fp,"%d ",data[i]);
    }
    fprintf(fp,"\n");
    return;
}
int dot(int vec1[],int vec2[],int d){
    int i;
    int dot_product=0;
    for(i=0;i<d;i++){
         dot_product+=vec1[i]*vec2[i];
    }
    return dot_product;
}
int norm_square(int vec[],int d){
    int i;
    int k=0;
    for(i=0;i<d;i++)k += vec[i]*vec[i];
    return k;
}
void reflect(int point[],int normal[],int c,int d,FILE*fp){
    int i;
    int* ref = (int*)malloc(sizeof(int)*d);
    for(i=0;i<d;i++){
          ref[i] = point[i] + 2*((c-dot(normal,point,2))/(norm_square(normal,d)))*normal[i];
    }
    load(ref,d,fp);
    free(ref);
   return;

}

int main(){
    FILE* fp = fopen("text.txt","w");
    int A[] ={0,5};
    int B[] ={3,0};
    int C[] ={1,0}; 
    int D[] ={1,-5};
    int d = 2;
    int n[] = {1,0};
    int c =0;
  load(A,2,fp);
  load(B,2,fp);
  load(C,2,fp);
  load(D,2,fp);
   reflect(B,n,c,d,fp);
   reflect(C,n,c,d,fp);
   reflect(D,n,c,d,fp);
   fclose(fp);

return 0;
}