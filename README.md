# ImageProcessing
In my research work, I have encountered a problem to process the images on prehand inorder for the other system to be able to recognize and extract the text from the images. 
The image source for my project is archive;org which contains tiff images which are copyright free material, it would be much difficult if one has to do the same job for better storage and information retrival.

## Proposed Solution
Using AI to address this problem is a way to do it with a minmal training data and with more precsion and accuracy.
### Steps in doing it
We are planning on building a mobile application once after a sucessful backbone, so
1. The document has to be rectified and cropped
2. The background of the images are mostly bright but sometimes brown with black shadows and even sometimes missing edges, of course the first step addresses the last problem.
3. The text in the image has to be of high contrast and the text has to be crisp.
### Prerequisites for the knowledge
Basically there are many and this system is popular in many maybe close sourced commercial applications the idea behind open-sourcing it is to allow future students or researchers to build upon it rather than building it up from scratch.

## Images in our problem
1. Images are mostly rectangular in shape and has a particular dimensions since these were tiff files but has a lot of noises due to several reasons.
# Where are we going to get started?
1. Contrast enhnacement
2. Filtering using convolution
3. Morphological operations
## 1. Contrast Enhancement
Image contrast means spread of pixels over the image. By this particular method we are going to make the a\pictures more vibrant and clear for the other system to extract text. 
I have choosen the following two methods for this purpose
i. Min-Max Stretch
ii.Histogram Equalization (Source: https://docs.opencv.org/master/d4/d1b/tutorial_histogram_equalization.html)
These enhances the contrast in particualr images.

## 2 .Differerent filtering Kernels by Convolution
Different filtering kernels invloved are Box Blur, Gaussian Blur(has sigma), Sobel (in direction of X)(datatype is float, x grad and y grad), Laplacian.
Noise like the dots on paper are approached with the median blur)

## 3. Morphological Operations
Performed on bianry images, works on boundary of images, two basic operations a) Erosion, b) dilation.



