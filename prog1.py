def remove_duplicates(s):
  result =""
  for char in s:
    if char not in result:
      result += char
  return result
  input = "aabcad"
  print(remove_duplicates(input))