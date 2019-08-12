__author__ = 'wangqc'


# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails):
        return len(set(map(self.convert, emails)))

    def convert(self, email):
        x, domain = email.split('@')
        i = x.find('+')
        return f"{(x if i<0 else x[:i]).replace('.', '')}@{domain}"


if __name__ == '__main__':
    sol = Solution()
    t1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"],
    print(sol.numUniqueEmails(*t1))
