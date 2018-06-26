import numpy as np
#include 

#todo- populate these arrays
Content_NoLearn_NoTrain_91 = [0.5,
                                                 1,
                                                 0,
                                                 0,
                                                 0,
                                                 0,
                                                 0,
                                                 0,
                                                 1,
                                                 1,
                                                 0,
                                                 0,
                                                 1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]

Content_YesLearn_NoTrain_90 = [1.5,
                                          1,
                                          0,
                                          1.5,
                                          1.5,
                                          1,
                                          0,
                                          0,
                                          1,
                                          0,
                                          0,
                                          0,
                                          0,
                                          0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]

Content_NoLearn_YesTrain_74 = [0,
                                          1,
                                          1,
                                          0.5,
                                          2,
                                          1.5,
                                          0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]

Content_YesLearn_YesTrain_89 = [0.5,
                                         0,
                                         1.5,
                                         0,
                                         1.5,
                                         0,
                                         2,
                                         0,
                                         0,
                                         1,
                                         0,
                                         2,
                                         1,
                                         1,
                                         0.5,
                                         1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
]


#todo-concatenate all arrays
Content_All_344 = Content_NoLearn_NoTrain_91 + Content_YesLearn_NoTrain_90 + Content_NoLearn_YesTrain_74 + Content_YesLearn_YesTrain_89
print np.sum(Content_All_344)

Content_AllYesTrain_163 = Content_NoLearn_YesTrain_74 + Content_YesLearn_YesTrain_89
Content_AllNoTrain_181 = Content_NoLearn_NoTrain_91 + Content_YesLearn_NoTrain_90
print "Train", "Yes: ", np.sum(Content_AllYesTrain_163), "No: ", np.sum(Content_AllNoTrain_181)

Content_AllYesLearn_179 = Content_YesLearn_NoTrain_90 + Content_YesLearn_YesTrain_89
Content_AllNoLearn_165 = Content_NoLearn_NoTrain_91 + Content_NoLearn_YesTrain_74
print "Learn", "Yes: ", np.sum(Content_AllYesLearn_179), "No: ", np.sum(Content_AllNoLearn_165)

######
print "****Sum******"
print np.sum(Content_NoLearn_NoTrain_91), np.sum(Content_YesLearn_NoTrain_90)
print np.sum(Content_NoLearn_YesTrain_74), np.sum(Content_YesLearn_YesTrain_89)

print "Train"
print np.sum(Content_AllNoTrain_181)
print np.sum(Content_AllYesTrain_163)

print "Learn"
print np.sum(Content_AllNoLearn_165)
print np.sum(Content_AllYesLearn_179)

print "All"
print np.sum(Content_All_344)

#####
print "******Mean*****"
print round(np.mean(Content_NoLearn_NoTrain_91), 2), round(np.mean(Content_YesLearn_NoTrain_90), 2)
print round(np.mean(Content_NoLearn_YesTrain_74), 2), round(np.mean(Content_YesLearn_YesTrain_89), 2)

print "Train"
print round(np.mean(Content_AllNoTrain_181), 2)
print round(np.mean(Content_AllYesTrain_163), 2)

print "Learn"
print round(np.mean(Content_AllNoLearn_165), 2)
print round(np.mean(Content_AllYesLearn_179), 2)

print "All"
print round(np.mean(Content_All_344), 2)
######
print "****p-values*****"
p_val_Content = 0
p_val_Content_train = 0
p_val_Content_learn = 0
p_val_Content_interaction = 0
#########################################################################
for i in range(10000):		
  np.random.shuffle(Content_All_344) #randomize all_array

  if np.sum(Content_All_344[255:343]) > np.sum(Content_YesLearn_YesTrain_89): #check if the value is greater than the origiinal value
    p_val_Content = p_val_Content + 1

#Check 2  - Effect of train -- does train improve 
  if (np.sum(Content_All_344[181:254]) + np.sum(Content_All_344[255:328])) > (np.sum(Content_NoLearn_YesTrain_74) + np.sum(Content_YesLearn_YesTrain_89[0:73]) ) :#taking 74 elements for all
    p_val_Content_train = p_val_Content_train + 1

#Check 3 - effect of learn
  #if (np.sum(Content_All_344[91:179]) + np.sum(Content_All_344[255:343])) > (np.sum(Content_YesLearn_NoTrain_90[0:88]) + np.sum(Content_YesLearn_YesTrain_89) ) :#taking 89 elements for all 
  if (np.sum(Content_All_344[91:179]) + np.sum(Content_All_344[255:343])) > (np.sum(Content_YesLearn_NoTrain_90[0:88]) + np.sum(Content_YesLearn_YesTrain_89) ) :#taking 89 elements for all 
    p_val_Content_learn = p_val_Content_learn + 1

#Check 4  - Interaction effects
  if np.sum(Content_All_344[91:180]) + np.sum(Content_All_344[181:254]) + np.sum(Content_All_344[255:343]) > np.sum(Content_YesLearn_NoTrain_90) + np.sum(Content_NoLearn_YesTrain_74) + np.sum(Content_YesLearn_YesTrain_89) :     
  #this below is worth cosnidering
  #if (np.sum(Content_All_344[181:254]) - np.sum(Content_All_344[0:73])) + (np.sum(Content_All_344[91:180]) - np.sum(Content_All_344[0:89])) > (np.sum(Content_All_344[255:343]) - np.sum(Content_All_344[0:88])): #take 74 and 90 and 89
    p_val_Content_interaction = p_val_Content_interaction + 1 

print "p_val_Content:   ", p_val_Content

print "p_val_Content_train:   ", p_val_Content_train
print (np.sum(Content_NoLearn_YesTrain_74) + np.sum(Content_YesLearn_YesTrain_89) )

print "p_val_Content_learn:   ", p_val_Content_learn
print (np.sum(Content_YesLearn_NoTrain_90) + np.sum(Content_YesLearn_YesTrain_89) )

print "p_val_Content_interaction:   ", p_val_Content_interaction
