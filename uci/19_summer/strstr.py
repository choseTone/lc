__author_ = "wangqc"

# find T in S
class Strstr:
    def KMP(self, S: str, T: str) -> int:
        n, j = len(T), 0
        dfa = [0] * n
        for i in range(1, n):
            while j and T[i] != T[j]:
                j = dfa[j-1]
            dfa[i] = (j := j + (T[i] == T[j]))
        j = 0
        for i in range(len(S)):
            while j and S[i] != T[j]:
                j = dfa[j-1]
            if (j := j + (S[i] == T[j])) == n:
                return i - n + 1
        return -1


if __name__ == "__main__":
    kmp = Strstr().KMP

    print(kmp(
        S = "hello world", T = "world"
    ))

    print(kmp(
        S = "hello world", T = "word"
    ))

    print(kmp(
        S = "daabcbaabcbc", T = "abc"
    ))

    print(kmp(
        S = "aabacbaabcbc", T = "aba"
    ))

    print(kmp(
        S = "panamabanana", T = "anan"
    ))

