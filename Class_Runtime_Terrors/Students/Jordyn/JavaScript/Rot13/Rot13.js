let current_index = 0
let lower_case = 'abcdefghijklmnopqrstuvwxyz'
let upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let digits = '1234567890'
let punctuation = '!@#$%^&*()~`-_=+{}[]|:";/\'\\,.<>?'

function main(){
    let words = prompt('Please type something you would like encrypted: ')
    let key = parseInt(prompt('Please select an offset key number for encryption: '))
    let new_line = ''
    if (key >= 0){
        for (x in words){
            let char = words[x]
            if (char === ' '){
                new_line += ' '
            } else if (lower_case.includes(char)){
                current_index = get_index(char, lower_case)
                new_line += rotate_positive(current_index, key, lower_case)
            } else if (upper_case.includes(char)){
                current_index = get_index(char, upper_case)
                new_line += rotate_positive(current_index, key, upper_case)
            } else if (digits.includes(char)){
                new_line += char
            } else if (punctuation.includes(char)){
                new_line += char
            }
        }
    } else if (key <= -1){
        for (x in words){
            let char = words[x]
            if (char === ' '){
                new_line += ' '
            } else if (lower_case.includes(char)){
                current_index = get_index(char, lower_case)
                new_line += rotate_negative(current_index, key, lower_case)
            } else if (upper_case.includes(char)){
                current_index = get_index(char, upper_case)
                new_line += rotate_negative(current_index, key, upper_case)
            } else if (digits.includes(char)){
                new_line += char
            } else if (punctuation.includes(char)){
                new_line += char
            }
        }
    }
    console.log(`Your encrypted password is: ${new_line}`)
}

function rotate_positive(p_index, p_key, p_list){
    let p_lenList = p_list.length - 1
    let p_repeat = 0
    let p_x = parseInt(p_index)
    while (p_repeat < p_key){
        p_x += 1
        if (p_x > p_lenList){
            p_x = 0
        }
        p_repeat += 1
    }
    return p_list[p_x]
}

function rotate_negative(n_index, n_key, n_list){
    let n_lenList = n_list.length - 1
    let n_repeat = 0
    let n_x = parseInt(n_index)
    while (n_repeat < Math.abs(n_key)){
        n_x += 1
        if (n_x > n_lenList){
            n_x = 0
        }
        n_repeat += 1
    }
    return n_list[n_x]
}

function get_index(char, list){
    for (index in list){
        if (list[index] == char){
            return index
        }
    }
}

main()