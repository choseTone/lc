__author_ = "wangqc"

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class LifeGame:
    def __init__(self, m, n, type=0):
        self.m, self.n = m, n
        if type == 1:
            self.A = [[i&1]*n for i in range(m)]
        elif type == 2:
            self.A = [[i&1^1]*n for i in range(m)]
        elif type == 3:
            self.A = [[1]*n for _ in range(m)]
        elif type == 4:
            self.A = [[m/4 < i < 3*m/4 and n/4 <= j < 3*n/4 for i in range(n)] for j in range(m)]
        elif type == 5:
            self.A = [[3*m/8 < i < 5*m/8 and 3*n/8 <= j < 5*n/8 for i in range(n)] for j in range(m)]
        elif type == 6:
            self.A = [[m/2-3 <= i <= m/2+3 and n/2-3 <= j <= n/2+3 for i in range(n)] for j in range(m)]
        elif type == 7:
            self.A = [[(i^j&1 and random.random() < 0.1) for j in range(n)] for i in range(m)]
        else:
            self.A = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]

    def next_generation(self):
        def nei(i,j):
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < self.m and 0 <= y < self.n:
                    yield x, y
        for i in range(self.m):
            for j in range(self.n):
                cnt = sum(self.A[x][y]&1 for x,y in nei(i,j))
                if cnt | self.A[i][j] == 3:
                    self.A[i][j] |= 2
        for i in range(self.m):
            for j in range(self.n):
                self.A[i][j] >>= 1

    def count(self):
        return sum(sum(row) for row in self.A)

    def print(self, live='1', dead='0'):
        print('='*self.n*3)
        for i in range(self.m):
            print(" ".join(live if x else dead for x in self.A[i]))
        print('='*self.n*3)

    def plot(self):
        xy = list(zip(*[(i,j) for i in range(self.m) for j in range(self.n) if self.A[i][j]]))
        if not xy:
            xy = [(), ()]
        return xy[1], xy[0]

if __name__ == "__main__":
    T, R, C = 7, 150, 150
    game = LifeGame(R, C, T)
    fig = plt.figure(figsize=(10,10))
    x, y = game.plot()
    ims = [plt.plot(x, y, 'g.') for _ in range(5)]
    for _ in range(400):
        game.next_generation()
        x, y = game.plot()
        plt.xlim(0, R)
        plt.ylim(0, C)
        ims.append(plt.plot(x, y, 'g.'))

    writer = animation.FFMpegWriter()
    plt.rcParams["animation.ffmpeg_path"] = "C:\\Users\lance\Documents\\ffmpeg-N-100493-gc720286ee3-win64-gpl\\bin\\ffmpeg.exe"
    im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=3000, blit=True)
    im_ani.save(f"life_game_{T}.mp4", writer=writer)
    plt.show()
