/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    let cnt =  0; 
    let i = s.length-1;

    while (s[i] == ' ') i--;
    while (i >= 0 && s[i] != ' ') {
        cnt ++;
        i--;
    }
    return cnt;
};

 var lengthOfLastWord2 = function(s) {
    let cnt = 0;
    for (let i = s.length-1; i >= 0; i--) {
        if (cnt != 0 && s[i] == " ") {
            return cnt;
        }
        if (s[i] != " ") {
            cnt ++;
        }
    }
    return cnt;
};

output1 = lengthOfLastWord("Hello World");
output2 = lengthOfLastWord("   fly me   to   the moon  ");
output3 = lengthOfLastWord("luffy is still joyboy");
console.log(output1, output2, output3);