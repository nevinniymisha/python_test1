#include <stdio.h>

int main() {
    
    unsigned arr[] = {1,2,3,4,5,67,83,93,108};
    int len_arr = sizeof(arr)/ sizeof(int);
    int o;
    int n =scanf("%d",&o);
    for(int i = 0;i  < len_arr;i++){
        if (arr[i] == o){
            printf("%d",(i + 1));
            break;
        }
        
    }
    

    return 0;
}