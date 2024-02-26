from random import shuffle

example = [1,2,3,4,5,6,7]

result = shuffle(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)

result

[5,6,1,7,4,2,3]

mylist = [ ' ' , 'o' , ' ' ]

shuffle_list(mylist)

print(mylist)

def check_guess(mylist,guess):
    if mylist[guess] == 'o':
        print("correct!")
    else:
        print("wrong guess!")
        print(mylist)