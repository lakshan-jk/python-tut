# Write to file
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Hey Thambi!\n")
# Read from file
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
