## FAQ : detectMultiscale()

### These are the values which are usually given to detectMultiScale(...) as parameters.

- **scaleFactor** : Parameter specifying how much the image size is reduced at each image scale.

  Basically the scale factor is used to create your scale pyramid. More explanation can be found here. In short, as described [here](https://sites.google.com/site/5kk73gpu2012/assignment/viola-jones-face-detection#TOC-Image-Pyramid), your model has a fixed size defined during training, which is visible in the xml. This means that this size of face is detected in the image if present. However, by rescaling the input image, you can resize a larger face to a smaller one, making it detectable by the algorithm.

  **1.05** is a good possible value for this, which means you use a small step for resizing, i.e. reduce size by 5%, you increase the chance of a matching size with the model for detection is found. This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection, with the risk of missing some faces altogether.

* **minNeighbors**: Parameter specifying how many neighbors each candidate rectangle should have to retain it.

  This parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality. **3~6** is a good value for it.

* **minSize** : Minimum possible object size. Objects smaller than that are ignored.

  This parameter determine how small size you want to detect. You decide it! Usually, **[30, 30]** is a good start for face detection.

* **maxSize** : Maximum possible object size. Objects bigger than this are ignored.

  This parameter determine how big size you want to detect. Again, you decide it! **Usually, you don't need to set it manually,** the default value assumes you want to detect without an upper limit on the size of the face.

---

###### The explanation was given in [this](https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters) stackoverflow question.
