import numpy as np
#include 

#todo- populate these arrays
Creativity_NoLearn_NoTrain_91 = [0.5,
                                                    0,
                                                    0,
                                                    0,
                                                    0,
                                                    0.5,
                                                    0,
                                                    0,
                                                    1,
                                                    1,
                                                    0.5,
                                                    0,
                                                    0.5,
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

Creativity_YesLearn_NoTrain_90 = [0.5,
                                             0,
                                             0,
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
                                             0.5,
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

Creativity_NoLearn_YesTrain_74 = [0,
                                             1,
                                             0,
                                             0.5,
                                             1,
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
0
]

Creativity_YesLearn_YesTrain_89 = [0,
                                            0,
                                            2,
                                            0,
                                            2,
                                            0,
                                            0,
                                            1,
                                            0,
                                            0,
                                            0,
                                            0,
                                            1,
                                            1,
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
Creativity_All_344 = Creativity_NoLearn_NoTrain_91 + Creativity_YesLearn_NoTrain_90 + Creativity_NoLearn_YesTrain_74 + Creativity_YesLearn_YesTrain_89
print np.sum(Creativity_All_344)

Creativity_AllYesTrain_163 = Creativity_NoLearn_YesTrain_74 + Creativity_YesLearn_YesTrain_89
Creativity_AllNoTrain_181 = Creativity_NoLearn_NoTrain_91 + Creativity_YesLearn_NoTrain_90

Creativity_AllYesLearn_179 = Creativity_YesLearn_NoTrain_90 + Creativity_YesLearn_YesTrain_89
Creativity_AllNoLearn_165 = Creativity_NoLearn_NoTrain_91 + Creativity_NoLearn_YesTrain_74

######
print "****Sum******"
print np.sum(Creativity_NoLearn_NoTrain_91), np.sum(Creativity_YesLearn_NoTrain_90)
print np.sum(Creativity_NoLearn_YesTrain_74), np.sum(Creativity_YesLearn_YesTrain_89)

print "Train"
print np.sum(Creativity_AllNoTrain_181)
print np.sum(Creativity_AllYesTrain_163)

print "Learn"
print np.sum(Creativity_AllNoLearn_165)
print np.sum(Creativity_AllYesLearn_179)

print "All"
print np.sum(Creativity_All_344)

#####
print "******Mean*****"
print round(np.mean(Creativity_NoLearn_NoTrain_91), 2), round(np.mean(Creativity_YesLearn_NoTrain_90), 2)
print round(np.mean(Creativity_NoLearn_YesTrain_74), 2), round(np.mean(Creativity_YesLearn_YesTrain_89), 2)

print "Train"
print round(np.mean(Creativity_AllNoTrain_181), 2)
print round(np.mean(Creativity_AllYesTrain_163), 2)

print "Learn"
print round(np.mean(Creativity_AllNoLearn_165), 2)
print round(np.mean(Creativity_AllYesLearn_179), 2)

print "All"
print round(np.mean(Creativity_All_344), 2)
######
print "****p-values*****"
p_val_Creativity = 0
p_val_Creativity_train = 0
p_val_Creativity_learn = 0
p_val_Creativity_interaction = 0

#########################################################################
for i in range(10000):
  np.random.shuffle(Creativity_All_344) #randomize all_array

#CHECK 1 - This is just to see if there's a difference
  if np.sum(Creativity_All_344[255:343]) + 1 > np.sum(Creativity_YesLearn_YesTrain_89): #check if the value is greater than the origiinal value
    p_val_Creativity = p_val_Creativity + 1

#Check 2  - Effect of train -- does train improve 
  if (np.sum(Creativity_All_344[181:254]) + np.sum(Creativity_All_344[255:328])) > (np.sum(Creativity_NoLearn_YesTrain_74) + np.sum(Creativity_YesLearn_YesTrain_89[0:73]) ) : #taking 74 elements for all
    p_val_Creativity_train = p_val_Creativity_train + 1

#Check 3  - Effect of learn -- does train improve 
  if (np.sum(Creativity_All_344[91:179]) + np.sum(Creativity_All_344[255:343])) > (np.sum(Creativity_YesLearn_NoTrain_90[0:88]) + np.sum(Creativity_YesLearn_YesTrain_89) ) :#taking 89 elements for all
    p_val_Creativity_learn = p_val_Creativity_learn + 1

#Check 4  - Interaction -- does learn improve 
  if np.sum(Creativity_All_344[91:180]) + np.sum(Creativity_All_344[181:254]) + np.sum(Creativity_All_344[255:343]) > np.sum(Creativity_YesLearn_NoTrain_90) + np.sum(Creativity_NoLearn_YesTrain_74) + np.sum(Creativity_YesLearn_YesTrain_89) :     
    p_val_Creativity_interaction = p_val_Creativity_interaction + 1   

print "p_val_Creativity:   ", p_val_Creativity
#print out the fraction -- this is the p-value
print "p_val_Creativity_train:   ", p_val_Creativity_train
print "p_val_Creativity_learn:   ", p_val_Creativity_learn
print "p_val_Creativity_interaction:   ", p_val_Creativity_interaction


