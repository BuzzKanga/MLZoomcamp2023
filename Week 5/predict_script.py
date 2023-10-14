import pickle

if __name__ == "__main__":
    with open('model1.bin', 'rb') as f_in:
        model = pickle.load(f_in)

    with open('dv.bin', 'rb') as f_in:
        dv = pickle.load(f_in)


    customer = {
        "job": "retired", 
        "duration": 445, 
        "poutcome": "success"
    }

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
        
    print('Credit score for customer:', y_pred.round(3))
   