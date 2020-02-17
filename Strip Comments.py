def solution(string,markers):
    words = string.split('\n')
    texts = []
    for word in words:
        wordin = word
        for mark in markers:
            if len(wordin) > len(word.split(mark)[0]):
                try:
                    if word.split(mark)[0][-1] == ' ':
                        wordin = word.split(mark)[0][:-1]
                    else:
                        wordin = word.split(mark)[0]
                except expression as identifier:
                    pass

                                    
        texts.append(wordin)
    return '\n'.join(texts)

    #your code here

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(result)