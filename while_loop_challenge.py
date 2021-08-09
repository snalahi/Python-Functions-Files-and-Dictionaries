def beginning(a_list):
  i = 0
  while i < len(a_list):
    if a_list[i] == 'bye':
      if i == 0:
        return []
      elif i < 10:
        return a_list[:i]
      else:
        break
    i += 1
  return a_list[:10]
