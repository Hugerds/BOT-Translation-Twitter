import tweepy
from googletrans import Translator

#
#


chave_consumidor = ""
segredo_consumidor = ""
token_acesso = ""
token_acesso_secreto = ""

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_secreto)

twitter = tweepy.API(autenticacao)
user = twitter.get_user('twitter')

def buscaTweet():
    resultados = tweepy.Cursor(twitter.search, q='@Twikipedia_', tweet_mode="extended").items(10)
    for tweet in resultados:
        idTweet = tweet.id
        idTrad = tweet.in_reply_to_status_id_str
        tuiteTrad = twitter.get_status(idTrad)
        textoTrad = tuiteTrad.text
        print(textoTrad)
        traduzaIsso(textoTrad, idTweet)

def traduzaIsso(textoTrad, idTweet):
    translator = Translator()
    tuiteTraduzido = translator.translate(textoTrad, dest='pt')
    tuitePostar = tuiteTraduzido.text
    try:
        twitter.update_status(tuitePostar, in_reply_to_status_id=idTweet, auto_populate_reply_metadata=True)
    except tweepy.TweepError as te:
        buscaTweet()
    print(tuiteTraduzido)
    buscaTweet()

buscaTweet()