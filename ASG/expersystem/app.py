from flask import Flask, render_template ,request, jsonify
from flask_cors import CORS
from expert import Base



app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/getPaths' , methods=['POST'])
def pathretrival():

    data = request.get_json()
    src = data.get("src")
    des = data.get("des")
    consider = data.get("con")

    res = Base.callingruls(src , des , consider , True)
    #print(res)  
    print(res["path"] ," " , res["cost"] ," ",  res["time"])

    returningpaths = res["path"]
    cost = res["cost"]
    time = res["time"]
    leng = len(returningpaths)
    named = []
    for i in range(leng):
        weIn = returningpaths[i]
        if(weIn == "A"):
            named.append("Sri Lanka")
        elif(weIn == "B"):
            named.append("China")
        elif(weIn == "C"):
            named.append("Australia")
        elif(weIn == "D"):
            named.append("Africa")
        elif(weIn == "E"):
            named.append("Amarica")
        elif(weIn == "F"):
            named.append("Arab")
        elif(weIn == "G"):
            named.append("France")
        elif(weIn == "H"):
            named.append("England")
        elif(weIn == "I"):
            named.append("Italy")
        
    print(named)
    return jsonify({"paths":named , "cost":cost , "time":time})
  




@app.route('/alterpaths' , methods=['POST'])
def alterpathretrival():

    data = request.get_json()
    src = data.get("src")
    des = data.get("des")
    consider = data.get("con")
    print("got")
    res = Base.callingruls(src , des , consider , False)
    #print(res)  
    #print(res["path"] ," " , res["cost"] ," ",  res["time"])

    #returningpaths = res["path"]
    #cost = res["cost"]
    #time = res["time"]
    leng = len(res)
    finanlizedSubPaths = []
    for i in range(leng):
        subpath = list(res[i])
        cost = subpath[1]
        time = subpath[2]
        subpathlen = len(subpath[0])
        named = []
        for j in range(subpathlen):

            weIn = subpath[0][j]
            if(weIn == "A"):
                named.append("Sri Lanka")
            elif(weIn == "B"):
                named.append("China")
            elif(weIn == "C"):
                named.append("Australia")
            elif(weIn == "D"):
                named.append("Africa")
            elif(weIn == "E"):
                named.append("Amarica")
            elif(weIn == "F"):
                named.append("Arab")
            elif(weIn == "G"):
                named.append("France")
            elif(weIn == "H"):
                named.append("England")
            elif(weIn == "I"):
                named.append("Italy")
        finalsubpath = [named , cost , time]
        finanlizedSubPaths.append(finalsubpath)
    print(finanlizedSubPaths)
    """
    #return jsonify({"paths":named , "cost":cost , "time":time})"""
    return  jsonify({"paths":finanlizedSubPaths})
  







if __name__ == '__main__':
    app.run(debug=True)
