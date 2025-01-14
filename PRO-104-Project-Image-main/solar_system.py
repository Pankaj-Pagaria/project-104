import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(
    img, 
    "Sun",
    (20,300),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Mercury",
    (120,190),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Venus",
    (192,172),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Earth",
    (295,170),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Mars",
    (385,175),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Jupiter",
    (565,55),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Saturn",
    (750,120),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Uranus",
    (970,140),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.putText(
    img, 
    "Neptune",
    (1120,145),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=0.5,
    color=(255,255,255)
)
cv2.imshow('output',img)
cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.waitKey(0)