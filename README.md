#   **OpenCV Overview**
I Learn it from [freeCodeCamp - YouTube](https://www.youtube.com/watch?v=oXlwWbU8l2o&t=2653s)
##  **Image Transformation**
### **Translation Image (2x3)**  
Define the Function flow with these steps:  
1. Define transmetrix like the next code:
    ```transmetric = np.float32([[1,0,x],[0,1,y]])```

    <pre lang="markdown"> Translation Matrix (2x3):  
    [ 1 0 X ] --> 1: keep x as-is, 0: no rotation, X: shift along x-axis 
    [ 0 1 Y ] --> 0: no rotation, 1: keep y as-is, Y: shift along y-axis  
    -X --> Left, not Right  
    -Y --> Up not Down  </pre>

2. select Dimentions `dimansions = (img.shape[1], img.shape[0])`  
3. apply `warpAffine()`function 
    ```python
    def translate(img,x,y):
    transmetric = np.float32([[1,0,x],[0,1,y]])
    dimansions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmetric, dimansions)

### **Rotation Image**

Flow of Function:
1. select hight and wedth of image `(h, w) = img.shape[:2]` and check value of rotpoint if **None** Replace it with medile point of image.
2. apply rotation matrix for 2D `rotMetric = cv.getRotationMatrix2D(rotPoint, angle, 1.0)` last Parameter for Scaling to image.
3. Select dimensions, then apply `warpAffine()`.
    ```python
    def rotate(img, angle, rotPoint=None):
        (h, w) = img.shape[:2]
        if rotpoint is None:
            rotpoint = (w // 2, h // 2)
        rotMetric = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimansions = (w, h)
        return cv.warpAffine(img, rotMetric, dimansions)
    ```
### **Resize Image**

```python
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
```
`interpolation` values are:
 1. `INTER_CUBIC` or `INTER_LINEAR` for **Zooming in (Upscale)**  
 2. `INTER_AREA` for **Zooming out**
 3. `INTER_NEAREST` for **Fast + Simple**

 ### **Flip Image**  
Using `flip()`:
```python
flipped = cv.flip(img, 1)  # 0 for vertical, 1 for horizontal, -1 for both
```

### **Crop Image**
Using slicing:
```python
cropped = img[50:200, 200:400]  # y1:y2, x1:x2
```


## **Contour Image**
Contours are curves or boundaries that connect continuous points along the same color or intensity.
They are often used to detect shapes, objects, and boundaries in images.  
### **Steps to Apply Contour:**
1. Apply Gray Filter using `cvtColor(img, cv.COLOR_BGR2GRAY)`
2. Apply Blur (optional) using `GaussianBlur()` or Use Threshold, then Continue from step 4.
3. Detect Edges with Canny `Canny()`
4. Find Contours `findContours()`:  
    - **Second Parameter (mode):**  
    `cv.RETR_LIST` for Retrieves all contours, but no hierarchical relationships are stored.  
    `cv.RETR_EXTERNAL` for Retrieves only outermost contours. Ignores child contours.
    `cv.RETR_CCOMP` for Retrieves all contours and organizes them into a 2-level hierarchy: outer and inner.   
    `cv.RETR_TREE` for Retrieves all contours and reconstructs a full hierarchy tree (parent-child relationship).

    - **Third Parameter (method):**  
    `cv.CHAIN_APPROX_NONE`: Stores all points along the contour. Very detailed, uses more memory.  
    `cv.CHAIN_APPROX_SIMPLE`: Compresses contours by removing redundant points (e.g., straight lines).  
    `cv.CHAIN_APPROX_TC89_L1`: Applies the Teh-Chin chain approximation algorithm (faster, advanced).  
    `cv.CHAIN_APPROX_TC89_KCOS`: Another variant of the Teh-Chin approximation.



5. Draw Contours `drawContours()`

    ```python
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    canny = cv.Canny(blur, 125, 175)
    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 1)
    cv.imshow('Contours', img)
    ```


##  **Color Spaces & Channels**  
It's Easy to understand it, search about it what's benefits, and look at it from [here - Spaces](color_space.py)  & [here - Channels](color_channels.py).

##  **Smoothing**
Smoothing is a technique used to reduce noise and make an image look cleaner and softer by averaging pixel values. 
 
Types of Smoothing Filter:  
- `Average`: Computes the mean of neighboring pixels; simple, fast, but blurs edges and fine details.  
- `Gaussian`: Applies a weighted average using a Gaussian kernel, smooths naturally, but still blurs edges.  
- `Median`: Replaces each pixel with the median of its neighbors; great for salt-and-pepper noise, keeps edges.  
- `Bilateral`: Combines spatial and intensity info to smooth while preserving edges; effective but slow.  

## **BITWISE Operations & Masking**

`AND`: Return the intersection between two objects.  
`OR`: Return Union between two objects.  
`XOP`: Return non-intersection Region.  
`NOT`: invert white to black & black to white.  
Follow [Masking](masking.py) to know more.

## **Computing Histograms**
From [Here](computing_histograms.py)


