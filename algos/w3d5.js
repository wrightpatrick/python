// Given a dollar amount with change (an integer w/decimal) convert to change. Make sure to count the largest denomination first!

// Example: 3.21 --> 12 quarters, 2 dimes, 1 penny



const coins = [.25, .10, .01];

function convertToCoinChange(dollars) {
    var quarter = (dollars / 4) /coins[0];
    var dimes = (dollars / 10) / coins[1];
    
}



const coins = {
    "silver dollar": 1,
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}

function convertToCoinChange(ammount, coins){
    ammount += 0.009;
    var output = "";

    Object.keys(coins).forEach(key => {
        if (ammount >= coins[key]){
            var coinCount = Math.floor(ammount / coins[key]);
            ammount -= coinCount * coins[key];
            output += coinCount + " " + key + "(s), ";
        }
    });

    output = output.slice(0, output.length - 2);
    return output;
}