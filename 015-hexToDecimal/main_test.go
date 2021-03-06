package main

import (
	"encoding/json"
	"log"
	"os"
	"testing"
)

func TestHexToDecimal(T *testing.T) {

	var tests []Test

	f, err := os.Open("tests.json")
	if err != nil {
		log.Println(err)
	}

	var b []byte
	_, err = f.Read(b)
	if err != nil {
		log.Println(err)
	}

	err = json.Unmarshal(b, &tests)

	for _, test := range tests {
		r, err := hexToDecimal(test.Input)
		if err != nil && test.Fails == true {
			continue
		}

		if err != nil {
			T.Fatalf(`Testcase: "%v" failed with error: %v`, test.Input, err)
		}

		if r != test.Result {
			T.Fatalf(`Testcase: "%v" failed. Expected: %v, got: %v`, test.Input, test.Result, r)
		}
	}
}
