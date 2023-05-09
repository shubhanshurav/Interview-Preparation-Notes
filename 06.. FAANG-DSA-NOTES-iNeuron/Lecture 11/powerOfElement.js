function ways(n) {
    if (n === 0)
        return 0;
    else if (n === 1)
        return 1;
    else if (n === 2)
        return 2;
    else {
        // recursion 
        return ways(n - 1) + ways(n - 2)
    }

}

let n = 4;
let res = ways(n);
console.log(`no of ways is: ${res}`)
