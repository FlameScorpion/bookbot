import os
def main():
    path = "books/frankenstein.txt"
    name = os.path.basename(path)
    name_without_extension, extension = os.path.splitext(name)
    print("--- The report for " + name_without_extension + " starts here ---")
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(f"The total number of words is: {count}")
        lowered_characters = file_contents.lower()
        character_counts = counting(lowered_characters)
        list_of_characters = []

        for char, count in character_counts.items():
            if char.isalpha():
                list_of_characters.append({"char": char, "num": count})
        list_of_characters.sort(reverse=True, key=sort_on)
        for item in list_of_characters:
            #if item.isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End of the report ---")


def counting(lowered_characters):
    lowered = {}
    for c in lowered_characters:
        if c not in lowered:
            lowered[c] = 1
        else:
            lowered[c] += 1
    return lowered

def sort_on(dict):
    return dict["num"]

main()