async function promiseAll(functions) {
  return new Promise((resolve, reject) => {
    let results = new Array(functions.length);
    let completed = 0;

    functions.forEach((fn, index) => {
      fn()
        .then(value => {
          results[index] = value;
          completed++;
          if (completed === functions.length) {
            resolve(results);
          }
        })
        .catch(err => reject(err));
    });
  });
}

// Example usage:
const promise = promiseAll([
  () => new Promise(res => setTimeout(() => res(42), 100)),
  () => new Promise(res => setTimeout(() => res(7), 200))
]);

promise.then(console.log).catch(console.error);
// Output: [42, 7] after 200ms
