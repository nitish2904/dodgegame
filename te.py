fw = open('high_score.txt', 'w')
fw.write(str(0))
fw.close()

fr = open('high_score.txt', 'r')
txt = fr.read()
print(txt)
fr.close()