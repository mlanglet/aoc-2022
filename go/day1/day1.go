package main

import (
       "bufio"
       "fmt"
       "os"
       "strconv"
)

func check(e error) {
     if e != nil {
     	panic(e)
     }
}

func main(){
     f, err := os.Open("../../input/day1")
     defer f.Close()
     check(err)

     max, current := 0, 0
     
     fileScanner := bufio.NewScanner(f)
     for fileScanner.Scan() {
      	 text := fileScanner.Text()
     	 if text == "" {
	 	    if current > max {
		 	    max = current
		    }
		    current = 0
         } else {
	        v, _ := strconv.Atoi(text)
	        current += v
	     }
     }
     
     fmt.Printf("The most carried calories is %v!\n", max)
}
