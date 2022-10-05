package main

func isSymmetric(root *TreeNode) bool {
	return root == nil || symmetric(root.Left, root.Right)
}

func symmetric(rootL, rootR *TreeNode) bool {
	if rootL == nil || rootR == nil {
		return rootL == rootR
	}

	if rootL.Val != rootR.Val {
		return false
	}

	return symmetric(rootL.Left, rootR.Right) && symmetric(rootL.Right, rootR.Left)
}
