def find_the_redheads(family):
    redheads = []
    
    for member in family[0]:
        if family[0][member] == "red":
            redheads.append(member)

    return redheads

nu_framily = [
    {"florian":"red",
    "marie":"blonde",
    "virginie":"brunette",
    "david":"red",
    "franck":"red"}]

print(find_the_redheads(nu_framily))
