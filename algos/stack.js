class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

// a stack operates on the principal of "First In, Last Out" like a pringles can
class SLStack{
    constructor() {
        this.top = null  // this.head equivalent
    }

    // add a given value to your stack
    push(value){
        // if(!this.value){
        //     console.log("this stack is empty")
        //     this.top = value
        //     this.next = null
        // } else {
        //     this.top.next = this.top
        //     this.top.value = value
        // }
        // create a new node with the value set to the passed in number
        var newNode = new Node(value);
        // take newNode's .next pointer and point it into the list

        if(this.top == null) {
            this.top = newNode;    
        } else {
            // change .head pointer to point at our newNode
            newNode.next = this.top;
            this.top = newNode;
            return this;
        }
    }
    
    // remove and return the top value
    pop(){
        if(!this.top){
            console.log("this stack is empty")
            return this;
        }
        console.log(this.top)
        var temp = this.top;
        this.top.pop;
        this.next = this.top;
        return temp;
    }

    // return (don't remove) the top value of a stack
    returnTop() {
        if(!this.top){
            console.log("this stack is empty")
            return false
        }
        return this.top
    }

    // return the number of stacked values
    stackSize(){
        var runner = this.top;

        var counter = 0;
        // run through entire list and count each value
        while(runner.next != null) {
            // print the value
            counter += 1;
            // iterate your runner
            runner = runner.next;
        }
        console.log(counter)
        return counter;
    }

    printStack() {
        var runner = this.top;

        var str = "this stack contains = ";
        // run through entire list and print each value
        while(runner.next != null) {
            // print the value
            str += `${runner.value} --> `;
            // iterate your runner
            runner = runner.next;
        }
        console.log(str);
    }
}

var sls = new SLStack()
sls.push(3)
sls.push(18)
sls.push(12)
sls.push(78)
sls.push(56)
console.log(sls.pop())
console.log(sls.returnTop())
sls.printStack()
sls.stackSize()