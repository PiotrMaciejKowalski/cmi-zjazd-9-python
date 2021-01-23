#include <iostream>
#include <algorithm>

using namespace std;


struct PartOfTree {
  int count; // liczba bombek
  int diameters[10]; // średnice bombek
  int sum; // suma średnic
};


void initPoT(PartOfTree &pot) {
  pot.count = 0;
  pot.sum = 0;
}


void pushToPoT(PartOfTree &pot, int diam) {
  //cerr << "Adding " << diam << " to " << &pot << "... (" << pot.count+1 << ")\n";
  pot.diameters[pot.count] = diam;
  pot.count++;
  pot.sum += diam;
}


int main() {
  PartOfTree top, mid, bot; // góra, środek, dół
  initPoT(top);
  initPoT(mid);
  initPoT(bot);
  
  for(int i = 0; i < 30; i++) {
    int diam;
    cin >> diam;
    
    if(diam < 5 and top.count < 10) {
      pushToPoT(top, diam);
    } else if(diam >= 5 and diam < 8 and mid.count < 10) {
      pushToPoT(mid, diam);
    } else if(diam >= 8 and bot.count < 10) {
      pushToPoT(bot, diam);
    } else {
      PartOfTree *a = &top, *b = &mid, *c = &bot;
      
      if(a->count > b->count) swap(a, b);
      if(b->count > c->count) swap(b, c);
      if(a->count > b->count) swap(a, b);
      
      if(a->count == b->count and b->sum < a->sum) {
        swap(a, b);
      }
      
      pushToPoT(*a, diam);
    }
  }
  
  for(int i = 0; i < 10; i++) {
    cout << mid.diameters[i] << ' ';
  }
  cout << '\n';
  
  return 0;
}
