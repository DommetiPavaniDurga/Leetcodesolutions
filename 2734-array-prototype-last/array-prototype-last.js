/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    return this.length? this[this.length-1]:-1;
};
const arr1=[1,2,3];
console.log(arr1.last());
const arr2=[]
console.log(arr2.last());

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */