def empty_file(path):
    with open(path,"r+") as f:
        f.truncate(0)