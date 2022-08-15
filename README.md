# Retail Products Self Checkout System
Machine Learning/Deep Learning
# 1.Business Problem
### 1.1 Problem Description
A self checkout store aims to provide customers with a satisfying experience, prevent time loss, and eliminate long lines and lengthy checkout times by implementing a system that streamlines the shopping experience and keeps track of each customer's choices and preferences without requiring the customer to do anything. Customers can enter a store, browse, and leave without having to stand in line or self-check out at the entrance thanks to self checkout technology in the retail industry. Particularly in the supermarket industry, a new era in retail has begun. Retail Products Self Checkout System is an AI-based approach for grocery superstores which allows customers to conveniently walk in, purchase their products and simply walk out of the stores. Customers need not to wait for long queues for billing or wait for manually self scanning to get the billing done which greatly improves customer happiness and boosts sales.
### 1.2  Features in the Dataset
Dataset have three files train images, train annotations, same type for both test and validation.
Source:-https://www.kaggle.com/datasets/diyer22/retail-product-checkout-dataset</pre>
## 1.3 Source
<pre>
<li> https://www.kaggle.com/datasets/diyer22/retail-product-checkout-dataset </li>
<li> https://github.com/jacobgil/pytorch-grad-cam </li>
<li> https://www.analyticsvidhya.com/blog/2021/12/how-to-use-yolo-v5-object-detection-algorithm-for-custom-object-detection-an-example-use-case/ </li>
<li> https://subscription.packtpub.com/book/data/9781838827069/7/ch07lvl1sec34/overview-of-faster-r-cnn </li>
<li> https://cocoa.ethz.ch/downloads/2017/05/2316\_final\_submission.pdf </li>
</pre>
## 1.4 Bussnies Objective and Constraints:-
<pre>
<li> The goal is to fix the problem. When a customer puts his/her products on the checkout counter.</li>
<li> Negligible amount of errors. </li>
<li> There are latency limitations. </li>
</pre>

### 1.5 Performance metric:-
<pre>
<li> Checkout Accuracy(cAcc). </li>
<li> Average Counting Distance(ACD). </li>
<li> Mean Category Counting Distance(mCCD). </li>
<li> Mean Category Intersection of Union(mCIoU). </li>
</pre>


### Model:-
## 2.1 Yolo-V5:-
YOLO (You Only Look Once) models are used for Object
detection with high performance. They can be used for realtime object detection based on the data streams. YOLO divides
an image into a grid system, and each grid detects objects
within itself.
The General Object Detector will have a head to forecast
classes and bounding boxes and a backbone for pre-training.
Platforms with a GPU or a CPU can run backbones. Head
can be either a one-stage (YOLO, SSD, RetinaNet, etc.) or a
two-stage (Sparse prediction) model.

## 2.2  Faster RCNN:-
we employ an object detection model based on the Faster
RCNN architecture. Modern object detection techniques are
implemented by the open source system Detectron2-[15].
Based on the PyTorch framework, it was created. The feature
extractor is Resnet-101, and the model is built on a Faster
RCNN architecture. We can initialize our model with weights
from an object detector.
We pretrained weights in the detectron2 model zoo before
starting the training. It takes about 4 hours to train this on
the RPC dataset for 10000 iterations.

## 2.3 Mask-RCNN:-
Mask R-CNN was built using Faster R-CNN. While Faster
R-CNN has 2 outputs for each candidate object, a class label
and a bounding-box offset, Mask R-CNN is the addition of
a third branch that outputs the object mask. The additional
mask output is distinct from the class and box outputs,
requiring the extraction of a much finer spatial layout of an
object.
The essential component of Fast/Faster R-CNN that is lacking
from Mask R-CNN is the pixel-to-pixel alignment. The same
two-step method, with an identical first stage, is used by Mask
R-CNN (which is RPN). In the second stage, Mask R-CNN
additionally produces a binary mask for each RoI in addition
to class and box offset predictions. In contrast, the majority
of current systems rely on mask predictions for categorization.

