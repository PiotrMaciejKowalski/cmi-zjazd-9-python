#include <iostream>
#include <stack> // http://www.cplusplus.com/reference/stack/stack/

using namespace std;

/*
Stos liter

W tym zadaniu należy napisać funkcję, która będzie odwracała kolejność znaków podanej argumentem tablicy znakowej i zapisywała wynik z powrotem we wspomnianej tablicy. W celu odwrócenia kolejności znaków, funkcja powinna wykorzystywać stos przechowujący wartości znakowe. Należy zademonstrować w programie głównym prawidłowość działania stworzonej funkcji dla kilku różnych przykładów tablic znakowych.
*/


void task_81(char *data) {
  stack<char> sol; // StackOfLetters *sol = NULL;
  
  for(char *ptr = data; *ptr != '\0'; ptr++) {
    sol.push(*ptr); // pushToSOL(sol, *ptr);
  }
  
  for(char *ptr = data; not sol.empty(); ptr++) {
    //*ptr = popFromSOL(sol);
    *ptr = sol.top();
    sol.pop();
  }
}


int main() {
  char data[4096];
  
  cin >> data;
  cout << "data = \"" << data << "\"\n";
  task_81(data);
  cout << "data = \"" << data << "\"\n";
  
  return 0;
}
