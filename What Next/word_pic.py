from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

f = open(u'./AkiraEN.txt', 'r').read()
wordcloud = WordCloud(
    background_color='white',
    width=1000,
    height=860,
    margin=2
).generate(f)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to.file('test.png')

