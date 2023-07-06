package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func read_input() []string {
	f, err := os.Open("../../input/day2")
	defer f.Close()
	check(err)

	lines := make([]string, 100)
	fileScanner := bufio.NewScanner(f)
	for fileScanner.Scan() {
		line := fileScanner.Text()
		lines = append(lines, line)
	}

	return lines
}

func main() {
	content := read_input()

	fmt.Printf("Total score of part one is %d\n", part_one(content))
	fmt.Printf("Total score of part two is %d\n", part_two(content))
}

func part_one(content []string) int32 {
	value_map := make(map[string]int)
	value_map["A X"] = 4
	value_map["B X"] = 1
	value_map["C X"] = 7
	value_map["A Y"] = 8
	value_map["B Y"] = 5
	value_map["C Y"] = 2
	value_map["A Z"] = 3
	value_map["B Z"] = 9
	value_map["C Z"] = 6

	totalScore := 0
	for _, line := range content {
		totalScore += value_map[line]
	}

	return int32(totalScore)
}

func part_two(content []string) int32 {
	value_map := make(map[string]int)
	value_map["A X"] = 3
	value_map["B X"] = 1
	value_map["C X"] = 2
	value_map["A Y"] = 4
	value_map["B Y"] = 5
	value_map["C Y"] = 6
	value_map["A Z"] = 8
	value_map["B Z"] = 9
	value_map["C Z"] = 7

	totalScore := 0
	for _, line := range content {
		totalScore += value_map[line]
	}

	return int32(totalScore)
}
