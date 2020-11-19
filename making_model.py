import pandas as pd
import dill as pickle

def clean_text(text):
    return text.lower()

#save function as pickle
# pickle preprocessing function
model_save_path = "clean_me.pkl"
with open(model_save_path,'wb') as file:
    pickle.dump(clean_text,file)

if __name__ == '__main__':
    #test function
    data = pd.read_csv('Tweetid,_Originaltex_1605092859311.csv')
    print(clean_text(data['text'][0]))