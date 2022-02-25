library(stringr)
library(wordcloud)
library(KoNLP)
library(qgraph)
text = read.csv("~/Desktop/MLP_4_Project/jm_data/data/폐교위기대학_news.csv")

ko.words=function(text){
    d = str_split(text, ';')
    extracted=tolower(str_match(d ,'([가-힣a-zA-Z]+)/[NVO]'))
    keyword=extracted[,2]
    keyword[!is.na(keyword)]
}
cps=Corpus(VectorSource(text$content))
tdm<-TermDocumentMatrix(cps,control=list(tokenize=ko.words,
                                         removePunctuation=T,
                                         stopwords = c('수', '있다', '대학', '등', 
                                                       '또', '위해', '이', '일', '더', 
                                                       '한다', '있도록', '개', '할', 
                                                       '위한', '함께', '한', '것이다', '것은', 
                                                       '해야', '또한', '등으로', '것도', '년', 
                                                       '월', '대학의', '있는', '대한', '및', 
                                                       '했다', '등을', '대해', '안', '이를', 
                                                       '대학에', '중', '그', '가장', '없다', 
                                                       '그리고', '따라', '게', '통해','하고', 
                                                       '같은', '된다', '대학을', '만', '때', 
                                                       '대', '이후', '한다는', '지난', '우리', 
                                                       '것이', '간', '지역의','될', '따른', '많은', '하는', '그래서',
                                                       '세','아니라','전','경우','있습니다','후','것','잘','말했다', '대학이',
                                                       '▲'),
                                         removeNumbers=T,
                                         worldLengths=c(2,Inf)))

Encoding(tdm$dimnames$Terms) = 'CP949'
dtm = as.DocumentTermMatrix(tdm)

freq=sort(colSums(as.matrix(dtm)), decreasing=TRUE)
wf=data.frame(word=names(freq), freq=freq)

wordcloud(names(freq),random.order = F, freq, min.freq= 45, color=brewer.pal(6, "Dark2"))
