from frontmatter import Frontmatter

a = 1
  
d=Frontmatter.read_file("야채볶음밥.md")



print(f"{d['attributes']}")
