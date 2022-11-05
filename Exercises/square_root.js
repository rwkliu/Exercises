function square_root(x){
    let i = 0;
    let sqr_root = 0;

    while(sqr_root <= x) {
        i++;
        sqr_root = i * i;
    }
    return i - 1;
}

let x = 1000000000000000000000;
console.log(square_root(x));