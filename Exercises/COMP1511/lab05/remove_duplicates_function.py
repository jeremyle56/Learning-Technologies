
def remove_duplicates(length, source, destination):
    destination_upto = 0
    source_upto = 0

    for i in range(length):
        duplicate = 0
        checking = 0
        for checking in range(source_upto) and duplication == 0:
            if (source[source_upto] == source[checking]):
                duplicate = 1

        if !duplicate:
            destination[destination_upto] = source[source_upto]
            destination_upto += 1
        
        source_upto += 1
    return destination_upto
