if(rot<0){
    let m = secret[i]
    let n = newList.indexOf(m)
    secretList += encodeAlpha[n]
    // console.log(typeof encodeAlpha[n]+' :1')
}


else{
            
    for(i=rotate;i<encodeAlpha.length;i++){
        newList += encodeAlpha[i];
    }
    for(i=0;i<rotate;i++){
        newList += encodeAlpha[i];
    }

    for(secretList=[],i=0;i<secret.length;i++){
        let j = secret[i]
        let k = encodeAlpha.indexOf(j.toLowerCase())
        if(newList[k] === undefined){
            // console.log(typeof element+' :2')
            continue
        }
        else if(newList[k] !== undefined){
            secretList += newList[k]
            // console.log(typeof element+' :3')
        }
        // secretList[i] = newList[k]
        
    } 
}