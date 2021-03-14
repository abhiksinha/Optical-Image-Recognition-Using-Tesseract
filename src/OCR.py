import cv2
import numpy as np
import pytesseract

## Simple yet powerfull OCR code which converts most of the image text to ASCII data.


## Loading the image in GrayScale
img=cv2.imread('test.jpg',0)


######## 

def imagetotext2(img):

    
    ### Resizing the image by scale factor (2,2). You can play with these numbers to get the better results.
    ### Resizing the image is most important as tesseract requires proper spacing and quality image.
    ### Bi-Cubic interpolation works better in this scenario, you can play with other method such as INTER_LANCZOS4 or INTER_NEAREST etc.
    
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    ### Applying more filters to the image, you can comment this out if not getting better Results.  
    img= cv2.medianBlur(img, 3)
 
                          
    ## path where the tesseract module is installed 
    pytesseract.pytesseract.tesseract_cmd =r'Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = r'--tessdata-dir "Tesseract-OCR\tessdata"'
    
    
    ## Converts the image to text 
    ## Using Pre-Trained DataSet. You can use other data set or train your own.  
    result = pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config) 
    
    return result




print('working')
data= imagetotext2(img)
print(data)
