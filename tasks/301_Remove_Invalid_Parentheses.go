package main

func removeInvalidParentheses(s string) []string {
	pre := map[string]bool{s: true}

	for {
		rez := make(map[string]bool, len(pre))

		for s := range pre {
			if check(s) {
				rez[s] = true
			}
		}

		if len(rez) > 0 {
			out := make([]string, 0, len(rez))

			for i := range rez {
				out = append(out, i)
			}

			return out
		}

		new_pre := make(map[string]bool, len(pre)*len(s))
		for s := range pre {
			for i := 0; i < len(s); i++ {
				new_pre[s[:i]+s[i+1:]] = true
			}
		}

		pre = new_pre
	}
}

func check(s string) bool {
	count := 0

	for _, i := range s {
		if i == '(' {
			count++
		} else if i == ')' && count == 0 {
			return false
		} else if i == ')' {
			count--
		}
	}

	return count == 0
}
