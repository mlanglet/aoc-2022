package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func read_input() []string {
	f, err := os.Open("../../input/day3")
	defer f.Close()
	check(err)

	lines := make([]string, 0)
	fileScanner := bufio.NewScanner(f)
	for fileScanner.Scan() {
		line := fileScanner.Text()
		lines = append(lines, line)
	}

	return lines
}

func main() {
	content := read_input()
	priority_values := make([]byte, 0)
	priority_values = append(priority_values, make_range(97, 122)...)
	priority_values = append(priority_values, make_range(65, 90)...)
	fmt.Printf("The sum of priorities for backpack sorting is %d\n", part_one(content, priority_values))
	fmt.Printf("The sum of priorities for badge authentication is %d\n", part_two(content, priority_values))
}

func get_priority_value(char byte, priority_values []byte) int {
	for i, v := range priority_values {
		if v == char {
			return i + 1
		}
	}
	return 0
}

func make_range(min, max byte) []byte {
	r := make([]byte, max-min+1)
	for i := range r {
		r[i] = min + byte(i)
	}
	return r
}

type HashSet map[byte]struct{}

func (set HashSet) Add(key byte) {
	set[key] = struct{}{}
}

func (set HashSet) Contains(key byte) bool {
	_, exists := set[key]
	return exists
}

func (set HashSet) Intersect(other HashSet) HashSet {
	intersection := make(HashSet)

	for k := range set {
		if other.Contains(k) {
			intersection.Add(k)
		}
	}

	return intersection
}

func (set HashSet) First() (byte, error) {
	for k := range set {
		return k, nil
	}
	return 0, errors.New("No entries in set")
}

func set_from_string(data string) HashSet {
	set := make(HashSet)
	for _, c := range data {
		set.Add(byte(c))
	}
	return set
}

func part_one(content []string, priority_values []byte) int {
	priority_sum := 0

	for _, backpack := range content {
		middle := len(backpack) / 2
		compartment1 := backpack[0:middle]
		compartment2 := backpack[middle:]
		set1 := set_from_string(compartment1)
		set2 := set_from_string(compartment2)
		common_letter, err := set1.Intersect(set2).First()
		check(err)
		priority_sum += get_priority_value(common_letter, priority_values)
	}

	return priority_sum
}

func part_two(content []string, priority_values []byte) int {
	priority_sum, items := 0, make([]string, 0)
	for _, backpack := range content {
		if len(items) == 3 {
			priority_sum += calculate_intersecting_priority_value(items, priority_values)
			items = items[3:]
		}
		items = append(items, backpack)
	}

	priority_sum += calculate_intersecting_priority_value(items, priority_values)

	return priority_sum
}

func calculate_intersecting_priority_value(items []string, priority_values []byte) int {
	set1 := set_from_string(items[len(items)-3])
	set2 := set_from_string(items[len(items)-2])
	set3 := set_from_string(items[len(items)-1])

	common_letter, _ := set1.Intersect(set2).Intersect(set3).First()

	return get_priority_value(common_letter, priority_values)
}
