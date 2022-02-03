lines_per_file = 2340
smallfile = None
with open('/home/dilsad/BeCode_Projects/challenge-collecting-data/ressources/all_items.txt', ) as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            print(lineno)
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()