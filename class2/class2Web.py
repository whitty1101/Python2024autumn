from flask import Flask

app=Flask(__name__, static_folder="static", static_url_path="/abc")#建立app便是為FLASK物件，__NAME__表示目前執行的程式

@app.route("/")#使用函式裝飾氣，建立一個路由 *ROUTES，可針對主網域/發出請求
def index():#發出請求後會執行*HOME的函示
    return "welcome"#56行函示後會回傳特定的網頁內容，以HTML格式以方便瀏覽器來做網頁的展示
@app.route("/member/<name>")
def sayhi(name):
    return"hello"+name
@app.route("/admin/<level>")
def login(level):
    if level=="A":
        return"login here"
    else:
        return"you cant login here"

app.run()#執行