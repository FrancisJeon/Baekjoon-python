#include <iostream>
using namespace std;

int main(){
    int num, inp;
    int count[10001] = {};
    cin >> num;
    for (int i = 0; i < num; i++) {
        scanf("%d", &inp);
        count[inp]++;
    }

    for (int i = 0; i<10001; i++) {
        while(count[i] != 0) {
            printf("%d\n", i);
            count[i]--;
        }
    }


    return 0;
}