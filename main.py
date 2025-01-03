def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words=file_contents.split()
        print(f'{len(words)} words found in the document')
        lowered_words=[]
        for word in words:
            lowered_words.append(word.lower())
        character_counts = count_characters(lowered_words)
        reported = report(character_counts)
        #print(character_counts)

def count_characters(words):
    result = {}
    for word in words:
        for char in word:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result


def report(result):
    #key,value in result
    for key,value in result.items():
        print(f'The {key} character was found {value} times')



main()


