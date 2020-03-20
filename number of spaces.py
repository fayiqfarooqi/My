x = "where there is a will there is a way"
s = 0
for i in range(len(x)):
    if x[i] == ' ':
        s = s + 1
print("there are",s,"spaces in this sentence")