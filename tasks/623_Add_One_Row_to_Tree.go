package main

func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if depth == 1 {
		return &TreeNode{
			Val:   val,
			Left:  root,
			Right: nil,
		}
	}

	if depth == 2 {
		root.Left = &TreeNode{
			Val:   val,
			Left:  root.Left,
			Right: nil,
		}
		root.Right = &TreeNode{
			Val:   val,
			Left:  nil,
			Right: root.Right,
		}

		return root
	}

	if root.Left != nil {
		addOneRow(root.Left, val, depth-1)
	}

	if root.Right != nil {
		addOneRow(root.Right, val, depth-1)
	}

	return root
}
