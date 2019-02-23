const N = 1000

/* Intro to iterators in JavaScript */
// Notice the * after the keyword function

function* range(start=0, end=Infinity, step=1) {
  let iteratorCount = 0;
  for (let i = start; i < end; i += step) {
    iteratorCount++;
    yield i;
  }
  return iteratorCount;
}

function main () {
  let result = 0;
  for (let i = 0; i < N; i += 1) {
    if (i % 3 === 0 || i % 5 === 0) {
      result += i;
    }
  }
  return result;
}

console.log(main())
