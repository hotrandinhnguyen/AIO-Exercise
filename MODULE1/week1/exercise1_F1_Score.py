def f1_score(tp, fp, fn) :
    #check condition1
    dictionary_check = {"tp":tp, "fp":fp, "fn":fn} # use dictionary because dictionary have values and key, ez to access
    for i in dictionary_check:
        try:
            if dictionary_check[i] == int(dictionary_check[i]):
                pass
        except:
            print(f"{i} must be int")
            return
    #change type to calc
    tp = int(tp)
    fp = int(fp)
    fn = int(fn)
    #check condition1
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    #calc Precision
    precision = tp/(tp+fp)
    #calc Recall
    recall = tp/(tp+fn)
    #calc F1-score
    f1_score = 2*precision*recall/(precision+recall)
    #print Precision, Recall, F1-score              
    print(f"Precision is {precision}")
    print(f"Recall is {recall}")
    print(f"F1-score is {f1_score}")


def exercise1():
    tp = input("tp =")
    fp = input("fp =")
    fn = input("fn =")
    f1_score(tp, fp, fn)


if __name__=='__main__':
    exercise1()
