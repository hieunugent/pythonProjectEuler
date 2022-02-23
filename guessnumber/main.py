from flask import Flask
app = Flask(__name__)
# @app.route('/1')
# def one():
#     return '<iframe src="https://giphy.com/embed/ZnZrgIwPaDcnS" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/art-design-3d-ZnZrgIwPaDcnS">via GIPHY</a></p>'
# @app.route('/2')
# def two():
#     return '<iframe src="https://giphy.com/embed/26gsqQxPQXHBiBEUU" width="480" height="320" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/studiosoriginals-numbers-gilphabet-26gsqQxPQXHBiBEUU">via GIPHY</a></p>'
# @app.route('/3')
# def three():
#     return '<iframe src="https://giphy.com/embed/bEV9qjqCnztxWuSXlc" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/clioawards-clio-clios-award-bEV9qjqCnztxWuSXlc">via GIPHY</a></p>'
# @app.route('/4')
# def four():
#     return '<iframe src="https://giphy.com/embed/l3V0vxrOHW5zPfd96" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/typography-type-shurly-l3V0vxrOHW5zPfd96">via GIPHY</a></p>'
# @app.route('/5')
# def five():
#     return '<iframe src="https://giphy.com/embed/LSKVlAGSnuXxVdp5wN" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/loop-minimal-every-day-LSKVlAGSnuXxVdp5wN">via GIPHY</a></p>'
# @app.route('/6')
# def six():
#     return '<iframe src="https://giphy.com/embed/L4NtmZmGB6zwUKPw6R" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/trippy-abstract-pi-slices-L4NtmZmGB6zwUKPw6R">via GIPHY</a></p>'
# @app.route('/7')
# def seven():
#     return '<iframe src="https://giphy.com/embed/l4Ho74sS3cxg5TLLa" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/typography-type-shurly-l4Ho74sS3cxg5TLLa">via GIPHY</a></p>'
# @app.route('/8')
# def eight():
#     return '<iframe src="https://giphy.com/embed/B6bnealXUbW18QjPCd" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/illustration-typography-number-B6bnealXUbW18QjPCd">via GIPHY</a></p>'
# @app.route('/9')
# def nine():
#     return '<iframe src="https://giphy.com/embed/FQpmX52vDfhja" width="400" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animography-animated-typography-font-FQpmX52vDfhja">via GIPHY</a></p>'
import random
random_number = random.randint(0,9)
@app.route('/')
def startnumber():
    return '<iframe src = "https://giphy.com/embed/LnFnoEGtO6DlUYpyzm" width = "480" height = "480" frameBorder = "0" class = "giphy-embed" allowFullScreen> </iframe> <p> <a href="https://giphy.com/gifs/metro-lineas-metromadrid-LnFnoEGtO6DlUYpyzm" > via GIPHY </a> </p>'
@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return "<h1>Too high! Guess again! </h1>"\
            '<iframe src="https://giphy.com/embed/P8jmgo10wMngFsPG2V" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/master-keki-procrastinator-P8jmgo10wMngFsPG2V">via GIPHY</a></p>'
    elif guess < random_number:
        return "<h1>Too low! Guess again!</h1>"\
        '<iframe src="https://giphy.com/embed/DMNqE0oBP2BEY" width="480" height="343" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/420-baked-DMNqE0oBP2BEY">via GIPHY</a></p>'
    else:
        return "<h1>You guessed it!</h1>" \
            '<iframe src="https://giphy.com/embed/ITFQun020grZE5i4Bb" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/accurate-you-are-right-your-ITFQun020grZE5i4Bb">via GIPHY</a></p>'
    


if __name__ == '__main__':
    app.run()
