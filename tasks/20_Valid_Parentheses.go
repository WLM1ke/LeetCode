package main

// https://leetcode.com/problems/valid-parentheses/
func isValid(s string) bool {
	stack := make([]rune, 0, len(s))
	brackets := map[rune]rune{
		'{': '}',
		'[': ']',
		'(': ')',
	}

	for _, bracket := range s {
		switch closing, ok := brackets[bracket]; {
		case ok:
			stack = append(stack, closing)
		case len(stack) == 0 || stack[len(stack)-1] != bracket:
			return false
		default:
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
