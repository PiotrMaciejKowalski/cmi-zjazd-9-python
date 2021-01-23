#include <iostream>

using namespace std;

/*
Stos liter

W tym zadaniu należy napisać funkcję, która będzie odwracała kolejność znaków podanej argumentem tablicy znakowej i zapisywała wynik z powrotem we wspomnianej tablicy. W celu odwrócenia kolejności znaków, funkcja powinna wykorzystywać stos przechowujący wartości znakowe. Należy zademonstrować w programie głównym prawidłowość działania stworzonej funkcji dla kilku różnych przykładów tablic znakowych.
*/

// będziemy posługiwać się wskaźnikami StackOfLetters*
// wartość NULL będzie oznaczała pusty stos / brak elementu / koniec stosu

struct StackOfLetters {
  char letter;
  StackOfLetters *prev;
};


void pushToSOL(StackOfLetters *&sol, char letter) {
  StackOfLetters *newElement = new StackOfLetters;
  newElement->letter = letter;
  //(*newElement).letter = letter;
  newElement->prev = sol;
  sol = newElement;
}

// ważne! po utworzeniu stosu trzeba usunąć wszystkie elementy za pomocą
// wielokrotnego popFromSOL, w innym przypakdu nastąpi wyciek pamięci
// (gdyż po wszystkich new nie zostaną wykonane odpowiadające im delete)
char popFromSOL(StackOfLetters *&sol) {
  if(sol == NULL) {
    return '\0';
  } else {
    char top = sol->letter;
    StackOfLetters *oldTop = sol;
    sol = sol->prev;
    delete oldTop;
    return top;
  }
}


void task_81(char *data) {
  StackOfLetters *sol = NULL;
  
  for(char *ptr = data; *ptr != '\0'; ptr++) {
    pushToSOL(sol, *ptr);
  }
  
  for(char *ptr = data; sol != NULL; ptr++) {
    *ptr = popFromSOL(sol);
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
