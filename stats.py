def get_book_text(filepath):
	with open(filepath, encoding="utf-8-sig") as file:
		file_contents = file.read()
	return file_contents

def get_num_words(filepath):
	contents = get_book_text(filepath)
	contents_words = contents.split()
	counter = 0
	for word in contents_words:
		counter += 1
	return print(f"Found {counter} total words")

def get_num_letters(filepath):
	contents = get_book_text(filepath)
	contents_string = contents.lower()
	letter_counter = {}
	for char in contents_string:
		if char in letter_counter:
			letter_counter[char] += 1
		else:
			letter_counter[char] = 1
	return letter_counter

def sort_on(item):
	return item["num"]

def result(letter_counter):
	result_list = []
	for char, count in letter_counter.items():
		if char.isalpha():
			new_dict = {
				"char": char,
				"num": count
			}
			result_list.append(new_dict)
	result_list.sort(reverse=True, key=sort_on)
	combined_list = [f"{item['char']}: {item['num']}" for item in result_list]
	return print(combined_list)