fw = open('sample-r-w.txt', 'w')
fw.write('writing some stuff in my text file\n')
fw.write('I like samosa, samosas are awesome\n')
fw.close()

fr = open('sample-r-w.txt', 'r')
text = fr.read()
print(text)
fr.close()