__author__ = 'wangqc'

'''
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''


class Solution:
    digit = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine',
             '10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen',
             '17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty',
             '60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety','100':'One Hundred'}
    ty = {'2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
    seg_level = ['Billion', 'Million', 'Thousand', '']

    def numberToWords(self, num):
        num, ans = str(num), ''
        if len(num) % 3:
            num = '0' * (3 - len(num) % 3) + num
        n = len(num) // 3
        for i in range(n):
            seg = self.convert_seg(num[3*i: 3*i+3].lstrip('0'))
            if seg: ans += '%s %s ' % (seg, self.seg_level[4 - n + i])
        return ans.rstrip() or 'Zero'

    def convert_seg(self, num):
        return num and (self.digit[num] if num in self.digit
                        else '%s %s' % (self.ty[num[0]], self.digit[num[1]]) if len(num) == 2
                        else '%s Hundred %s' % (self.digit[num[0]], self.convert_seg(num[1:].lstrip('0')))).rstrip()


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.numberToWords(200000)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
