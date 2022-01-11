// Create a function that, given an input string, returns a boolean true/false whether parentheses in that string are valid.

// Example 1:"y(3(p)p(3)r)s" --> true
// Example 2: "n(0(p)3" --> false
// Example 3: "n)0(t(o)k" --> false

// hint: consider using an array or object to solve

// check entire string, return true/false
// every single opening parens has a closing
// never hit an closing parens before a opening parens
// ONLY care about the parens in the string

function parensValid (str) {
    // your code here
    //make an array 
    var tempArr = [];

    for (i = 0; i < tempArr.length; i++) {
        if (str[i] === "(" || str[i] === "[" || str[i] === "{") {
            tempArr.push(str[i]);
        }
        else if (str[i] === ")" || str[i] === "]" || str[i] === "}" && tempArr[tempArr.length-1] == "(") {
            tempArr.pop();
        }
        else if (str[i] === ")" || str[i] === "]" || str[i] === "}") {
            return false;
        }
    }

if (tempArr.length > 0) {
        return false;
} else {
    return true;
}
}
console.log(parensValid("y(3(p)p(3)r)s")); // true
console.log(parensValid("n(0(p)3")); // false
console.log(parensValid("n)0(t(o)k")); // false
console.log(parensValid("((()))")); // true
console.log(parensValid("()()()()()()(")); // false

// Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid. 

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[a]}}(){bcd}{()}" --> true

// hint: consider using an array or object to solve

function bracesValid(str) {
    // your code here
}

console.log(bracesValid("({[({})]})")); // true 
console.log(bracesValid("d(i{a}l[t]o)n{e!")); // false
console.log(bracesValid("{{[a]}}(){bcd}{()}")); // true