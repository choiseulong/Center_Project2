from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET["fulltext"]  
    #원문 전체를 가져온다 text라는 변수에 담아준다
    words = text.split()
    #공백기준으로 나눠 리스트로 바꾸어주는 것.
    word_dic = {}
    #빈사전을 만들어준다.
    for i in words :
        if i in word_dic :
            word_dic[i] += 1
            #증가
        else:
            word_dic[i] = 1
            #추가
    import operator
    sort = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'result.html', {'full' : text, 'total': len(words), 'dic' : word_dic.items(), 
    'TOP5':tuple(sort[:5]), 'TOP1': sort[0][0], 'TOP1_VAL' : sort[0][1], })
    #full 이라는 키값이 text를 대표한다