#include <bits/stdc++.h>
using namespace std;

int n, s, temp;
long long int ans=0;
vector<int> t, tmin; //telescopes
int main() {
  std::ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> s;
  t.resize(n); tmin.resize(n);
  for(int i=0;i<n;i++) {
    cin >> t[i];
  }
  for(int i=n-1;i>=0;i--) {
    if(i<n-1) {
      tmin[i] = min(t[i], tmin[i+1]);
    }
    else {
      tmin[i] = t[i];
    }
  }

  while(s--) {
    cin >> temp;
    ans += tmin[temp];
  }
  cout << ans;
}