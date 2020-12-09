function rot(userpassword, rotnumber)
    {
        let = userpassword = Array.from(userpassword);
        let answerlist = [];
        rotnumber = rotnumber;
        for(let i = 0; i < (userpassword.length); i++)
            {
                let newasc = userpassword[i];
                newasc = newasc.charCodeAt(0);
            if ((newasc >= 97 && newasc <=122) || (newasc >= 65 && newasc <=90))
                {
                    if (rotnumber >= 0)
                        {
                            if ((newasc >= 97 && newasc <=122))
                                {
                                    let check = newasc + rotnumber; 
                                    if ((newasc + rotnumber) >= 123 )
                                        {
                                            newasc = newasc - rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);
                                        }
                                    else
                                        {
                                            newasc = newasc + rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);
                                        }

                                }
                            else
                                {
                                    if ((newasc + rotnumber) >= 91)
                                        {
                                            newasc = newasc - rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);                                            
                                        }
                                    else
                                        {
                                            newasc = newasc + rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);    
                                        }
                                }
                        }   
                    else
                        {
                            if (newasc >= 97 && newasc <=122)
                                {
                                    if ((newasc + rotnumber) <= 96 )
                                        {
                                            newasc = newasc - rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar); 
                                        }
                                    else
                                        {
                                            newasc = newasc + rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);  
                                        }
                                }    
                            else
                                {
                                    if ((newasc + rotnumber) <= 64)
                                        {
                                            newasc = newasc - rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);
                                        }       
                                    else
                                        {
                                            newasc = newasc + rotnumber;
                                            rotchar = String.fromCharCode(newasc);
                                            answerlist.push(rotchar);
                                        }
                        
                                }    
                        }    
                        
                }
            else
                {
                    rotchar = String.fromCharCode(newasc);
                    answerlist.push(rotchar);
                }
            }
            return answerlist
    }
   

const readline = require('readline-sync');

let userpassword = readline.question('Input your password to be cipher? ');
let userrot = parseInt(readline.question('What is your ROT '));

let output = (rot(userpassword, userrot));

console.log(output.join(""));