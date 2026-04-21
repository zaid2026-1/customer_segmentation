from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load( open("model.pkl","rb") )

segment_map = {
    0: "Premium Customer",
    1: "Standard Customer",
    2: "Budget Customer",
    3.: "Low Budget Customer", 
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        income = int( request.form["income"] )
        spending = int ( request.form["spending"] )
    
        cluster = model.predict([[income, spending]])[0]
        result = segment_map.get(cluster)
    
    return render_template("index.html",result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
