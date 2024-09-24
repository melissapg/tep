from collections import deque, defaultdict


def team_queue_simulation():
    scenario_index = 1
    while True:
        number_of_teams = int(input())
        if number_of_teams == 0:
            break

        print(f"Scenario #{scenario_index}")
        scenario_index += 1

        element_team_map = {}
        team_element_queues = defaultdict(deque)
        team_queue = deque()

        for team_index in range(number_of_teams):
            team_data = list(map(int, input().split()))
            team_id = team_index + 1
            for element in team_data[1:]:
                element_team_map[element] = team_id

        while True:
            command = input().strip()
            if command == "STOP":
                break

            if command.startswith("ENQUEUE"):
                _, element_value = command.split()
                element_value = int(element_value)
                team_id = element_team_map[element_value]

                if team_id not in team_queue:
                    team_queue.append(team_id)

                team_element_queues[team_id].append(element_value)

            elif command == "DEQUEUE":
                first_team_id = team_queue[0]
                dequeued_element = team_element_queues[first_team_id].popleft()
                print(dequeued_element)

                if not team_element_queues[first_team_id]:
                    team_queue.popleft()

        print()


team_queue_simulation()
