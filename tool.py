with open('事象と空想 - ナナヲアカリ.mp4', 'rb')as source:
    with open('testfile', 'wb')as target_file:
        target_file.write(source.read(1024))
