from flask import Flask, jsonify, request
from classifier import  get_prediction
import cv2
import numpy as np

app = Flask(__name__)



if __name__ == "__main__":
  app.run(debug=True)
