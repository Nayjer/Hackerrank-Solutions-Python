def matchingStrings(strings, queries):
  return [strings.count(queries[i]) for i in range(len(queries))]
