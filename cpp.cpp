#include <iostream>
using namespace std;
 
int main () {
   int a = 10;

   while( a < 20 ) {
      cout << "value of a: " << a << endl;
      a++;
      if (a == 18){
          cout << "program exited";
          return 0;
      }
   }
 
   return 0;
}