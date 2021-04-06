with open('Release.zip', 'rb') as file_data:
    bytes_content = file_data.read()
    # print(bytes_content)
with open('test.txt', 'wb') as f:
    f.write(bytes_content)
