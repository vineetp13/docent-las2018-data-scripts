import numpy as np
#include 

#todo- populate these arrays
Str_NoLearn_NoTrain_91 = [0,
                                             4,
                                             3,
                                             1,
                                             0,
                                             4,
                                             0,
                                             0,
                                             1,
                                             0,
                                             1,
                                             2,
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

Str_YesLearn_NoTrain_90 = [2,
                                      0,
                                      1,
                                      2,
                                      3,
                                      2,
                                      2,
                                      0,
                                      2,
                                      2,
                                      1,
                                      2,
                                      1,
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

Str_NoLearn_YesTrain_74 = [4,
                                      4,
                                      2,
                                      2,
                                      2,
                                      2,
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

Str_YesLearn_YesTrain_89 = [1,
                                     0,
                                     3,
                                     2,
                                     4,
                                     1,
                                     2,
                                     2,
                                     1,
                                     2,
                                     2,
                                     2,
                                     2,
                                     2,
                                     2,
                                     2,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
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
Str_All_344 = Str_NoLearn_NoTrain_91 + Str_YesLearn_NoTrain_90 + Str_NoLearn_YesTrain_74 + Str_YesLearn_YesTrain_89
print np.sum(Str_All_344)

Str_AllYesTrain_163 = Str_NoLearn_YesTrain_74 + Str_YesLearn_YesTrain_89
Str_AllNoTrain_181 = Str_NoLearn_NoTrain_91 + Str_YesLearn_NoTrain_90
print "Train", "Yes: ", np.sum(Str_AllYesTrain_163), "No: ", np.sum(Str_AllNoTrain_181)

Str_AllYesLearn_179 = Str_YesLearn_NoTrain_90 + Str_YesLearn_YesTrain_89
Str_AllNoLearn_165 = Str_NoLearn_NoTrain_91 + Str_NoLearn_YesTrain_74
print "Learn", "Yes: ", np.sum(Str_AllYesLearn_179), "No: ", np.sum(Str_AllNoLearn_165)
print ""

######
print "****Sum******"
print np.sum(Str_NoLearn_NoTrain_91), np.sum(Str_YesLearn_NoTrain_90)
print np.sum(Str_NoLearn_YesTrain_74), np.sum(Str_YesLearn_YesTrain_89)

print "Train"
print np.sum(Str_AllNoTrain_181)
print np.sum(Str_AllYesTrain_163)

print "Learn"
print np.sum(Str_AllNoLearn_165)
print np.sum(Str_AllYesLearn_179)

print "All"
print np.sum(Str_All_344)

#####
print "******Mean*****"
print round(np.mean(Str_NoLearn_NoTrain_91), 2), round(np.mean(Str_YesLearn_NoTrain_90), 2)
print round(np.mean(Str_NoLearn_YesTrain_74), 2), round(np.mean(Str_YesLearn_YesTrain_89), 2)

print "Train"
print round(np.mean(Str_AllNoTrain_181), 2)
print round(np.mean(Str_AllYesTrain_163), 2)

print "Learn"
print round(np.mean(Str_AllNoLearn_165), 2)
print round(np.mean(Str_AllYesLearn_179), 2)

print "All"
print round(np.mean(Str_All_344), 2)
######
print "****p-values*****"
p_val_Str = 0
p_val_Str_train = 0
p_val_Str_learn = 0
p_val_Str_interaction = 0
#########################################################################
for i in range(10000):
  np.random.shuffle(Str_All_344)

#CHECK 0 - not doing  
  #if np.sum(Str_All_344)!=?????:
   # print "sum not correct" #check, this should be 25.5+31.5+26.5+50 = 133.5

#CHECK 1 - This is just to see if there's a difference
  #if np.sum(Overall_All_344[255:343]) > np.sum(Overall_YesLearn_YesTrain_89): #check if the value is greater than the original   
  if np.sum(Str_All_344[255:343]) > np.sum(Str_YesLearn_YesTrain_89): #check if the value is greater than the origiinal value:
    p_val_Str = p_val_Str + 1

#IMP -- THESE CHECKS MIGHT NOT BE CORRECT -- SEE OVERALL SCRIPT -- I HAVENT FIXED THIS COS CHECK 1 DOES NOT YIELD SIGNIFICANCE
    #Check 2  - Effect of train -- does train improve 
  if (np.sum(Str_All_344[181:254]) + np.sum(Str_All_344[255:343])) > (np.sum(Str_NoLearn_YesTrain_74) + np.sum(Str_YesLearn_YesTrain_89) ) :    
    p_val_Str_train = p_val_Str_train + 1
    
    #Check 3  - Effect of learn -- does learn improve 
  if (np.sum(Str_All_344[91:180]) + np.sum(Str_All_344[255:343])) > (np.sum(Str_YesLearn_NoTrain_90) + np.sum(Str_YesLearn_YesTrain_89) ) : 
    #print "larger"
    p_val_Str_learn = p_val_Str_learn + 1

    #Check 4  - Interaction -- does learn improve 
  if np.sum(Str_All_344[91:180]) + np.sum(Str_All_344[181:254]) + np.sum(Str_All_344[255:343]) > np.sum(Str_YesLearn_NoTrain_90) + np.sum(Str_NoLearn_YesTrain_74) + np.sum(Str_YesLearn_YesTrain_89) : 
    #print "larger"
    p_val_Str_interaction = p_val_Str_interaction + 1

print "p_val_Str:   ", p_val_Str
#print out the fraction -- this is the p-value
print "p_val_Str_train:   ", p_val_Str_train
print (np.sum(Str_NoLearn_YesTrain_74) + np.sum(Str_YesLearn_YesTrain_89) )

print "p_val_Str_learn:   ", p_val_Str_learn
print (np.sum(Str_YesLearn_NoTrain_90) + np.sum(Str_YesLearn_YesTrain_89) )

print "p_val_Str_interaction:   ", p_val_Str_interaction
print np.sum(Str_YesLearn_NoTrain_90) + np.sum(Str_NoLearn_YesTrain_74)


