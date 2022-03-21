package main

import (
	"bufio"
	"container/list"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	t := 0
	l := list.New()

	for true {
		f, err := os.Open("input.txt")

		if err != nil {
			log.Fatal(err)
		}

		defer f.Close()

		scanner := bufio.NewScanner(f)

		for scanner.Scan() {
			i, err := strconv.Atoi(scanner.Text())
			if err != nil {
				log.Fatal(err)
			}
			t += i
			for e := l.Front(); e != nil; e = e.Next() {
				if e.Value == t {
					fmt.Println("Resultado encontrado:")
					fmt.Println(t)
					os.Exit(0)
				}
			}
			l.PushFront(t)
		}

		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}

		// fmt.Println(t) Part 1
	}

}
