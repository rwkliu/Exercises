# You are given a 0-indexed array of positive integers tasks, 
# representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.
# Each day, until all tasks have been completed, you must either:
# Complete the next task from tasks, or take a break.
# Return the minimum number of days needed to complete all tasks.

#Incrememnt all values in the hash map
def update_hash(hash_map):
  for hash in hash_map:
      hash_map[hash] += 1
  return hash_map

#Compute the minimum days to complete all tasks
#A break is taken when days is incremented but the tasks index is not incremented
#Breaks occur when the current task is not greater than spaces away from the previous
#task of the same type
def task_schedule(tasks, space):
  task_hash = {}
  days = 0
  i = 0

  while i < len(tasks):
    update_hash(task_hash)
    
    if tasks[i] not in task_hash:
      task_hash.update({tasks[i]:0})
    elif task_hash[tasks[i]] <= space:
      days += 1
      continue
    else: 
      task_hash[tasks[i]] = 0
    i += 1
    days += 1
  return days

if __name__ == "__main__":
  print("days:", task_schedule([1,2,1,2,3,1], 3))
  print("days:", task_schedule([5,8,8,5], 2))
