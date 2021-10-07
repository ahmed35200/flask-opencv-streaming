#!/usr/bin/env python
from flask import Flask, render_template, Response
import io
import cv2
import urllib.request

app = Flask(__name__)
vc = cv2.VideoCapture(-1)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def dhash(image, hashSize=8):
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hashSize + 1, hashSize))

	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]

	# convert the difference image to a hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])



@app.route('/video_feed')
def video_feed():
    return "dsf"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
