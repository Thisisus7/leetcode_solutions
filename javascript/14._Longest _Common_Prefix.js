var longestCommonPrefix = function(strs) {
    res = '';
    for (let i=0; i<strs[0].length; i++) {
        for (s of strs) {
            if (i === s.length || strs[0][i] != s[i])  {
                return res;
            }
        }
        res += strs[0][i];
    }
    return res;
};

output1 = longestCommonPrefix(["flower","flow","flight"]);
output2 = longestCommonPrefix(["dog","racecar","car"]);
console.log(output1, output2);