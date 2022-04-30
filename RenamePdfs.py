import textract
from shutil import copyfile
# copyfile(src, dst)

for i in range(1,147):
    fname = 'data/History_' + str(i) + '.pdf'
    text = textract.process(fname).decode("utf-8")
    text = text.split('\r\n\r\n')
    if text[3].find('MAIN IDEA'):
        text = text[2]
    else:
        text = text[2] + text[3]
    print(text)
    name = text.partition('\n')[0]
    name = name[:-1]
    dst = 'data/' + str(i) + '_' + name + '.pdf'
    print(dst)
    copyfile(fname, dst)




