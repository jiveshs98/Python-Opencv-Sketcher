import cv2

# Our sketch generating function

def sketch(image):

    #Convert image into grayscale
    img_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(img_gray)

    # Clean up image using GaussianBlur
    img_gray_blur= cv2.GaussianBlur(img_gray, (5,5), 0)

    # Extract edges
    canny_edges= cv2.Canny(img_gray_blur, 10, 70)

    # Do an invert binarize the image
    ret, mask= cv2.threshold(canny_edges, 40, 225, cv2.THRESH_BINARY_INV)
    return mask


# Initialise webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was successful (ret)
# It also contains the images collected from the webcam (frame)

cap= cv2.VideoCapture(0)
print(cap)

while True:
    ret, frame= cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13:        # 13 is the Enter Key
        break

# Release Camera and close the windows
cap.release()
cv2.destroyAllWindows()
