import re

#Paragraph provided for search and replace

original_text='''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor.
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo.
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor.
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo.
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#this is the findall function, to get all of the instances of non alphanumeric characters in the string assigned to 'lorem_ipsum'

results=re.findall(r"[^a-zA-Z0-9]",lorem_ipsum)

#len function to print the characters that are not listed

print(len(results))

#this function findall finds all the instances of sit-amet included in lorem_ipsum, it is assigned to the variable and then printed

occurrance_sit_amet=re.findall(r"sit[:|-]amet",lorem_ipsum)
print(len(occurrance_sit_amet))

#sit-amet is replaced by sit amet and the results of the number of sit amet occurances are output

replace_results=re.sub(r"sit[:|-]amet",'sit amet',lorem_ipsum)
occurrance_sit_amet=re.findall(r"sit amet",replace_results)
print(len(occurrance_sit_amet))
