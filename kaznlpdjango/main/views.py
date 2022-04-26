from django.shortcuts import render
import kaznlpdjango.morphologic.tutorial

def index(request):
    return render(request, 'main/index.html')


# Create your views here.
#     txt = 'Введите текст на казахском языке для токенизации: '
#     # Көш жүре түзеледі. Ақсақ қой түстен кейін маңырайды.
#     tokrex = TokenizeRex()
#     sents_toks = tokrex.tokenize(txt)


    # mdl = os.path.join('kaznlp', 'tokenization', 'tokhmm.mdl')
    # tokhmm = TokenizerHMM(model=mdl)
    # sents_toks = tokhmm.tokenize(txt)

def tokenz(request):

    return render(request, 'main/tokenz.html',{'words':})


def normalize(request):
    return render(request, 'main/normalize.html')


def morphologic(request):
    return render(request, 'main/morpholog.html')
