#include<iostream>

using namespace std;
int main()
{
    int n,size=10;
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        cout<<"Enter an Integer: ";
        cin>>n;
        arr[i]=n;
    }
    int min_el,temp_swap;
    int i=0,index;

    while (i<size)
    {
        min_el=arr[i];
        index=i;
        for (int j = i+1; j < size; j++)
        {
            if (arr[j]<min_el)
            {
                min_el=arr[j];
                index=j;
            }    
        }
    /*Swapping*/
    temp_swap=arr[i];
    arr[i]=min_el;
    arr[index]=temp_swap;  
    i+=1;
    }
/*Sorted Array is By Selection Sort*/
cout<<"Sorted Array is: {";
for (int i = 0; i <size; i++)
{
    cout<<arr[i];
    if (i!=size-1)
    {
        cout<<",";
    }
}
cout<<"}";
   

}