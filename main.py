from keras.models import load_model
import tensorflowjs as tfjs

model = load_model("models/model.h5")

tfjs.converters.save_keras_model(model, "static/tfjs_model")