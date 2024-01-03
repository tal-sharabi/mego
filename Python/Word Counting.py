file_path_original = input("Enter the file path: ")
file_path_corrected = file_path_original.replace("\\", "/").replace("\"","")
print(file_path_corrected)
with open(file_path_corrected, 'r') as file:
    # Read the entire file content
    content = file.read()
    cleaned_content = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in content)
    words_list = cleaned_content.split()
    num_of_words = len(words_list)
    print(f"Number of words: {num_of_words}")
    unique_words = set()
    for word in words_list:
        unique_words.add(word)
    print(f"Number of unique words: {len(unique_words)}")
    print("All words used:")
    for word in unique_words:
        counter = 0
        for i in range(len(words_list)):
            if word == words_list[i]:
                counter += 1
        print(word, counter)











