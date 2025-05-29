# You are given a string. 
# Split the string on a " " (space)
# delimiter 
# and join using a - hyphen.



def split_and_join(line):
    """Splits a string by spaces and joins it with hyphens."""
    parts = line.split(" ")
    joined_string = "-".join(parts)
    return joined_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)