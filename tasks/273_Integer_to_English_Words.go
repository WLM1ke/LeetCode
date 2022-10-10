package main

import "strings"

var thousands = []struct {
	div  int
	word string
}{
	{1000000000, " Billion"},
	{1000000, " Million"},
	{1000, " Thousand"},
	{1, ""},
}

var (
	digitsNames = []string{
		"",
		" One",
		" Two",
		" Three",
		" Four",
		" Five",
		" Six",
		" Seven",
		" Eight",
		" Nine",
	}
	teensNames = []string{
		" Ten",
		" Eleven",
		" Twelve",
		" Thirteen",
		" Fourteen",
		" Fifteen",
		" Sixteen",
		" Seventeen",
		" Eighteen",
		" Nineteen",
	}
	tensNames = []string{
		"",
		"",
		" Twenty",
		" Thirty",
		" Forty",
		" Fifty",
		" Sixty",
		" Seventy",
		" Eighty",
		" Ninety",
	}
)

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	var builder strings.Builder

	for _, desc := range thousands {
		thousand := num / desc.div
		num %= desc.div
		if thousand > 0 {
			buildThousand(&builder, thousand)
			builder.WriteString(desc.word)
		}
	}

	return builder.String()[1:]
}

func buildThousand(builder *strings.Builder, n int) {
	hundreds := n / 100
	n %= 100
	if hundreds > 0 {
		builder.WriteString(digitsNames[hundreds])
		builder.WriteString(" Hundred")
	}

	tens := n / 10
	n %= 10
	if tens >= 2 {
		builder.WriteString(tensNames[tens])
	} else if tens == 1 {
		builder.WriteString(teensNames[n])
		n = 0
	}

	if n > 0 {
		builder.WriteString(digitsNames[n])
	}
}
