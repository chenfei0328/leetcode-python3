import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_num = [0] * 26
        for task in tasks:
            task_num[ord(task) - ord('A')] += 1
        task_num.sort()
        # print(task_num)

        max_val = task_num[25] - 1
        slots = max_val * n

        for i in range(24, -1, -1):
            slots -= min(task_num[i], max_val)
        return slots + len(tasks) if slots > 0 else len(tasks)