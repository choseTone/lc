__author__ = 'wangqc'

# https://leetcode.com/problems/smallest-sufficient-team/


class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_idx = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, person in enumerate(people):
            curr_skills = 0
            for skill in person:
                if skill in skill_idx:
                    curr_skills |= 1 << skill_idx[skill]
            for team_skills, team in list(dp.items()):
                cand = team_skills | curr_skills
                if cand != team_skills and (cand not in dp or len(dp[cand]) > len(team) + 1):
                    dp[cand] = team + [i]
        return dp[(1<<len(req_skills))-1]


if __name__ == '__main__':
    sol = Solution()

    t1 = ["java","nodejs","reactjs"], \
         [
             ["java"],
             ["nodejs"],
             ["nodejs","reactjs"]
         ],
    print(sol.smallestSufficientTeam(*t1))

    t2 = ["algorithms","math","java","reactjs","csharp","aws"], \
         [
             ["algorithms","math","java"],
             ["algorithms","math","reactjs"],
             ["java","csharp","aws"],
             ["reactjs","csharp"],
             ["csharp","math"],
             ["aws","java"]
         ],
    print(sol.smallestSufficientTeam(*t2))