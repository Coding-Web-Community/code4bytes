package main

import (
	"encoding/json"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	var tests []struct {
		Input  string `json:"input"`
		Result int    `json:"result"`
		Fails  bool   `json:"fails"`
	}

	bites, err := os.ReadFile("tests.json")
	if err != nil {
		fmt.Println("dies x3")
		return
	}
	json.Unmarshal(bites, &tests)

	for _, test := range tests {
		output, fails := hexdecimal(test.Input)
		fmt.Printf("Input: %v\nExpected: %v  Got: %v\nFails: %v, Got:%v\ngamer win?: %v\n\n", test.Input, test.Result, output, test.Fails, fails, test.Result == output && test.Fails == fails)
	}
}

func hexdecimal(input string) (int, bool) {
	output := 0
	splitteth := strings.Split(strings.ToLower(input), "")

	for i, j := 0, len(splitteth)-1; i < j; i, j = i+1, j-1 {
		splitteth[i], splitteth[j] = splitteth[j], splitteth[i]
	}

	for index, char := range splitteth {
		if !strings.ContainsAny(char, "1234567890abcdef") {
			return 0, true
		}
		var charValue int
		if strings.ContainsAny(char, "abcdef") {
			charValue = int(char[0] - 87)
		} else {
			charValue, _ = strconv.Atoi(char)
		}

		output = output + charValue*int(math.Pow(16, float64(index)))

	}
	return output, false
}