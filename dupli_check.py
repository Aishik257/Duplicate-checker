def duplicate_checker():
    with open("data.txt","r") as f:
        data = f.read().split()

    seen = []
    duplicates = []

    for item in data:
        if item not in seen:
            if item not in duplicates:
                duplicates.append(item)
            else:
                seen.append(item)

    print("Duplicates: ",duplicates)

duplicate_checker()