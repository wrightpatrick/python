// There are 3 edits that can be done on a string: add a acharacter, remove a character, or replace a character. 
// Given 2 strings, write a function that checks if they are one edit or fewer away from eachother (see samples below)

function oneAway(str1, str2) {
    var end = 0;
    var runner1 = 0;
    var runner2 = 0;
    while (runner1 < str1.length || runner2 < str2.length) {
        if (str1[runner1] == str2[runner2]) {
            runner1++;
            runner2++;
        } else if (str1[runner1] == str2[runner2 + 1]) {
            runner1++;
            runner2++;
        } else {
            runner1++;
            runner2++;
            end++;
        }
    }
    runner1 = str1.length - 1;
    runner2 = str2.length - 1;
    while (runner1 >= 0 || runner2 >= 0) {
        if (str1[runner1] == str2[runner2]) {
            runner1--;
            runner2--;
        } else if (str1[runner1 - 1] == str2[runner2]) {
            runner1--;
            runner2--;
        } else {
            runner1--;
            runner2--;
            end++;
        }
    } if (end > 2) {
        return false;
    } return true;
}



console.log(oneAway("hello", "eello")) // true
console.log(oneAway("hello", "eelloo")) // false 
console.log(oneAway("ello", "hello")) // true
console.log(oneAway("helllo", "hello")) // true
console.log(oneAway("hello", "helo")) // true
console.log(oneAway("hello", "hell")) // true
console.log(oneAway("hjllo", "helo")) // false


// ==========================================
// Vampires and the sleeping man
// ==========================================

// Consider a village with vampires and a sleeping man (who never wakes up, no matter what).
// A vampire can eat the sleeping man, but after eating him, the vampire falls asleep.
// Similarly, any vampire can eat any other sleeping vampire, and this process repeats.
// Assume that the vampires are very smart and would ALWAYS choose to stay alive than to eat the man and risk their lives.
// Initially, there are 65 vampires and 1 sleeping man. What would happen in the village?