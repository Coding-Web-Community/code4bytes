package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"strconv"
	"strings"
)

type Test struct {
	Input  string `json:"input"`
	Result int    `json:"result"`
	Fails  bool   `json:"fails"`
}

var hexMap = map[string]int{
	"A": 10,
	"B": 11,
	"C": 12,
	"D": 13,
	"E": 14,
	"F": 15,
}

func hexToDecimal(hex string) (decimal int, err error) {
	split := strings.Split(hex, "")
	length := len(split)

	for i, char := range split {
		var num int
		num, strConvErr := strconv.Atoi(char)
		if strConvErr != nil {
			if num = hexMap[char]; num == 0 {
				return 0, errors.New(fmt.Sprintf("hex: %v not valid", hex))
			}
		}

		decimal += num * int(math.Pow(16, float64(length-i+-1)))
	}

	return decimal, nil
}

func readFile(filename string) []byte {
	b, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Println(err)
	}

	return b
}

func main() {

	var tests []Test

	b := readFile("tests.json")
	err := json.Unmarshal(b, &tests)
	if err != nil {
		fmt.Println(err)
	}

	for _, test := range tests {
		r, err := hexToDecimal(test.Input)

		if err != nil && test.Fails == true {
			fmt.Printf("Testcase: '%v' | Expected: err, got: err\n", test.Input)
		} else {
			fmt.Printf("Testcase: '%v' | Expected: %v, got: %v\n", test.Input, test.Result, r)
		}

	}
}
