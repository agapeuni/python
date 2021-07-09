# 텐서플로 라이브러리를 임포트
import tensorflow as tf

# MNIST 데이터셋을 로드하여 준비
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# tf.keras.Sequential 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델훈련
model.fit(x_train, y_train, epochs=5)

# 모델평가
model.evaluate(x_test,  y_test, verbose=2)
