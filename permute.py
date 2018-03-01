def permute(word):
    if n==0:yield [];
    else :
        for i in range(n):
            for a in permute(word[:i]+word[i+1:]):
                yield [word[i]]+a;
def middle_permutation(word):
    list_of_word,word,x,s=[],list(word),0,1;
    for i in range(n):
        s=s*i;
    word.sort();
    for p in permute(word):
        x=x+1;
        if x==s/2-1:
            return list_of_word([x]);
        list_of_word.append("".join(p));
    print list_of_word;
    return list_of_word[len(list_of_word)/2-1];
