import numpy as np
#include 

#todo- populate these arrays
Overall_NoLearn_NoTrain_91 = [1,
5,
3,
1,
0,
4.5,
0,
0,
3,
2,
1.5,
2,
2.5,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
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

Overall_YesLearn_NoTrain_90 = [4,
1,
1,
4.5,
5,
4,
2,
0,
3,
2,
1,
2,
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
0,
0,
0,
0
]

Overall_NoLearn_YesTrain_74 = [4,
6,
3,
3,
5,
3.5,
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
0
]

Overall_YesLearn_YesTrain_89 = [1.5,
0,
6.5,
2,
7.5,
1,
4,
3,
1,
3,
2,
4,
4,
4,
3.5,
3,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
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

Overall_All_344 = Overall_NoLearn_NoTrain_91 + Overall_YesLearn_NoTrain_90 + Overall_NoLearn_YesTrain_74 + Overall_YesLearn_YesTrain_89

Overall_AllYesTrain_163 = Overall_NoLearn_YesTrain_74 + Overall_YesLearn_YesTrain_89
Overall_AllNoTrain_181 = Overall_NoLearn_NoTrain_91 + Overall_YesLearn_NoTrain_90

Overall_AllYesLearn_179 = Overall_YesLearn_NoTrain_90 + Overall_YesLearn_YesTrain_89
Overall_AllNoLearn_165 = Overall_NoLearn_NoTrain_91 + Overall_NoLearn_YesTrain_74

######
print "*******Sum******"
print np.sum(Overall_NoLearn_NoTrain_91), np.sum(Overall_YesLearn_NoTrain_90)
print np.sum(Overall_NoLearn_YesTrain_74), np.sum(Overall_YesLearn_YesTrain_89)

print "Train"
print np.sum(Overall_AllNoTrain_181)
print np.sum(Overall_AllYesTrain_163)

print "Learn"
print np.sum(Overall_AllNoLearn_165)
print np.sum(Overall_AllYesLearn_179)

print "All"
print np.sum(Overall_All_344)
#####
print "******Mean******"
print round(np.mean(Overall_NoLearn_NoTrain_91), 2), round(np.mean(Overall_YesLearn_NoTrain_90), 2)
print round(np.mean(Overall_NoLearn_YesTrain_74), 2), round(np.mean(Overall_YesLearn_YesTrain_89), 2)

print "Train"
print round(np.mean(Overall_AllNoTrain_181), 2)
print round(np.mean(Overall_AllYesTrain_163), 2)

print "Learn"
print round(np.mean(Overall_AllNoLearn_165), 2)
print round(np.mean(Overall_AllYesLearn_179), 2)

print "All"
print round(np.mean(Overall_All_344), 2)
######
print "****p-values*****"
p_val_overall = 0
p_val_overall_train = 0
p_val_overall_learn = 0
p_val_overall_interaction = 0

#########################################################################
for i in range(10000):		
	np.random.shuffle(Overall_All_344) #randomize all_array
	if np.sum(Overall_All_344)!=133.5:
		print "sum not correct" #check, this should be 25.5+31.5+26.5+50 = 133.5

#CHECK 1 - This is just to see if there's a difference
	if np.sum(Overall_All_344[255:343]) > np.sum(Overall_YesLearn_YesTrain_89): #check if the value is greater than the original value
	#if np.sum(Overall_All_344[255:328]) > np.sum(Overall_YesLearn_YesTrain_89[0:74]): #take74
	#if np.sum(Overall_All_344[255:343]) > np.sum(Overall_All_344[0:90]):
	#if np.sum(Overall_All_344[255:343]) > np.sum(Overall_All_344[0:88]):
	#if np.sum(Overall_All_344[255:343]) - np.sum(Overall_All_344[0:88]) > 24.5:
		p_val_overall = p_val_overall + 1

#Check 2  - Effect of train -- does train improve 
	#if (np.sum(Overall_All_344[181:254]) + np.sum(Overall_All_344[255:343])) > (np.sum(Overall_NoLearn_YesTrain_74) + np.sum(Overall_YesLearn_YesTrain_89) ) : 
	if (np.sum(Overall_All_344[181:254]) + np.sum(Overall_All_344[255:328])) > (np.sum(Overall_NoLearn_YesTrain_74) + np.sum(Overall_YesLearn_YesTrain_89[0:73]) ) : #taking 74 elements for all	
		p_val_overall_train = p_val_overall_train + 1

#Check 3  - Effect of learn -- does learn improve 
	#if (np.sum(Overall_All_344[91:180]) + np.sum(Overall_All_344[255:343])) > (np.sum(Overall_YesLearn_NoTrain_90) + np.sum(Overall_YesLearn_YesTrain_89) ) : 
	if (np.sum(Overall_All_344[91:179]) + np.sum(Overall_All_344[255:343])) > (np.sum(Overall_YesLearn_NoTrain_90[0:88]) + np.sum(Overall_YesLearn_YesTrain_89) ) : #taking 89 elements for all	
		p_val_overall_learn = p_val_overall_learn + 1	

#Check 4  - Interaction effects
	#if (np.sum(Overall_All_344[91:180]) + np.sum(Overall_All_344[181:254]) > (np.sum(Overall_YesLearn_NoTrain_90) + np.sum(Overall_NoLearn_YesTrain_74))) : 	 	
	#if np.sum(Overall_All_344[91:180]) + np.sum(Overall_All_344[181:254]) + np.sum(Overall_All_344[255:343]) > np.sum(Overall_YesLearn_NoTrain_90) + np.sum(Overall_NoLearn_YesTrain_74) + np.sum(Overall_YesLearn_YesTrain_89) : 	 	
	#if np.sum(Overall_All_344[91:180]) + np.sum(Overall_All_344[181:254]) + np.sum(Overall_All_344[255:343]) > np.sum(Overall_YesLearn_NoTrain_90) + np.sum(Overall_NoLearn_YesTrain_74) + np.sum(Overall_YesLearn_YesTrain_89) :


	#if (26.5 - 25.5) + (31.5 - 25.5) > (50 - 25.5):
	#if (np.sum(Overall_All_344[181:254]) - np.sum(Overall_All_344[0:90])) + (np.sum(Overall_All_344[91:180]) - np.sum(Overall_All_344[0:90])) > 24.5:
	#if (np.sum(Overall_All_344[181:254]) - np.sum(Overall_All_344[0:73])) + (np.sum(Overall_All_344[91:180]) - np.sum(Overall_All_344[0:89])) > 24.5: #take 74 and 90
	#if (np.sum(Overall_All_344[181:254]) - np.sum(Overall_All_344[0:90])) + (np.sum(Overall_All_344[91:180]) - np.sum(Overall_All_344[0:90])) > (np.sum(Overall_All_344[255:343]) - np.sum(Overall_All_344[0:90])):
	#if (np.sum(Overall_All_344[181:254]) - np.sum(Overall_All_344[0:73])) + (np.sum(Overall_All_344[91:180]) - np.sum(Overall_All_344[0:89])) > (np.sum(Overall_All_344[255:343]) - np.sum(Overall_All_344[0:88])): #take 74 and 90 and 89
	if (np.sum(Overall_All_344[181:254]) - np.sum(Overall_All_344[0:73])) + (np.sum(Overall_All_344[91:180]) - np.sum(Overall_All_344[0:89])) > (np.sum(Overall_All_344[255:343]) - np.sum(Overall_All_344[0:88])): #take 74 and 90 and 89
	#if (np.sum(Overall_All_344[255:343]) - np.sum(Overall_All_344[0:88])) - (np.sum(Overall_All_344[181:254]) - np.sum(Overall_All_344[0:73])) + (np.sum(Overall_All_344[91:180]) - np.sum(Overall_All_344[0:89])) > (50-25.5) - ((26.5-25.5) + (31.5-25.5)): #take 74 and 90 and 89
		p_val_overall_interaction = p_val_overall_interaction + 1

print "p_val_overall:   ", p_val_overall
#print out the fraction -- this is the p-value
print "p_val_overall_train:   ", p_val_overall_train
print (np.sum(Overall_NoLearn_YesTrain_74) + np.sum(Overall_YesLearn_YesTrain_89) )

print "p_val_overall_learn:   ", p_val_overall_learn
print (np.sum(Overall_YesLearn_NoTrain_90) + np.sum(Overall_YesLearn_YesTrain_89) )

print "p_val_overall_interaction:   ", p_val_overall_interaction
#print np.sum(Overall_YesLearn_NoTrain_90) + np.sum(Overall_NoLearn_YesTrain_74)




