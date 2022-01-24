class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

// a queue operates on the principal of "First In, First Out" like waiting in line for something
class SLQueue{
    constructor() {
        this.head = null
        this.tail = null
    }

    // add a node with the given value to the queue
    enqueue(value) {
        // your code here
        // create a new node with the value set to the passed in number
        var newNode = new Node(value);
        
        if (!this.head){
            this.head = newNode;
            this.tail = newNode;
            return this;
        }

        this.tail.next = newNode;
        this.tail = this.tail.next;
        return this;
    }

    // remove and return the front value from the queue
    dequeue() {
        // your code here
        if(!this.head) {
            
        } 
    }

    //return true/false based on whether you find the given value in a queue
    contains(value) {
        // your code here
        if(!this.head) { //this.head === null
            console.log("There's nothing in this list, so it cannot contain anything!")
            return false
        }
        // start runner at the beginning of the list
        var runner = this.head;
        while(runner != null) {
            // check if the input value is equal to the runner's value
            if(runner.value ==  value) {
                // if it is, return true
                console.log(`Found it! ${runner.value}`);
                return true
            }
            runner = runner.next;
        }
        // if we made it through out entire list and never hit true, we didn't find it!
        return false
    }

    displayQueue(){
        // your code here
        var runner = this.head;

        var str = "this.head = ";
        // run through entire list and print each value
        while(runner.next != null) {
            // print the value
            str += `${runner.value} --> `;
            // iterate your runner
            runner = runner.next;
        }
        str += `this.tail = ${runner.value} --> null`;
        console.log(str);
    }

    // return the value of the front node without removing from list
    front() {
        // your code here
        if(!this.head) {
            return null;
        } else {
            return this.head.value;
        }
    }

    // return whether or not a list is empty
    isEmpty() {
        // your code here
        if(!this.head){
            console.log("This is empty");
            return true;
        }
        else {
            console.log("This has values");
            return false;
        }
    }

}


var q = new SLQueue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
q.enqueue(5);
q.enqueue(6);
q.displayQueue();
console.log(q.contains(7));
console.log(q.isEmpty());
console.log(q);