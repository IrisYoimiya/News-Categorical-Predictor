from flask import Flask, render_template, request
import pickle, string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


stop_words = set(stopwords.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()
tambahan = {'saya', 'dia', 'itu', 'dan', 'ke', 'di'}
stop_words.update(tambahan)

def process_text(text):
    list_words = word_tokenize(str(text).lower())  # pastikan tipe string
    list_words = [word for word in list_words if word not in stop_words]
    list_words = [word for word in list_words if word not in string.punctuation]
    list_words = [word for word in list_words if word.isalpha()]
    # list_words = [stemmer.stem(word) for word in list_words]
    return ' '.join(list_words)

app = Flask(__name__)
model_rf = pickle.load(open('model_rf.pickle', 'rb'))
count_vectorizer =  pickle.load(open('count_vectorizer.pickle', 'rb'))
tfidf_transformer = pickle.load(open('tfidf_transformer.pickle', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    title = request.form['title']  # Ambil data dari form
    clean_title = process_text(title)
    counts = count_vectorizer.transform([clean_title])
    X = tfidf_transformer.transform(counts)
    prediction = model_rf.predict(X)
    
    return render_template('index.html', prediction=prediction[0], original=title)

if __name__ == '__main__':
    app.run(debug=True)