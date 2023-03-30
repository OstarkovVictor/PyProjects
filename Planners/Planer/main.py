import sys

in_params = sys.stdin.readline().strip()

arr_in_params = []
arr_in_params.append(in_params.split())

count_data, bot, queues = int(arr_in_params[0][0]), int(arr_in_params[0][1]), int(arr_in_params[0][2])
arr_in_data = []



arr_bot =[[0, 1] for i in range(bot)]
arr_queues = [[] for i in range(queues)]
arr_queues_equal = [[] for i in range(queues)]
arr_end = [[] for i in range(count_data)]

for i in range(count_data):
        s = sys.stdin.readline().strip()
        arr_in_data.append((s.split()))



for i in range(count_data):
        arr_queues[int(arr_in_data[i][1]) - 1].append([int(arr_in_data[i][0]), int(arr_in_data[i][1]), int(arr_in_data[i][2]), i])

        arr_queues_equal[int(arr_in_data[i][1]) - 1].append([])
while True:
        if arr_queues==arr_queues_equal:break

        for i in range(bot):
            for i1 in range(queues):

                if arr_queues[i1] != arr_queues_equal[i1]:
                    if arr_bot[i][0] == 0   and   arr_queues[i1][0][0] <= arr_bot[i][1]:

                        arr_bot[i][0] = arr_queues[i1][0][2]
                        arr_end[arr_queues[i1][0][3]] = [i + 1, arr_bot[i][1]]

                        arr_queues[i1].pop(0)
                        arr_queues_equal[i1].pop(0)
                        arr_queues_equal.append(arr_queues_equal.pop(i1))
                        arr_queues.append(arr_queues.pop(i1))
                        # print(Oar,Oar123)

            arr_bot[i][1]+=1
            if arr_bot[i][0]>0: arr_bot[i][0]-=1
for i in range(count_data):print(type(*(arr_end[i])))
