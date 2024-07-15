import tensorflow as tf
from nn_functions import fetch_data, tokenize
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

# Tokenizer ayarlama
tokenizer = Tokenizer(num_words=70, oov_token="<oov>", split=' ')
data, vocab_size, input_len = fetch_data(tokenizer)

# Veriyi ve etiketleri ayırma
data_input = data[:, :5]
data_output = data[:, 5:]
# Etiketleri one-hot encoding ile dönüştürme
data_output = to_categorical(data_output, num_classes=3)
data_output = data_output.astype(int)
# Veri bölme
input_train, input_val, output_train, output_val = train_test_split(
    data_input, data_output, test_size=0.3, random_state=28
)
# Model mimarisini tanımlama
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=5, input_length=5),
    LSTM(6, return_sequences=True),
    LSTM(6),
    Dense(10, activation='relu'),
    Dense(10, activation='relu'),
    Dense(10, activation='relu'),
    Dense(10, activation='relu'),
    Dense(3, activation='softmax')  # Çok sınıflı sınıflandırma için softmax kullanıyoruz
])

# Modeli derleme
model.compile(optimizer=tf.keras.optimizers.Adam(
    learning_rate=0.01, epsilon=0.00001, use_ema=True, ema_momentum=0.8), loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy']
)

# Model özetini yazdırma
model.summary()

# Modeli eğitme
model.fit(input_train, output_train, epochs=60, validation_data=(input_val, output_val))

model.save('./model/model.keras')
print(model.layers[4].get_weights())

# Yeni metni tokenizasyon
new_text = ["kapıları kapat"]
tokenized_data = tokenize(tokenizer, new_text)
print(model.predict(tokenized_data))

