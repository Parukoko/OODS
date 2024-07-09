def find_countdown_sequences(numbers):
  countdowns = []
  temp = []
  for n in numbers:
    if n == 1:
      temp.append(1)
      if len(temp) > 1:
        countdowns.append(temp)
      else:
        countdowns.append([1])
      temp = []
    elif temp and n == temp[-1] - 1:
      temp.append(n)
    else:
      temp = [n] if n > 1 else []

  return [len(countdowns), countdowns]

print("*** Fun with countdown ***")
lst = list(map(int, input("Enter List : ").split()))
count, sequence = find_countdown_sequences(lst)
print(f"[{count}, {sequence}]")

