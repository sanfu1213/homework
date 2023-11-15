

from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>s1114653文宏勝</h1>"
    homepage += "<a href=/profile>個人簡介</a><br>"
    homepage += "<a href=/hollandcodes>何倫碼測驗結果分析</a><br>"
    homepage += "<a href=/jobintroduced>相關工作介紹</a><br>"
    homepage += "<a href=/resume_autobiography>履歷自傳</a><br>"
    return homepage

@app.route("/profile")
def profile():
    
    return render_template("profile.html")
@app.route("/hollandcodes")
def hollandcodes():
    
    return render_template("hollandcodes.html")

@app.route("/jobintroduced")
def jobintroduced():
    
    return render_template("jobintroduced.html")
@app.route("/resume_autobiography")
def resume_autobiography():
    
    return render_template("resume_autobiography.html")












if __name__ == "__main__":
    app.run()