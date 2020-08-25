package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"strings"

  "time"
)

var (
	extentions = map[string]string{
		"py":  "python3",
		"js":  "node",
		"ex":  "elixir",
		"cpp": "gcc",
		"go":  "go",
    "java": "java",
	}

	TESTCASES []testCase
)

type testCase struct {
	S     string `json:"s"`
	T     string `json:"t"`
	Truth string `json:"truth"`
}

func init() {
	jsonFile, err := os.Open("test_cases.json")
	defer jsonFile.Close()

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(jsonFile)
	for scanner.Scan() {
		var testcase testCase

		json.Unmarshal([]byte(scanner.Text()), &testcase)
		TESTCASES = append(TESTCASES, testcase)
	}

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(TESTCASES)
	fmt.Println(len(TESTCASES))
}

func main() {
	cwd, _ := os.Getwd()
	files, _ := ioutil.ReadDir(fmt.Sprintf("%s/submissions", cwd))
	for _, file := range files {
		fn := file.Name()
		cmnd := GetFileCommand(file.Name())

		var err error
		var out []byte

		var failed bool

    start := time.Now()

		for _, testcase := range TESTCASES {

			s := testcase.S
			t := testcase.T
			truth := testcase.Truth

			if cmnd == "go" {
				out, err = exec.Command(cmnd, "run", fmt.Sprintf("%s/submissions/%s", cwd, fn), s, t).Output()
			} else {
				out, err = exec.Command(cmnd, fmt.Sprintf("%s/submissions/%s", cwd, fn), s, t).Output()
			}
			if err != nil {
				fmt.Println(err)
			}

			resp := strings.ToLower(strings.Replace(string(out), "\n", "", -1))

			if resp != truth {
				failed = true
				fmt.Println(s, t, truth, resp)
				break
			}
		}

		if failed == true {
			fmt.Printf("%v failed!\n", fn)
		} else {
			fmt.Printf("%v correct!  %v\n", fn, time.Now().Sub(start))
		}
	}
}

func StringIn(s string, a []string) bool {
	for _, t := range a {
		if s == t {
			return true
		}
	}
	return false
}

func GetFileCommand(filename string) string {
	s := strings.Split(filename, ".")
	return extentions[s[len(s)-1]]
}
