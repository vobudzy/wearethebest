def write_in_file():
    with open('file.txt', 'w') as writer:
        writer.write('I love Git')
        return True
