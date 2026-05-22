/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let result=[]
    for(let el of arr){
        if(Array.isArray(el)&&n>0){
            result.push(...flat(el,n-1));

        }else{
            result.push(el);

        }
    }
    return result;
};