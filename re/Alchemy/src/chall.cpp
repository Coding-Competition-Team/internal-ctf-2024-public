#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

std::unordered_map<std::string, int> periodicTable = {
        {"H", 1}, {"He", 2}, {"Li", 3}, {"Be", 4}, {"B", 5},
        {"C", 6}, {"N", 7}, {"O", 8}, {"F", 9}, {"Ne", 10},
        {"Na", 11}, {"Mg", 12}, {"Al", 13}, {"Si", 14}, {"P", 15},
        {"S", 16}, {"Cl", 17}, {"Ar", 18}, {"K", 19}, {"Ca", 20},
        {"Sc", 21}, {"Ti", 22}, {"V", 23}, {"Cr", 24}, {"Mn", 25},
        {"Fe", 26}, {"Co", 27}, {"Ni", 28}, {"Cu", 29}, {"Zn", 30},
        {"Ga", 31}, {"Ge", 32}, {"As", 33}, {"Se", 34}, {"Br", 35},
        {"Kr", 36}, {"Rb", 37}, {"Sr", 38}, {"Y", 39}, {"Zr", 40},
        {"Nb", 41}, {"Mo", 42}, {"Tc", 43}, {"Ru", 44}, {"Rh", 45},
        {"Pd", 46}, {"Ag", 47}, {"Cd", 48}, {"In", 49}, {"Sn", 50},
        {"Sb", 51}, {"Te", 52}, {"I", 53}, {"Xe", 54}, {"Cs", 55},
        {"Ba", 56}, {"La", 57}, {"Ce", 58}, {"Pr", 59}, {"Nd", 60},
        {"Pm", 61}, {"Sm", 62}, {"Eu", 63}, {"Gd", 64}, {"Tb", 65},
        {"Dy", 66}, {"Ho", 67}, {"Er", 68}, {"Tm", 69}, {"Yb", 70},
        {"Lu", 71}, {"Hf", 72}, {"Ta", 73}, {"W", 74}, {"Re", 75},
        {"Os", 76}, {"Ir", 77}, {"Pt", 78}, {"Au", 79}, {"Hg", 80},
        {"Tl", 81}, {"Pb", 82}, {"Bi", 83}, {"Po", 84}, {"At", 85},
        {"Rn", 86}, {"Fr", 87}, {"Ra", 88}, {"Ac", 89}, {"Th", 90},
        {"Pa", 91}, {"U", 92}, {"Np", 93}, {"Pu", 94}, {"Am", 95},
        {"Cm", 96}, {"Bk", 97}, {"Cf", 98}, {"Es", 99}, {"Fm", 100},
        {"Md", 101}, {"No", 102}, {"Lr", 103}, {"Rf", 104}, {"Db", 105},
        {"Sg", 106}, {"Bh", 107}, {"Hs", 108}, {"Mt", 109}, {"Ds", 110},
        {"Rg", 111}, {"Cn", 112}, {"Nh", 113}, {"Fl", 114}, {"Mc", 115},
        {"Lv", 116}, {"Ts", 117}, {"Og", 118}
    };


void start() {
  std::cout <<
    "H                                                  He\n"
    "Li Be                                B  C  N  O  F Ne\n"
    "Na Mg                               Al Si  P  S Cl Ar\n"
    "K  Ca Sc Ti  V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr\n"
    "Rb Sr  Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te  I Xe\n"
    "Cs Ba La Hf Ta  W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn\n"
    "Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og\n"
    "\n"
    "  * La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu\n"
    "  * Ac Th Pa  U Np Pu Am Cm Bk Cf Es Fm Md No Lr\n"
    "\n\n";

  return;
}


int one() {
  std::string a;
  
  std::cout << "a = 80\n";
  std::cout << "a: ";
  std::cin >> a;

  if(periodicTable[a] != 80) {
    return 0;
  }

  return 1;
}


int two() {
  std::string a, b;
  
  std::cout << "a**2 + b = 12608\n";
  std::cout << "a: ";
  std::cin >> a;
  std::cout << "b: ";
  std::cin >> b;

  if(periodicTable[a] * periodicTable[a] + periodicTable[b] != 12608) {
    return 0;
  }

  return 1;
}


