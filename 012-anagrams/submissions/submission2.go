package main

import (
    "fmt"
    "os"
    "reflect"
    "sort"
    "strings"
)

func main() {
    args := os.Args[1:]

    if !(len(args) == 2) {
        fmt.Println("Incorrect amount of arguments")
        return
    }
    firstWord := strings.Split(args[0],"")
    secondWord := strings.Split(args[1],"")

    sort.Strings(firstWord)
    sort.Strings(secondWord)


    fmt.Println(reflect.DeepEqual(firstWord,secondWord))
}
