# Three solution for single query

text = input("Write the string")
reversed_text = ""
i=len(text)-1

while  i>=0:
    reversed_text+=text[i]
    i-=1
    
print(reversed_text)





text = input("Write the string")
reversed_text = ""
for char in text:
    reversed_text= char + reversed_text
    
print(reversed_text)

    

text = input("Write the string")
reversed_text = ""
i = len(text)-1
for i in range(i,-1,-1):
    reversed_text+=text[i]
    
    
print(reversed_text)
