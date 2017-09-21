const assert = require('assert')
const bs = require('../binSearch')

describe('binSearch', () => {
  it('1-pool', () => {
    let p = [0]
    assert(0 === bs(0, p))
    assert(-1 === bs(-1, p))
    assert(-1 === bs(0.5, p))
  })

  it('2-pool', () => {
    let p = [0, 1]
    assert(0 === bs(0, p))
    assert(1 === bs(1, p))
    assert(-1 === bs(-1, p))
    assert(-1 === bs(0.5, p))
    assert(-1 === bs(4, p))
  })

  it('3-pool', () => {
    let p = [0, 1, 2]
    assert(0 === bs(0, p))
    assert(1 === bs(1, p))
    assert(2 === bs(2, p))
    assert(-1 === bs(-1, p))
    assert(-1 === bs(0.5, p))
    assert(-1 === bs(1.3, p))
    assert(-1 === bs(4, p))
  })
})
