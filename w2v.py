from gensim.models import KeyedVectors
filename = 'GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(filename, binary=True)

active = True

while active: 
    print("")    
    print("")    
    print("1) Word + Word")
    print("2) Word - Word")
    print("3) (Word + Word) - Word")
    print("4) (Word - Word) + Word")
    print("")    
    print("0) Exit")

    try: 
        answer = input("Option: ")
        print("")    
        if answer == str(1):
            first = input("word:")
            second = input("+ word:")
            result = model.most_similar(positive=[first, second], negative=[], topn=1)
            print('#------------------------------')
            print(result)
            print('#------------------------------')
        elif answer == str(2): 
            first = input("word:")
            second = input("- word:")
            result = model.most_similar(positive=[first], negative=[second], topn=1)
            print('#------------------------------')
            print(result)
            print('#------------------------------')
        elif answer == str(3):
            first = input("word:")
            second = input("+ word:")
            neg = input("- word:")
            result = model.most_similar(positive=[first, second], negative=[neg], topn=1)
            print('#------------------------------')
            print(result)
            print('#------------------------------')
        elif answer == str(4): 
            first = input("word:")
            second = input("- word:")
            pos = input("+ word:")
            result = model.most_similar(positive=[pos], negative=[first, second], topn=1)
            print('#------------------------------')
            print(result)
            print('#------------------------------')
        elif answer == str(0):
            active = False
        else:
            print("Please select a valid option number")
    except NameError:
        print("Error")            