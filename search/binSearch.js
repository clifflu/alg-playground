
module.exports = (find, lst) => {
  let left = 0
  let right = lst.length - 1

  while (right >= left) {
    let mid = Math.floor((left + right) / 2)
    if (lst[mid] === find) {
      return mid
    }

    if (lst[mid] > find) {
      right = mid - 1
    } else {
      left = mid + 1
    }
  }

  return -1
}
