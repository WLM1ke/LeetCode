package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	minusN := head
	current := head
	counter := 0

	for current.Next != nil {
		if counter > n-1 {
			minusN = minusN.Next
		}
		current = current.Next
		counter++
	}

	if counter == n-1 {
		return head.Next
	}

	minusN.Next = minusN.Next.Next

	return head
}