void three() {
  std::string a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r;
  
  std::cout << 
  "d**2 + n**3 + r**2 + j = 18710510\n"
  "k + p = 172\n"
  "d + f = 122\n"
  "e = 54\n"
  "b + h**2 = 9525\n"
  "q**3 + p = 857430\n"
  "g = 57\n"
  "h + o + q = 300\n"
  "l + a = 141\n"
  "m + c + e**2 = 3074\n"
  "i = 55\n"
  "j**3 + e = 1295083\n"
  "r = 49\n"
  "n = 95\n"
  "e + q = 149\n"
  "m + q = 152\n"
  "k + a = 163\n"
  "o = 108\n"
  "b = 116\n"
  "i + h = 152\n"
  "m + k = 174\n";

  std::cout << "a: ";
  std::cin >> a;
  std::cout << "b: ";
  std::cin >> b;
  std::cout << "c: ";
  std::cin >> c;
  std::cout << "d: ";
  std::cin >> d;
  std::cout << "e: ";
  std::cin >> e;
  std::cout << "f: ";
  std::cin >> f;
  std::cout << "g: ";
  std::cin >> g;
  std::cout << "h: ";
  std::cin >> h;
  std::cout << "i: ";
  std::cin >> i;
  std::cout << "j: ";
  std::cin >> j;
  std::cout << "k: ";
  std::cin >> k;
  std::cout << "l: ";
  std::cin >> l;
  std::cout << "m: ";
  std::cin >> m;
  std::cout << "n: ";
  std::cin >> n;
  std::cout << "o: ";
  std::cin >> o;
  std::cout << "p: ";
  std::cin >> p;
  std::cout << "q: ";
  std::cin >> q;
  std::cout << "r: ";
  std::cin >> r;

  if(periodicTable[d] * periodicTable[d] + periodicTable[n] * periodicTable[n] * periodicTable[n] + periodicTable[r] * periodicTable[r] + periodicTable[j] != 864110) {
    return;
  }
  if(periodicTable[k] + periodicTable[p] != 172) {
    return;
  }
  if(periodicTable[d] + periodicTable[f] != 122) {
    return;
  }
  if(periodicTable[e] != 54) {
    return;
  }
  if(periodicTable[b] + periodicTable[h] * periodicTable[h] != 9525) {
    return;
  }
  if(periodicTable[q] * periodicTable[q] * periodicTable[q] + periodicTable[p] != 857430) {
    return;
  }
  if(periodicTable[g] != 57) {
    return;
  }
  if(periodicTable[h] + periodicTable[o] + periodicTable[q] != 300) {
    return;
  }
  if(periodicTable[l] + periodicTable[a] != 141) {
    return;
  }
  if(periodicTable[m] + periodicTable[c] + periodicTable[e] * periodicTable[e] != 3074) {
    return;
  }
  if(periodicTable[i] != 55) {
    return;
  }
  if(periodicTable[j] * periodicTable[j] * periodicTable[j] + periodicTable[e] != 1295083) {
    return;
  }
  if(periodicTable[r] != 49) {
    return;
  }
  if(periodicTable[n] != 95) {
    return;
  }
  if(periodicTable[e] + periodicTable[q] != 149) {
    return;
  }
  if(periodicTable[m] + periodicTable[q] != 152) {
    return;
  }
  if(periodicTable[k] + periodicTable[a] != 163) {
    return;
  }
  if(periodicTable[o] != 108) {
    return;
  }
  if(periodicTable[b] != 116) {
    return;
  }
  if(periodicTable[i] + periodicTable[h] != 152) {
    return;
  }
  if(periodicTable[m] + periodicTable[k] != 174) {
    return;
  }

  std::string flag = "ACSI{" + std::string(1, periodicTable[d]) + std::string(1, periodicTable[k]) + std::string(1, periodicTable[q]) + std::string(1, periodicTable[p]) + std::string(1, periodicTable[g]) + std::string(1, periodicTable[n]) + std::string(1, periodicTable[r]) + std::string(1, periodicTable[f]) + std::string(1, periodicTable[e]) + std::string(1, periodicTable[a]) + std::string(1, periodicTable[m]) + std::string(1, periodicTable[i]) + std::string(1, periodicTable[l]) + std::string(1, periodicTable[j]) + std::string(1, periodicTable[c]) + std::string(1, periodicTable[b]) + std::string(1, periodicTable[h]) + std::string(1, periodicTable[o]) + "}";
  std::cout << "Here is the secret element:" << flag;
}


int main() {
  start();
  
  if(one()) {
    if(two()) {
      three();
    }
  }
  
  return 0;
}