print("Enter the values of the array:")
arr = []
for i in range(5):
    element = int(input("Enter value based on user order: "))
    arr.append(element)
if arr == sorted(arr):
    print(f"{arr[4]} shark is alive")
eliminated = []
for i in range(4):
    for j in range(i+1, 5):
        if arr[i] < arr[j]:
            eliminated.append(arr[i])
print(f"Killed sharks are: {list(set(eliminated))}")