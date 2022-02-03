// Given a list of itineraries, find the proper path of the trip. 
// A list of itineraries will be an array of arrays, where the inner array will always be length two. 
// For example, here is an example list of itineraries: [ ['LAX', 'SFO'], ['ICN', 'LAX'], ['SJC', 'ICN'] ].

// The first element in each inner array is the "from" airport, and the latter is the "to" airport. 
// So, ['LAX', 'SFO'] means "from LAX to SFO." Running with this example, given this list of itineraries,
// your code should then print out 'SJC -> ICN -> LAX -> SFO', or you can just comma-separate 
// those airports if you don't like the arrows. Whatever method you choose, 
// you should produce the proper route of the trip. It's guaranteed that the itineraries 
// have exactly one start airport, and exactly one end airport, and that there aren't any loops. 
// Basically, the itinerary will form a single linked list.

// return a single string of the mapped itineraries

function mappingItineraries(arr) {

	//loop through list, tag index 0 as start and index 1 as end
	var starts = [];
	var ends = [];
	var middle = [];
	for (i = 0; i < arr.length; i++) {
		starts.push(arr[i][0]);
		ends.push(arr[i][1]);
	}
	console.log(starts);
	console.log(ends);

	for (i = 0; i < arr.length; i++) {
		for (j = 0; j < 2; j++) {
			for (k = 0; k < starts.length; k++) {
				if (starts[k] === arr[i][j]) {
					middle.push(arr[i][j])
				}
				else {
					var end = arr[i][j];
				}
				if (ends[k] === arr[i][j]) {
					middle.push(arr[i][j])
				}
				else {
					var start = arr[i][j];
				}
			}
		}
	}

}



console.log(mappingItineraries([['ICN', 'LAX'], ['LAX', 'SFO'], ['SJC', 'ICN'], ['NYU', 'SJC'], ['AMS', 'NYU']]));
// AMS -> NYU -> SJC -> ICN -> LAX -> SFO


// ############################################################################################


// There are 3 edits that can be done on a string: add a acharacter, remove a character, or replace a character. 
// Given 2 strings, write a function that checks if they are one edit or fewer away from eachother (see samples below)
function oneAway(str1, str2) {
	// your code here
}

// console.log(oneAway("hello", "eello")) // true
// console.log(oneAway("hello", "eelloo")) // false 
// console.log(oneAway("ello", "hello")) // true
// console.log(oneAway("helllo", "hello")) // true
// console.log(oneAway("hello", "helo")) // true
// console.log(oneAway("hello", "hell")) // true
// console.log(oneAway("hjllo", "helo")) // false