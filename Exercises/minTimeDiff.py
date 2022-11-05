# Given a list of 24-hour clock time points in "HH:MM" format, return the 
# minimum minutes difference between any two-time points in the list.

# Convert HH:MM to number of minutes
def convertToMin(time_array):
  minute_array = []
  for time in time_array:
    time_split = time.split(":")
    if(time_split[0] == "00" and time_split[1] == "00"):
      time_split[0] = "24"
    hour_to_min = int(time_split[0]) * 60
    minutes = int(time_split[1])
    minute_array.append(hour_to_min + minutes)
  return minute_array

#Find the minimum minute difference
def findMinDifference(time_array):
  sorted_time = sorted(convertToMin(time_array))
  minute_diff = sorted_time[1] - sorted_time[0]
  for x in range(1,len(sorted_time) - 1):
    time_diff = sorted_time[x+1] - sorted_time[x]
    if(time_diff < minute_diff):
      minute_diff = time_diff
  return minute_diff

if __name__ == "__main__":
  time_points =  ["23:59","00:00"]
  time_points2 = ["00:00","23:59","00:00"]
  time_points3 = ['11:43','18:42','11:29','20:37','12:31','21:24','02:42','18:06','00:38','03:43']

  print(findMinDifference(time_points))
  print(findMinDifference(time_points2))
  print(findMinDifference(time_points3))