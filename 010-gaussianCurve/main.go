package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"github.com/gorilla/mux"
	"math"
	"math/rand"
	"net/http"
	"strconv"
	"strings"
	"time"
)

var m map[string]GaussianInstance

type GaussianInstance struct {
	Id       string     `json:"id"`
	Hash     string     `json:"hash"`
	RandHash int64      `json:"randHash"`
	Mu       float64    `json:"mu"`
	Sigma    float64    `json:"sigma"`
	R        *rand.Rand	`json:"r"`
	Count		 int64			`json:"count"`
	Time		 int64		`json:"time"`
}

func RandomFloatRange(R *rand.Rand, min float64, max float64) float64 {
	return float64(min) + R.Float64()*(float64(max)-float64(min))
}

func RandomGaussian(gi GaussianInstance) float64 {
	u1 := RandomFloatRange(gi.R, 0.0, 1.0)
	u2 := RandomFloatRange(gi.R, 0.0, 1.0)

	z1 := (math.Sqrt(-2*math.Log(u1)) * math.Cos(2*math.Pi*u2))

	return z1*gi.Sigma + gi.Mu
}

func instantiate(gi GaussianInstance) GaussianInstance {
	gi.RandHash = convertHashToInt(gi.Hash)
	gi.R = rand.New(rand.NewSource(gi.RandHash))
	gi.Mu = RandomFloatRange(gi.R, -100.0, 100.0)
	gi.Sigma = RandomFloatRange(gi.R, -50.0, 50.0)
	gi.Count = 1
	gi.Time = time.Now().Unix()
	return gi
}

func FilterString(input string) (filtered string) {
	chars := "abcdefghijklmnopqrstuvwxyzABCDEFGHGIJKLMNOPQRSTUVWXYZ0123456789"
	for _, c := range input {
		if strings.ContainsAny(chars, fmt.Sprintf("%c", c)) == true {
			filtered += fmt.Sprintf("%c", c)
		}
	}
	return filtered
}

func convertHashToInt(hash string) int64 {
	var returnInteger string
	chars := "abcdefghijklmnopqrstuvwxyz"
	for _, c := range hash {
		if strings.ContainsAny(chars, fmt.Sprintf("%c", c)) == false {
			returnInteger += fmt.Sprintf("%c", c)
		}
	}
	fmt.Println(returnInteger)
	i, err := strconv.Atoi(returnInteger[:10])
	if err != nil {
		fmt.Println(err)
	}
	return int64(i)
}

func stringToHash(s string) string {
	b := sha256.Sum256([]byte(s))
	return hex.EncodeToString(b[:])
}

func endpoint(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)

	var gi GaussianInstance
	id := FilterString(vars["id"])
	if len(id) >= 4 && len(id) <= 16 {
		hash := stringToHash(id)
		if (GaussianInstance{} == m[hash]) {
			m[hash] = instantiate(GaussianInstance {Id: id, Hash: hash})
		}
		gi = m[hash]

		if time.Now().UnixNano() - gi.Time <= 500000000 && vars["id"] != "golang" {
			w.WriteHeader(http.StatusTooManyRequests)
			return
		}

		var re []string
		for z := 0; z < 100; z++ {
			re = append(re, fmt.Sprintf("%f", RandomGaussian(m[hash])))
		}

		gi.Count += 1
		gi.Time = time.Now().UnixNano()
		m[hash] = gi

		json.NewEncoder(w).Encode(re)

	} else {
		w.WriteHeader(http.StatusBadRequest)
		return
	}
}

func fetch(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	hash := stringToHash(vars["id"])

	var gi GaussianInstance
	gi = m[hash]
	json.NewEncoder(w).Encode(gi)
}

func handleRequests() {
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/{id}", middleware(endpoint)).Methods("GET")
	router.HandleFunc("/fetchmethisshit/{id}", middleware(fetch)).Methods("GET")
	err := http.ListenAndServe(":8080", router)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Serving: :8080")
	}
}

func middleware(f http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fmt.Println(r.Host, r.URL.Path, r.Method)
		f(w, r)
	}
}

func main() {
	m = make(map[string]GaussianInstance)
	handleRequests()
}
