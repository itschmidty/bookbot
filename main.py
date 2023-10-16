def main():
  path_to_file = "./books/frankenstein.txt"
  with open(path_to_file) as f:
    file_contents = f.read()
    number_of_words = count_words(file_contents)
    number_of_letters = count_letters(file_contents)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{number_of_words} words found in the document")
    for key in number_of_letters:
      print(f"The '{key}' character was found {number_of_letters[key]} times")
    print("--- End report ---")


def count_words(contents):
  return len(contents.split())

def count_letters(contents):
  counts = {}
  for letter in contents:
    converted = letter.lower()
    if converted.isalpha():
      if converted in counts:
        counts[converted] += 1
      else:
        counts[converted] = 1

  keys = list(counts.keys())
  keys.sort()
  sorted = {}

  for key in keys:
    sorted[key] = counts[key]

  return sorted

main()