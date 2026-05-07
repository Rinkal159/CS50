filename = input("File name: ").lower().strip()

if (filename.endswith(".gif") | filename.endswith(".png")):
    print("image/" + filename[filename.rfind(".") + 1:])

elif (filename.endswith(".jpeg") | filename.endswith(".jpg")):
    print("image/jpeg")

elif (filename.endswith(".pdf") | filename.endswith(".zip")) :
    print("application/" + filename[filename.rfind(".") + 1:])

elif (filename.endswith(".txt")):
    print("text/plain")

else:
    print("application/octet-stream")