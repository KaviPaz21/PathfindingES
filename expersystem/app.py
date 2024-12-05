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

    res = Base.callingruls(src , des , consider , True , False)
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
    res = Base.callingruls(src , des , consider , False , False)
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
  







@app.route('/explain_Path' , methods=['POST'])
def plathexplainer():

    data = request.get_json()
    src = data.get("src")
    des = data.get("des")
    consider = data.get("con")
    #print("gotex" , src , " " , des)
    res , w = Base.callingruls(src , des , consider , False , True)
     
    #print(res["path"] ," " , res["cost"] ," ",  res["time"])

    #returningpaths = res["path"]
    #cost = res["cost"]
    #time = res["time"]
    #[f"<h3>Explain the traversal from <u>{}</u> to <u></u></h3>"]
    
    print(res) 
    finanlizedSubPaths = []
    for i in range(len(res)):
        subpath = res[i]
        cost = subpath[2]
        time = subpath[3]
        print(i)
        named = []
        for j in range(2):
            
            
            weIn = subpath[j]
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
        if i==0:
            if consider =="0":
                take ="Minimum Cost"
            elif consider =="1":
                take ="Minimum Time"
            else:
                take = "Optimal"
                

            text= f"<h2>Explanation for Optimal Path</h2>"
            finanlizedSubPaths.append(text)
            text= f"<div>Initially we are at <b>{named[0]}</b> and we need to determine the nearest possible node considering {take}. </div><div>Then repeating this Procedure  untill we reach to the destination. </div> <div>So that, </div>"
            finanlizedSubPaths.append(text)
            text=    f"<div>Step 0{i+1} :First We are at {named[0]} and we go for {named[1]}. for that we have to pay {res[i][2]} $ and {res[i][3]} Days. after ending this traversal <b>totally</b> we have to pay <b>{res[i][4]} $</b> and <b>{res[i][5]} Days.</b></div>"
            finanlizedSubPaths.append(text)

        elif i==len(res)-1:
            text=    f"<div>Step 0{i+1} :Finally, We are at {named[0]} and we go for {named[1]} which is our destination. for that we have to pay {res[i][2]} $ and {res[i][3]} Days. after ending this traversal <b>totally</b> we have to pay <b>{res[i][4]} $</b> and <b>{res[i][5]} Days.</b></div>"

            finanlizedSubPaths.append(text)

            text=    f"<br/><div className='text-red-500'>At the end of this route as a summary We have to pay <b>totally</b> we have to pay <b>{res[i][4]} $</b> and <b>{res[i][5]} Days.</b></div>"
            
            finanlizedSubPaths.append(text)

            if(consider == "2"):
                weight = f"<b>weight for the optimal path is {w}</b>"
                finanlizedSubPaths.append(weight)
        else:
            text=    f"<div>Step 0{i+1} :Then, New Starting is {named[0]} and we go for {named[1]}. for that we have to pay {res[i][2]} $ and {res[i][3]} Days. after ending this traversal <b>totally</b> we have to pay <b>{res[i][4]} $</b> and <b>{res[i][5]} Days.</b></div>"
            finanlizedSubPaths.append(text)
    print(finanlizedSubPaths)
    """
    #return jsonify({"paths":named , "cost":cost , "time":time})"""
    return  jsonify({"paths":finanlizedSubPaths})






if __name__ == '__main__':
    app.run(debug=True)
