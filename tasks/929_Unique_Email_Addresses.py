# https://leetcode.com/problems/unique-email-addresses/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        send = set()
        for mail in emails:
            loc, dom = mail.split("@")
            loc = loc.split("+")[0].replace(".", "")
            send.add((loc, dom))

        return len(send)
