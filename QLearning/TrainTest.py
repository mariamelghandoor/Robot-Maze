def train_qlearning(q_agent, maze, agent, episodes, shape):
    for episode in range(episodes):
        s_t = maze.start
        agent.reset_visited()
        total_reward = 0
        done = False

        while not done:
            a_t = q_agent.get_action(s_t)

            # Determine the next state based on the action
            if a_t == 0:  # Up
                s_next = (max(s_t[0] - 1, 0), s_t[1])
            elif a_t == 1:  # Down
                s_next = (min(s_t[0] + 1, shape[0] - 1), s_t[1])
            elif a_t == 2:  # Left
                s_next = (s_t[0], max(s_t[1] - 1, 0))
            elif a_t == 3:  # Right
                s_next = (s_t[0], min(s_t[1] + 1, shape[1] - 1))

            if maze.is_open_Qlearning(s_next[0], s_next[1]):
                reward = maze[s_next]
            else:
                reward = -100  # Penalize hitting a wall
                s_next = s_t

            if s_next == maze.goal:
                reward = 1  # Reward for reaching the goal
                done = True

            q_agent.update(s_t, a_t, reward, s_next)
            s_t = s_next
            total_reward += reward

        if episode % 100 == 0:
            print(f"Episode {episode} completed with total reward: {total_reward}")

def test_qlearning(q_agent, maze, shape):
    s_t = maze.start
    path = [s_t]

    while s_t != maze.goal:
        a_t = q_agent.get_best_action(s_t)
        if a_t == 0:  # Up
            s_next = (max(s_t[0] - 1, 0), s_t[1])
        elif a_t == 1:  # Down
            s_next = (min(s_t[0] + 1, shape[0] - 1), s_t[1])
        elif a_t == 2:  # Left
            s_next = (s_t[0], max(s_t[1] - 1, 0))
        elif a_t == 3:  # Right
            s_next = (s_t[0], min(s_t[1] + 1, shape[1] - 1))

        if maze.is_open_Qlearning(s_next[0], s_next[1]):
            path.append(s_next)
            s_t = s_next
        else:
            break

    print("Optimal path:", path)
    maze.plot_Qlearning(path, "Q-Learning")
