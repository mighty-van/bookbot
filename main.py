def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_contents(book_path)
    words_count = count_words(file_contents)
    char_dict = count_characters(file_contents)
    char_list = sort_char_dict(char_dict)
    print_report(book_path, words_count, char_list)


def get_book_contents(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(file_contents):
    count = file_contents.split();
    return len(count)


def count_characters(file_contents):
    char_dict = {}

    for c in file_contents:
        if c.lower() in char_dict:
            char_dict[c.lower()] += 1
        else:
            char_dict[c.lower()] = 1
    return char_dict


def print_report(book_path, total_words, char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document\n")

    for c in char_list:
        char = c["char"]
        count = c["count"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def sort_char_dict(char_dict):
    char_list = []

    for c in char_dict:
        if c.isalpha():
            char_list.append({"char": c, "count": char_dict[c]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(dict):
    return dict["count"]

    

main()