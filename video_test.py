# =============================================================================
# ####################### IMPORT THE LIBRARIES NECESSARY ######################
# =============================================================================

import cv2
from keras.preprocessing import image
import keras
import numpy as np


# =============================================================================
# ####################### LOAD THE MODEL TO RUN ###############################
# =============================================================================

model_file = "MODELS/Optimised_20_2_19.h5"
classifier = keras.models.load_model(model_file)
if classifier is not None:
    print('model is loaded from ', model_file)
    

# =============================================================================
# ######################## USE THE WEBCAM ON THE LAPTOP #######################
# =============================================================================
    
cap = cv2.VideoCapture(0)

while(1):

# =============================================================================
# ######################## GET THE FRAME FROM WEBCAM ##########################
# =============================================================================

    hasFrame, frame = cap.read()
    if not hasFrame:
        break
    

# =============================================================================
# ######################## RESIZE THE FRAME AND SAVE ##########################
# =============================================================================
    
    h,w,bpp = np.shape(frame)
    dim = (int(w/4), int(h/4))
    frame_2 = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite("frame.jpg", frame_2)
    

# =============================================================================
# ################## READ THE FRAME AND PUT INTO CLASSIFIER ###################
# =============================================================================
    
    test_frame = image.load_img('frame.jpg', target_size = (60,40))
    test_frame = image.img_to_array(test_frame)
    test_frame = np.expand_dims(test_frame, axis = 0)
    result = classifier.predict(test_frame)
    

# =============================================================================
# ####################### GET PREDICITION OF THE FRAME ########################
# =============================================================================
    
    if result[0][0] == 1:
        prediction = 'good'
        text_colour = (0,255,0)
    else:
        prediction = 'bad'
        text_colour = (0,0,255)
#        
#    print(prediction)
#    prediction = 'test'

    cv2.putText(frame, prediction, (5,80),cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale = 3, color = text_colour,thickness = 3)
    
   
# =============================================================================
# ############################# SHOW FRAMES (VIDEO) ###########################
# =============================================================================
    
    cv2.imshow('Video', frame)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
