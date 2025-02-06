# كتابة نص في ملف
with open("example.txt", "w") as file:
    file.write("Hello, this is a text file!")

# قراءة محتوى الملف
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
