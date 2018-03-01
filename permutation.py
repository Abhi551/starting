import time;
y=time.time();
def permute(word):
    n=len(word);
    if n==0:yield [];
    else :
        for i in range(n):
            for a in permute(word[:i]+word[i+1:]):
                yield [word[i]]+a;
def a(word):
    list_of_word,word,x,s=[],list(word),0,1;
    word.sort();
    for i in range(1,len(word)+1):
        s=s*i;
    for p in permute(list(word)):
        list_of_word.append("".join(p));
        x=x+1;
        if x==s/2:
            print len(list_of_word);
            print (time.time()-y);
            return list_of_word[x-1];