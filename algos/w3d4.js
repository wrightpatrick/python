function bookIndex(arr){
    var temp = [];
    for (var x = 0; x < arr.length; x++) {
        if (arr[x]+1 == arr[x+1]) {
            var y = arr[x];
            while (arr[x]+1 == arr[x+1]) {
                x++;
            }
        var z = arr[x];
        temp.push(y + "-" + z);
        } else {
            temp.push(arr[x]);
        }
    }
    return temp.toString()
}

console.log(bookIndex([1,3,4,5,7,8,10,12])) // "1, 3-5, 7-8, 10, 12"


function bookIndex(arr){
    var str = "";
    for (i = 0 ; i < arr.length ; i++){
        if (i != 0 && str[str.length - 1] != " "){
            str = str + " ";
        }
        if (arr[i + 1] == arr[i] + 1){
            var x = arr[i];
            //var j = i;
            while (arr[i + 1] == arr[i] + 1){
                i++;
            }
            var z = arr[i];
            str = str + x + "-" + z;
            //i = j;
        }
        else if (arr[i] != str[str.length - 2]){
            str = str + arr[i];
        }
    }
    return str;
}

console.log(bookIndex([1,3,4,5,7,8,10,12]));
console.log(bookIndex([1,2,3,4,6,8,9,10,11,12]));

// Write a function that given a sorted array of page positive numbers, return a string representing a book index. Combine consecutive pages to create ranges.

// Example: [1,3,4,5,7,8,10,12] --> "1, 3-5, 7-8, 10, 12"

function bookIndex(arr){
    var str = "";

    for (var i = 0 ; i < arr.length ; i++){
        if(i !== 0){
            str += ", ";
        }

        if (arr[i + 1] === arr[i] + 1){
            var start = arr[i];
            while (arr[i + 1] === arr[i]+1){
                i++;
            }
            var end = arr[i];
            str += start + "-" + end;
        }
        
        else {
            str += arr[i];
        }
    }
    return str;
}

console.log(bookIndex([1,3,4,5,7,8,10,12])) // "1, 3-5, 7-8, 10, 12"