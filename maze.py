from microbit import *
import random
class Env:
    def __init__(self):
        # 0: 路 1: 起点 2: 终点 3: 墙 4: 大便
        self.map = [
            [1,0,0,0,3],
            [0,3,0,0,0],
            [0,0,3,0,3],
            [0,0,0,0,0],
            [3,4,0,3,2],
        ]
        self.map_size = 5
        self.action_space = ['u', 'd', 'l', 'r']
        self.entrance = [0, 0]
        self.reach_count = 0
        self.accuracy_offset = 0
        self.reset()
    def action_index(self, a):
        return self.action_space.index(a)
    def step(self, action):
        dest = self.actor_pos[:]
        if action == 'u':
            if self.actor_pos[0] - 1 >= 0:
                dest[0] -= 1
        elif action == 'd':
            if dest[0] + 1 < self.map_size:
                dest[0] += 1
        elif action == 'l':
            if dest[1] - 1 >= 0:
                dest[1] -= 1
        elif action == 'r':
            if dest[1] + 1 < self.map_size:
                dest[1] += 1
        
        v = self.map[dest[0]][dest[1]] 
        if v == 3:
            reward = -10
            done = True
        elif v == 4:
            reward = -30
            done = True
        elif v == 2:
            reward = 50
            done = True
            self.reach_count += 1
            if self.reach_count >= 10:
                self.reach_count = 0
                self.accuracy_offset += 1
        else:
            reward = -1
            done = False
        self.move_to(dest, done)
        return dest, reward, done
    def reset(self):
        self.init()
        self.actor_pos = self.entrance[:]
        display.set_pixel(self.actor_pos[1], self.actor_pos[0], 5)
        return self.actor_pos
    def move_to(self, dest_pos, done = False):
        display.set_pixel(self.actor_pos[1], self.actor_pos[0], 0)
        display.set_pixel(dest_pos[1], dest_pos[0], 5)
        self.actor_pos = dest_pos[:]
        if done == True:
            sleep(100)
    def init(self):
        for r in range(5):
            for c in range(5):
                if self.map[r][c] == 3:
                    display.set_pixel(c, r, 1)
                elif self.map[r][c] == 4:
                    display.set_pixel(c, r, 3)
                else:
                    display.set_pixel(c, r, 0)
                    
def find_all_max_index(arr):
    m = max(arr)
    result = []
    for i in range(len(arr)):
        if arr[i] == m:
            result.append(i)
    return result

class AI:
    def __init__(self, env, learning_rate=0.01, reward_decay=0.9, e_greddy=0.9):
        self.env = env
        self.q_table = {}
        self.lr = learning_rate
        self.elsilon = e_greddy
        self.gamma = reward_decay
    def find_max_action(self, s):
        all_max_index = find_all_max_index(self.q_table[str(s)])
        return self.env.action_space[random.choice(all_max_index)]
    def choose_action(self, s):
        self.make_sure_state_exist(s)
        r = random.randrange(0, 100)
        if r > 90 + self.env.accuracy_offset:
            action = random.choice(self.env.action_space)
        else:
            action = self.find_max_action(s)
        return action
    def make_sure_state_exist(self, s):
        if str(s) not in self.q_table.keys():
            self.q_table[str(s)] = [0] * len(self.env.action_space)
    def learn(self, s, a, r, s_):
        self.make_sure_state_exist(s_)
        a_index = self.env.action_index(a)
        q_predict = self.q_table[str(s)][a_index]
        if s_ == 2:
            q_target = r
        else:
            q_target = r + self.gamma * max(self.q_table[str(s_)])
        self.q_table[str(s)][a_index] += self.lr * (q_target - q_predict)
    def run(self):
        for episode in range(1000):
            s = self.env.reset()
            sleep(100)
            while True:
                a = self.choose_action(s)
                s_, r, done = self.env.step(a)
                self.learn(s, a, r, s_)
                s = s_
                if done:
                    break
                sleep(100)

agent = AI(Env())
agent.run()
