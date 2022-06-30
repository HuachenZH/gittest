# readme:
# learning the module markdown
# la documentation est de la merde
# it is used for parsing markdown-syntax string into html stuffs like <div></div>
import markdown

#%% basic usage of markdown.markdown()
a=markdown.markdown("*boo!*")
b=markdown.markdown("**boo!**")
c=markdown.markdown("#boo!#")
print(a)
print(b)
print(c)

#%% create a new file or open an existing file
try:
    f = open("test.md", "x") # create a new file in the same directory as this py script. x means create.
except:
	f = open("test.md", "r") # if the file already exists, read it. r stands for read.


#%% output. rewrite the file
with open("test.md", "w", encoding="utf-8") as output_file:
    output_file.write(a)

#%% 
md=markdown.Markdown() # M in capital letter
print(type(md))