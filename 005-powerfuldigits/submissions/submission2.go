package main

import (
    "fmt"
    "math"
)

//How many n-digit positive integers exist which are also an nth power?
func solution() int {
    cnt := 0                   // init count variable
    for a := 1; a < 100; a++ { // check for n to nth power
        for b := 1; b < 100; b++ {
            var res float64 = math.Pow(float64(a), float64(b)) // calc power
            var f string = fmt.Sprint(res)
            if len(f) == b { // check if its nth power
                fmt.Println(a, b, len(f), res)
                cnt++ // add to our count
            }
        }
    }
    return cnt // return it
}

func main() {
    fmt.Println(solution()) // run it
}

