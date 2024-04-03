from flask import Flask, render_template

app=Flask(__name__)

if __name__ == '__main__':    
    app.run(port=5000,debug=True)

@app.route('/')
def home():    
    return render_template("<pizza>Hello world!</pizza>")



