fs = require('fs');
let lines = fs.readFileSync('2020/day8/input.txt', 'utf-8').split('\r').filter(x=>x);
let len_lines = 0;
for (i in lines) {
    lines[i] = lines[i].replace('\n','');
    len_lines+=1;
}

function part1() {
    let pos = 0;
    let acc = 0;
    let vistos = [];
    while (vistos.includes(pos) == false) {
        [com, num] = lines[pos].split(' ');
        vistos.push(pos);
        if (com=='nop') {
            pos += 1;
        }
        else if (com=='acc') {
            acc += parseInt(num);
            pos += 1;
        }
        else if (com=='jmp') {
            pos += parseInt(num);
        }
        if (pos == len_lines) {
            return [acc, acc]
        }
    }
    return acc
}
//console.log(part1());


function part2() {
    for (i in lines) {
        [com, num] = lines[i].split(' ');
        if (com == 'nop') {
            lines[i] = 'jmp ' + num;
        }
        else if (com == 'jmp') {
            lines[i] = 'nop ' + num;
        }
        else continue
        let res = part1();
        if (res.length == 2) {
            return res[0]
        }

        [com, num] = lines[i].split(' ');
        if (com == 'nop') {
            lines[i] = 'jmp ' + num;
        }
        else if (com == 'jmp') {
            lines[i] = 'nop ' + num;
        }
    }
}

console.log(part2());