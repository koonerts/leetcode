package test

import (
	"errors"
	"go-algo/ext/sliceext"
	"reflect"
	"testing"
)


func BenchmarkSliceClearIterative(b *testing.B) {
	x := []int{10000:0}
	b.ResetTimer()
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		for i := range x {
			x[i] = 0
		}
	}
}

func BenchmarkSliceClearMake(b *testing.B) {
	x := []int{10000:0}
	b.ResetTimer()
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		x = make([]int, 10000)
	}
	b.StopTimer()
	_ = len(x)
}


func BenchmarkSliceLiteralCreate(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = []int{10000:0}
	}
}


func BenchmarkSliceMakeCreate(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = make([]int, 10000)
	}
}


func BenchmarkSliceReverseSwap(b *testing.B) {
	x := getIntSlice(1000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		sliceext.ReverseSlice(x)
	}
}

func BenchmarkSliceReverseUsingInterface(b *testing.B) {
	x := getIntSlice(1000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		reverseUsingInterface(x)
	}
}

func BenchmarkSliceReverseIntSlice(b *testing.B) {
	x := getIntSlice(1000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		sliceext.ReverseIntSlice(x)
	}
}

func BenchmarkSliceRotateLeft(b *testing.B) {
	x := getIntSlice(100000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		rotLeft(x, 50000)
	}
}

func BenchmarkSliceRotateLeftManual(b *testing.B) {
	x := getIntSlice(100000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		rotLeftManual(x, 50000)
	}
}

func rotLeftManual(a []int, d int) []int {
	n := len(a)
	k := int(d)%n
	if k == 0 {return a}

	cntr, start, idx := 0, len(a)-1, len(a)-1
	var prev = a[idx]
	for cntr < len(a) {
		nextIdx := mod(idx-k, n)
		tmp := a[nextIdx]
		a[nextIdx] = prev
		prev = tmp
		idx = nextIdx
		cntr++
		if idx == start {
			idx--
			prev = a[idx]
			start = idx
		}
	}
	return a
}

func mod(n, m int) int {
	res := n%m
	if res < 0 {
		return res+m
	}
	return res
}


func rotLeft(a []int, d int) []int {
	n := len(a)
	k := int(d)%n
	if k == 0 {return a}

	return append(a[k:], a[:k]...)
}

func getIntSlice(n int) []int {
	var x []int
	for i := 0; i < n; i++ {
		x = append(x, i)
	}
	return x
}

func reverseUsingInterface(data interface{}) {
	value := reflect.ValueOf(data)
	if value.Kind() != reflect.Slice {
		panic(errors.New("data must be a sliceext type"))
	}
	valueLen := value.Len()
	for i := 0; i <= int((valueLen-1)/2); i++ {
		reverseIndex := valueLen - 1 - i
		tmp := value.Index(reverseIndex).Interface()
		value.Index(reverseIndex).Set(value.Index(i))
		value.Index(i).Set(reflect.ValueOf(tmp))
	}
}
