#include <bits/stdc++.h>
using namespace std;

char getRandomChar(default_random_engine& engine) {
    std::uniform_int_distribution<int> distribution(0, 51); // 0-51 for a-zA-Z
    int randomIndex = distribution(engine);
    char randomCharacter;
    if (randomIndex < 26) {
        randomCharacter = 'a' + randomIndex;
    } else {
        randomCharacter = 'A' + (randomIndex - 26);
    }
    
    return randomCharacter;
}

int main() {
  std::random_device rd;
  std::default_random_engine engine(rd());

  int n = 1;
  string inp;

  cout << "Let's play a game: Echo the character I give you!" << endl;
  cout << "Any mistake will end the game." << endl;
  cout << "Get to 1000 to win!" << endl;

  while (n < 1000) {
    char c = getRandomChar(engine);
    cout << "No. " << n << " - " << c << ": "; cin >> inp;
    if (inp[0] == c) n++;
    else break;
  }

  if (n > 1000) cout << "ACSI{str1ngs_c4n_s0lv3_th1s}" << endl;

  return 0;
}
