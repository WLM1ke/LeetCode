package main

import "strings"

var symbols = []struct {
	arab  int
	roman string
}{
	{1000, "M"},
	{900, "CM"},
	{500, "D"},
	{400, "CD"},
	{100, "C"},
	{90, "XC"},
	{50, "L"},
	{40, "XL"},
	{10, "X"},
	{9, "IX"},
	{5, "V"},
	{4, "IV"},
	{1, "I"},
}

func intToRoman(num int) string {
	var s strings.Builder

	for _, symbol := range symbols {
		for num >= symbol.arab {
			s.WriteString(symbol.roman)
			num -= symbol.arab
		}
	}

	return s.String()
}
