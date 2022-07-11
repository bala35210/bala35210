from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
from os import path

'''
Multi Color Function that does the job of color business in the wordcloud. 
Refer https://hslpicker.com/ for the color of your choice and enter the three numbers in a list for every color.
'''
def multi_color_func(word=None, font_size=None,
                     position=None, orientation=None,
                     font_path=None, random_state=None):
    colors = [[164, 100, 31],
              [160, 36, 74]]
    rand = random_state.randint(0, len(colors) - 1)
    return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])

'''
Load in the mask from the directory and masking works only when the background is white.
So, we make the background white. 'Masking out' the white.
'''
mask_color = np.array(Image.open('blank.png'))
mask = mask_color.copy()
mask[mask.sum(axis=2) == 0] = 255

#Get the text file containing the list of code-words. Higher the 'Bigger' in the wordcloud!
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d,'test_word.txt')).read()

'''
WordCloud DEFINITION:
prefer_horizontal = 1 makes the words only horizontal fit
max_font_size -> the max font size that can go in
relative_scaling of 0 makes word weight in the order they are entered in the text file. For example, relative scaling of 1 will mean that words that are twice as 
    frequent are prioritized and appear bigger.
repeat = True | allows for repeats.
'''
wc = WordCloud(mask=mask, background_color="white",
               prefer_horizontal=1,repeat=True,
               max_words=100000, max_font_size=50,
               relative_scaling=0,
               width=mask.shape[1], height=mask.shape[0],
               color_func = multi_color_func).generate(text)

#Plotting the wordcloud and display!
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()

#Command to export it as png file.
#wc.to_file(path.join(d,'export.png'))

#Export as svg
with open('export.svg', 'w') as f:
    f.write(WordCloud.to_svg(wc))
