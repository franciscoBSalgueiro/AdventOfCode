fs = require('fs');
let lines = fs.readFileSync('2020/day10/input.txt', 'utf-8').split('\n');

nums = [];

for (i in lines) {
  nums.push(Number(lines[i]))
}
nums.sort((a, b) => a - b)

function part1() {
  diffs = [0,0,1]
  for (i in nums) {
    if (i==0) {
      diffs[nums[0]-1] += 1
    }
    else {
      dif = nums[i] - nums[i-1];
      diffs[dif-1] += 1
    }
  }
  console.log(diffs[0]*diffs[2])
}

function part2() {
  paths = {}
  for (i in nums) {
    paths[nums[i]] = [];
    for (j=1; j<4; j++) {
      if (nums.includes(nums[i]+j)) {
        paths[nums[i]].push(nums[i]+j)
      }
    }
  }
  nums.reverse()
  for (i in nums) {
    dest = paths[nums[i]]
    if (dest.length==0) {
      paths[nums[i]] = 1
    }
    else {
      val = 0
      for (j in dest) {
        val += paths[dest[j]]
      }
      paths[nums[i]] = val;
    }
  }
  console.log(paths[0])
}

part1()
part2()