from art import logoHL
imp

def resultfun(win, score):
    prompt=""
    resultstring=""
    if not win:
        prompt = "Sorry your are lose."
        resultstring = " Final score " + str(score)
    else:
        prompt = "Your are right. "    
        resultstring = " Current score "+ str(score)
    print(prompt + resultstring)


print(logoHL)
resultfun(True, 8)
