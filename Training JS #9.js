function padIt(str, n) {
    //coding here
    let i = 0;
    let word = '';
    while (i <= n) {
        if (i == Math.ceil(n / 2)) {
            word += str;
        } else {
            word += '*';
        }
        i++;
    }
    console.log(word);
}

padIt("a", 1);
padIt("a", 2);
padIt("a", 3);
padIt("a", 4);
padIt("a", 5);