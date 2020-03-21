//Written by Bork

package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "math"
    "net/http"
    "strconv"
    "strings"
    "time"
)

func main() {
    start := time.Now()

    var arr string = "["
    var list [][]string
    var sum float64
    var count float64 = 0.0
    var max int = 100
    var standardDeviance float64
    var mean float64

    for i := 1; i <= max; i++ {
        resp, err := http.Get("http://codingweb.eu-central-1.elasticbeanstalk.com/toiletgang")
        if err != nil {
            panic(err)
        }

        if resp.StatusCode == 429 {
            fmt.Println("429 Reached.")
            continue
        }

        content, err := ioutil.ReadAll(resp.Body)
        if err != nil {
            panic(err)
        }

        if i != max {
            arr += string(content) + ","
        } else {
            arr += string(content)
        }

        time.Sleep(time.Nanosecond * 500000000)
    }

    arr += "]"

    fmt.Println(arr)

    dec := json.NewDecoder(strings.NewReader(arr))
    err := dec.Decode(&list)
    fmt.Println(err, list)

    for _, list := range list {
        for _, interior := range list {
            float, err := strconv.ParseFloat(interior, 64)
            if err != nil {
                panic(err)
            }
            fmt.Println(sum)
            sum += float
            count += 1.0
        }
    }

    mean = sum / count

    for _, list := range list {
        for _, interior := range list {
            float, err := strconv.ParseFloat(interior, 64)
            if err != nil {
                panic(err)
            }
            standardDeviance += math.Pow(float-mean, 2)
        }
    }

    standardDeviance = math.Sqrt(standardDeviance / count)
    fmt.Println("Standard Deviation: ", standardDeviance)

    elapsed := time.Since(start)

    fmt.Println(fmt.Sprintf("[Finished] \nStandard Deviation: %g \nMean of Items: %g \nTime Taken to Complete: %s", standardDeviance, mean, elapsed))
}
