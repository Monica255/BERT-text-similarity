import numpy as np
import nltk
nltk.download('punkt')
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string

def sentence_split(paragraph):
    return nltk.sent_tokenize(paragraph)

def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res

def sentence_weight(data,wordfreq):
    weights = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        weights.append(temp)
    return weights

news = """
"Berbagai manfaat cabe untuk kesehatan:
1. Penghilang rasa sakit
Pelepasan endorfin yang dirangsang oleh cabe dapat berperan sebagai penghilang rasa sakit alami. Selain itu, endorfin juga dapat membuat seseorang menjadi ketergantungan. Berikut ini rasa sakit yang mampu diredakan oleh cabe adalah herpes zoster, bursitis, neuropati diabetes dan kejang otot pada bahu, serta penyakit rematik. Capsaicin pada cabe bekerja sama dengan reseptor rasa sakit, adanya sensasi rasa panas mampu membuat ujung saraf berhenti mengirim sinyal sensasi rasa sakit.

2. Penurun berat badan
Capsaicin dipercaya mampu mengurangi asupan kalori. Penelitian menunjukkan 10 gram cabe merah mampu meningkatkan pembakaran lemak pada perempuan dan laki-laki. Memang tidak semua penelitian menemukan cara ini efektif, bahkan ada yang menemukan bahwa cara ini tidak bekerja sama sekali.

3. Detoksifikasi
Cabe bisa membantu detoksifikasi gastrointestinal dalam mencerna makanan, dan membuang zat-zat yang tidak terpakai oleh tubuh. Selain itu juga mampu meningkatkan pasokan nutrisi ke dalam jaringan tubuh.

4. Kesehatan kardiovaskular
Cabe rawit mampu mengurangi kolestrol dalam darah dan level trigliserida. Penelitian yang dikutip oleh WHFood (The World’s Healthiest Foods) menunjukkan bahwa 27 partisipan yang terdiri dari 14 perempuan dan 13 laki-laki), memakan potongan cabe selama 4 minggu, dibagi menjadi dua grup, grup yang satu diet dengan mengkonsumsi cabe, yang satu lagi tidak melibatkan cabe. Hasilnya terbukti grup yang memakan cabe, level kolestrol dan trigliseridanya lebih rendah baik pada laki-laki maupun pada perempuan.

5. Mencegah bisul pada lambung
Orang-orang berasumsi bahwa memakan cabe dapat menimbulkan bisul pada lambung, namun ternyata cabe membantu membunuh bakteri yang kemungkinan tertelan oleh Anda dan memberikan stimulasi sel-sel yang melapisi lambung untuk mengeluarkan zat-zat yang melindungi lambung.

6. Mencegah penyakit jantung
Kandungan vitamin B6 dan asam folat yang terdapat pada cabe, serta potassium dan beta karoten, Anda dapat terhindar dari serangan jantung. Vitamin B juga dapat dapat mengurangi level homocysteine; tingginya level homocysteine dapat merusak pembuluh darah dan meningkatkan risiko stroke dan serangan jantung.

7. Mencegah risiko kanker usus besar
Vitamin C sangat berpenagruh dalam peningkatan imun tubuh. Cartonoid lycopene, beta karoten dan asam folat pada cabe merah mampu mengurangi risiko kanker usus besar. Asam folat sangat berguna untuk metabolisme tubuh yang sehat.

8. Melancarkan pernapasan
Cabe dapat membantu melebarkan saluran napas di paru-paru, sehingga dapat mengurangi asma. Vitamin A pada cabe dapat mengurangi radang paru-paru akibat merokok, sebab asap rokok mengandung benzopyreneyang menghancurkan vitamin A dalam tubuh.
"
"""

def preprocess_text(text):
    # Remove question words in Indonesian
    question_words = ['bagaimana', 'apa', 'dimana', 'siapa', 'kapan', 'berapa', 'mengapa','itu']
    text = ' '.join(word for word in text.split() if word.lower() not in question_words)

    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # stemming process
    text   = stemmer.stem(text)

    # case folding
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans("","",string.punctuation))

    # remove white space
    text = text.strip()

    return text

def sum(text):
    data = sentence_split(text)
    wordfreq = word_freq(data)
    rank = sentence_weight(data,wordfreq)
    # print("aa",text)
    n = 2
    result = ''
    sort_list = np.argsort(rank)[::-1][:n]
    for i in range(n):
        result += '{} '.format(data[sort_list[i]])

    print(result)
    return result

# sum(news)