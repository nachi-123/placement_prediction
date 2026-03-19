from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import os
import webbrowser
application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    

    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            ssc_p=float(request.form.get('ssc_p')),
            ssc_b=request.form.get('ssc_b'),
            hsc_p=float(request.form.get('hsc_p')),
            hsc_b=request.form.get('hsc_b'),
            hsc_s=request.form.get('hsc_s'),
            degree_p=float(request.form.get('degree_p')),
            degree_t=request.form.get('degree_t'),
            workex=request.form.get('workex'),
            etest_p=float(request.form.get('etest_p')),
            specialisation=request.form.get('specialisation'),
            mba_p=float(request.form.get('mba_p'))

        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])



if __name__=="__main__":
    url = "http://127.0.0.1:5000/predictdata"
    
    print("🚀 Starting server...")
    if os.environ.get("RUNNING_IN_DOCKER") != "1":
        webbrowser.open(url)   
    
    app.run(host="0.0.0.0", port=5000, debug=True)


