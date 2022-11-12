var romanToInt = function(s) {
    const map = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };
    res = 0;

    for (let i=0; i < s.length; i++) {
        if (i+1 < s.length && map[s[i]] < map[s[i+1]]) {
            res -= map[s[i]];
        } else {
            res += map[s[i]];
        } 
    }
    return res;
};

output1 = romanToInt("LVIII");
output2 = romanToInt("MCMXCIV");
console.log(output1, output2);