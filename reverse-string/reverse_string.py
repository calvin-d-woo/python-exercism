def reverse(text):
    def reverse_acc(text, acc):
        if text=="":
            return acc
        else:
            return reverse_acc(text[1:],text[0] + acc)
    return reverse_acc(text,"")    
