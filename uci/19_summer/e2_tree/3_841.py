__author__ = 'wangqc'


# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms):
        q, seen = [0], {0}
        for node in q:
            for nei in rooms[node]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
        return len(seen) == len(rooms)


if __name__ == '__main__':
    sol = Solution()

    t1 = [[1],[2],[3],[]],
    print(sol.canVisitAllRooms(*t1))

    t2 = [[1,3],[3,0,1],[2],[0]],
    print(sol.canVisitAllRooms(*t2))