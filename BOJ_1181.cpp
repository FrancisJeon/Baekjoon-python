// 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
//     길이가 짧은 것부터
//     길이가 같으면 사전 순으로

// 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.
// 출력

// 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

#include <iostream>
#include <algorithm>
using namespace std;

string a[20000];
int n;

bool compare(string a, string b) {
    // higher priority to shorter one
        if (a.length() < b.length()) {
            return  1;
        }
        else if (a.length() > b.length()) {
            return 0;
        } 
        // string compare '<' top-down
        else {
            return a < b;
        }
    }

int main() {
    cin >> n;
    for (int i = 0 ; i < n; i++) {
        cin >> a[i] ;
    }

    sort(a, a+n, compare);
    
    for (int i = 0; i < n; i++) {
        if(i>0 && a[i] == a[i-1]) {
            continue;
        } else {
            cout << a[i] << endl;
        }
    }
}