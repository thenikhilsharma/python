#include <bits/stdc++.h>
using namespace std;

long long A[200002];
long long B[200002];
long long B1=0;
long long B2=0;
void function1(long long x,long long y){
    A[B1]=x;
    B1++;
    A[B1]=y;
    B1++;
}
void function2(long long x,long long y){
    B[B2]=x;
    B2++;
    B[B2]=y;
    B2++;
}
//END OF STATEMENT
int main()
{
    long long t;
    cin >> t;
    while(t--){
        B1=0;
        B2=0;
        
        long long cnt1 = 0;
        long long cnt2 = 0;
        
        long long n;
        cin >> n;
        long long a[n];
        long long A[n];
        
        long long Y1=0,Y=2;
        long long y1=0,y=0;
        
        long long odd_check =0;
        for(long long i=0; i<n ;i++){
            cin>>a[i];
            A[i]=a[i];
        }
//END OF STATEMENT        
if(a[0]%2==0)
{
    if(a[1]%2==0){
         
         for(long long i=2;i<n;i++){
             if(a[i]%2==1){
                 Y1=a[i];
                 y1=i;
                 odd_check = 1;
                 
                 a[1] = a[1]^Y1;
                 cnt1++;
                 function1(1,y1);
                 break;
             }
         }
         
    }//END OF STATEMENT
    else{
        Y1=a[1];
        y1=1;
        odd_check = 1;
    }
      Y=a[1];
      y=1;
      for(long long i =2;i<n;i++){
          if(a[i]%2==1){
              a[i]=a[i]^Y;
              cnt1++;
              function1(i,y);
          }
          i++;
          if(i<n){
              if(a[i]%2==0){
                  a[i]=a[i]^Y;
              cnt1++;
              function1(i,y);
              }
          }
      }//END OF STATEMENT
      A[0]=A[0]^Y1;
      cnt2++;
      function2(0,y1);
      
      Y=A[0];
      y=0;
      
      for(long long i=1;i<n;i++){
          if(A[i]%2==1){
              A[i]=A[i]^Y;
              cnt2++;
              function2(i,y);
          }
          i++;
          if(i<n){
              if(A[i]%2==0){
                  A[i]=A[i]^Y;
                  cnt2++;
                  function2(i,y);
              }
          }
      }
//END OF STATEMENT    
    
}
else{
    odd_check = 1;
    Y=A[0];
    y=0;
    for(long long i=1;i<n;i++){
        if(a[i]%2==1){
            a[i]=a[i]^Y;
            cnt1++;
            function1(i,y);
        }
        i++;
        if(a[i]%2==0 && i<n){
            a[i]=a[i]^Y;
            cnt1++;
            function1(i,y);
        }
    }
    
    Y = A[0];
    y=0;
    
    for(long long i=1;i<n;i++){
        if(A[i]%2==0){
            A[i]=A[i]^Y;
            cnt2++;
            function2(i,y);
        }
        i++;
        if(A[i]%2==1 && i<n){
            A[i]=A[i]^Y;
            cnt2++;
            function2(i,y);
        }
    }
    A[0]=A[0]^A[1];
    cnt2++;
    function2(0,1);
//END OF STATEMENT    
}
 if(odd_check==0){
     cout<<"-1\n";
 }
 else if(cnt1>cnt2){
     long long j;
     cout<<cnt2<<"\n";
     for(long long i=0;i<cnt2;i++){
         j=i*2;
         cout<<B[j]+1<<" "<<B[j+1]+1<<"\n";
     }
 }
 else{
     int j;
     cout<<cnt1<<"\n";
     for(long long i=0;i<cnt1;i++){
         j=i*2;
         cout<<A[j]+1<<" "<<A[j+1]+1<<"\n";
     }
 }
//END OF STATEMENT
}  
      return 0;  
    }