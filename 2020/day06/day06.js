fs = require('fs');
const lines = fs.readFileSync('2020/day6/input.txt', 'utf-8').split('\n').filter(x=>x);

function part1() {
    var total = 0
    var letras = []
    for (n in lines) {
        if (lines[n] == '\r') {
            total += letras.length
            letras = []
        }
        else {
            for (l in lines[n]) {
                if (lines[n][l] == '\r') {
                    continue
                }
                if (letras.includes(lines[n][l])==false) {
                    letras.push(lines[n][l])
                }
            }
        }
    }
    return total
}

function part2() {
    var total = 0
    var letras = []
    var primeiro = true
    for (n in lines) {
        if (lines[n] == '\r') {
            total += letras.length
            primeiro = true
            letras = []
        }
        else {
            var compara = []
            for (l in lines[n]) {
                if (lines[n][l] == '\r') {
                    if (primeiro == false) {
                        var continua = true
                        while (continua == true) {
                            find: {
                                for (c in letras) {
                                    if (compara.includes(letras[c])==false) {
                                        letras.splice(c,1)
                                        break find
                                    }
                                }
                                continua = false
                            }
                        }
                    }
                    primeiro = false
                    continue
                }
                if (primeiro && letras.includes(lines[n][l])==false) {
                    letras.push(lines[n][l])
                }
                else if (compara.includes(lines[n][l])==false) {
                    compara.push(lines[n][l])
                }
            }
        }
    }
    return total
}
console.log(part1())
console.log(part2())