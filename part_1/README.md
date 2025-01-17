# Output
The following code:

```js

const array = [12, 10, 22, 5, 25];

for(var i = 0; i < array.length; i++){

setTimeout(function(){

console.log("The element in position " + i + " is: " + array[i]);

}, 5000);

}

```


will output to the console:


```
The element in position 5 is: undefined
The element in position 5 is: undefined
The element in position 5 is: undefined
The element in position 5 is: undefined
The element in position 5 is: undefined
```

# Explanation:

setTimeout() sets an anonymuos function to print the i'th element 5 secs in the future (5 times). By that time, the value of i is 5, which points outside the array, and therefore prints 'undefined'.