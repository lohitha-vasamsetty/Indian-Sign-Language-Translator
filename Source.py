import os 
from logging import exception
from tkinter import N
import speech_recognition as sr
import cv2
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk 
def animation_view(words):
    #tokenizing the sentence
    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)
    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"])
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
    tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])



    #stopwords that will be removed
    stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])



    #removing stopwords and applying lemmatizing nlp process to words
    lr = WordNetLemmatizer()
    filtered_text = []
    for w,p in zip(words,tagged):
        if w not in stop_words:
            if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
                filtered_text.append(lr.lemmatize(w,pos='v'))
            elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
                filtered_text.append(lr.lemmatize(w,pos='a'))

            else:
                filtered_text.append(lr.lemmatize(w))

    #adding the specific word to specify tense
    words = filtered_text
    temp=[]
    for w in words:
        if w=='I':
            temp.append('Me')
        else:
            temp.append(w)
    words = temp
    probable_tense = max(tense,key=tense.get)

    if probable_tense == "past" and tense["past"]>=1:
        temp = ["Before"]
        temp = temp + words
        words = temp
    elif probable_tense == "future" and tense["future"]>=1:
        if "Will" not in words:
                temp = ["Will"]
                temp = temp + words
                words = temp
        else:
            pass
    else:
        if tense["present_continuous"]>=1:
            temp = ["Now"]
            temp = temp + words
            words = temp
    filtered_text = []
    for w in words:
        path = vds(w)
        if path==False and isnoun(w):
            filtered_text.append(w)
        else:
            filtered_text.append(w)
    return filtered_text
def isnoun(word):
    text = [word]
    ans = nltk.pos_tag(text)
    #print(ans)
    # ans returns a list of tuple
    val = ans[0][1]
    
    # checking if it is a noun or not
    if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
        return True
    else:
        return False
def vds(inps): 
    symb_k=str(inps)
    print(symb_k)
    path="C:\\Users\\irfan\\OneDrive\\Desktop\\project\\AUDIO-SPEECH-TO-SIGN-LANGUAGE-CONVERTER-master\\sign\\"
    pth=path+symb_k+'.mp4'
    print(pth)
    isExist=os.path.exists(pth)
    #pth="C:\\Users\\irfan\\OneDrive\\Desktop\\project\\AUDIO-SPEECH-TO-SIGN-LANGUAGE-CONVERTER-master\\sign\\hello.mp4"

    return isExist
def vid(inps): 
    symb_k=str(inps)
    print(symb_k)
    path="C:\\Users\\irfan\\OneDrive\\Desktop\\project\\AUDIO-SPEECH-TO-SIGN-LANGUAGE-CONVERTER-master\\sign\\"
    pth=path+symb_k+'.mp4'
    print(pth)
    isExist=os.path.exists(pth)
    #pth="C:\\Users\\irfan\\OneDrive\\Desktop\\project\\AUDIO-SPEECH-TO-SIGN-LANGUAGE-CONVERTER-master\\sign\\hello.mp4"

    print(isExist)
    if(isExist):

        #cap=cv2.VideoCapture("C:\\Users\\irfan\\OneDrive\\Desktop\\project\\AUDIO-SPEECH-TO-SIGN-LANGUAGE-CONVERTER-master\\sign\\your.mp4")
        cap=cv2.VideoCapture(pth)
        #print('cpread',cap.read())
        while (cap.isOpened()):
            ret , frame = cap.read()
            if ret==True:
                cv2. imshow('frame',frame)
                if cv2.waitKey(10  ) and 0xFF==ord('q'):
                    break 
            else:
                break
            
        cap.release()
        cv2.destroyAllWindows()
    else:
        return 0
def takecomd():
    # it will take microphone input from user and returns string as an output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")
        except Exception as e :
            print("say that once again")
            takecomd() 
            #speak("sorry! this query not in my range please say it again") 
            return "None"
        return query  
def wrd(text):
    text.lower()
    #nltk.download('punkt')
    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)
    print(words)
    p={'Will','Now','Before'}
    print('keywords are',animation_view(words))
    words=animation_view(words)
    for i in words:
        if(i not in p):
            k=vid(i)
            if(k==0):
                k1=[str(i3) for i3 in i]
                print(k1)
                for i1 in k1:
                    vid(i1)


                 
           

      
if _name_ == "_main_":
            
    text=takecomd() 
    print(text)
        
    wrd(text)   
    print("Successfully Executed")