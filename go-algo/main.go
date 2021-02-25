package main

import (
	"encoding/json"
	"fmt"
	_ "gopkg.in/karalabe/cookiejar.v2/collections/deque"
	"reflect"
	"strconv"
	"unsafe"
)


func main() {
	fmt.Println(findPeakElement([]int{1,2,3,1}))
	fmt.Println(findPeakElement([]int{1,2,1,3,5,6,4}))
}

func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}

func IsNumeric(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

func printSlice(iSlice interface{}) {
	switch slice := iSlice.(type) {
	case [][]bool:
		for _, value := range slice {
			fmt.Println(value)
		}
	case [][]string:
		for _, value := range slice {
			fmt.Println(value)
		}
	case [][]int:
		for _, value := range slice {
			fmt.Println(value)
		}
	case [][]float64:
		for _, value := range slice {
			fmt.Println(value)
		}
	case []bool:
		fmt.Println(slice)
	case []string:
		fmt.Println(slice)
	case []int:
		fmt.Println(slice)
	case []float64:
		fmt.Println(slice)
	}
}

func ContainsString(s []string, val string) bool {
	for i := range s {
		if s[i] == val {
			return true
		}
	}
	return false
}

func ReverseSlice(s interface{}) {
	n := reflect.ValueOf(s).Len()
	swap := reflect.Swapper(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		swap(i, j)
	}
}

func ReverseIntSlice(data []int) {
	for i, j := 0, len(data)-1; i < j; i, j = i+1, j-1 {
		data[i], data[j] = data[j], data[i]
	}
}

// ByteSliceToString is used when you really want to convert a slice of bytes to a string without incurring overhead.
// It is only safe to use if you really know the byte slice is not going to change in the lifetime of the string
func byteSliceToString(bs []byte) string {
	// This is copied from runtime. It relies on the string
	// header being a prefix of the slice header!
	return *(*string)(unsafe.Pointer(&bs))
}

func MaxInt(nums ...int) int {
	maxInt := nums[0]
	for i := range nums {
		if nums[i] > maxInt {
			maxInt = nums[i]
		}
	}
	return maxInt
}

func MinInt(nums ...int) int {
	minInt := nums[0]
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
}

func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}