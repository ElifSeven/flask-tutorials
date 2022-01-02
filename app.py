from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    #return "Anasayfa"
    #return render_template("index.html",number = 10, number2 = 20)
   # message = "Bu ir mesajdır...."
    #return render_template("index.html",message = message)
    numbers = [1,2,3,4,5,6,7]
    return render_template("index.html",numbers = numbers)
@app.route("/search")
def search():
    return "Search Page"

@app.route("/delete/item")
def delete():
    return "Delete Item"

@app.route("/delete/<string:id>")
def deleteId(id):
    return "Id: " + id

@app.route("/toplam",methods=["GET","POST"])
def toplam():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")

        return render_template("number.html",total = int(number1) + int(number2))
    else:
        return redirect(url_for("index")) #sayfada index fonksiyonunu buluyor


if __name__ == "__main__":
    app.run(debug = True)
