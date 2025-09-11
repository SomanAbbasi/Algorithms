
#include<iostream>

using namespace std;
int main()
{
    int arr[5]={1,2,5,4,3};
    int n=5;

    for (int i = 1; i < n; i++)
    {
        int key=arr[i];
        int j=i-1;
        while (j>=0 && key<arr[j])
        {
            arr[j+1]=arr[j];
            j-=1;
        }

        arr[j+1]=key;
        
        
        

    }
    
    cout<<"Insertion Sort "<<endl;
    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    
}