

function isOkPass(p){
    var anUpperCase = /[A-Z]/;
    var aLowerCase = /[a-z]/; 
    var aNumber = /[0-9]/;
    var aSpecial = /[!|@|#|$|%|^|&|*|(|)|-|_]/;
    var obj = {};
    obj.result = true;
    if(p.length < 8){
        obj.result=false;
        obj.error="Not long enough!"
        return obj;
    }
    var numUpper = 0;
    var numLower = 0;
    var numNums = 0;
    var numSpecials = 0;
    for(var i=0; i<p.length; i++){
        if(anUpperCase.test(p[i]))
            numUpper++;
        else if(aLowerCase.test(p[i]))
            numLower++;
        else if(aNumber.test(p[i]))
            numNums++;
        else if(aSpecial.test(p[i]))
            numSpecials++;
    }
    if(numUpper < 2 || numLower < 2 || numNums < 2 || numSpecials <2){
        return false
    }
    return true;
}


var password = "TTtt11##";
console.log(isOkPass(password))