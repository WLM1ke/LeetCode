package main

// https://leetcode.com/problems/satisfiability-of-equality-equations/
func equationsPossible(equations []string) bool {
	graph := make(map[string]string)
	notEq := make([][2]string, 0)

	for _, eq := range equations {
		first := eq[:1]
		second := eq[3:]

		if eq[1:3] == "==" {
			parent1 := findRoot(first, graph)
			parent2 := findRoot(second, graph)

			if parent1 != parent2 {
				graph[parent1] = parent2
			}
		} else {
			notEq = append(notEq, [2]string{first, second})
		}
	}

	for _, pairs := range notEq {
		if findRoot(pairs[0], graph) == findRoot(pairs[1], graph) {
			return false
		}
	}

	return true
}

func findRoot(variable string, graph map[string]string) string {
	if parent, ok := graph[variable]; ok {
		return findRoot(parent, graph)
	} else {
		return variable
	}
}
