import sys
from pkl_utils import save_obj, load_obj
import numpy as np

# Argument 1: Reduced dimensions
# Argument 2: Train (0) or Val(1)
dim_red=int(sys.argv[1])
sys2=int(sys.argv[2])

if not sys2:
	DATA_DIR='../Models/VW_Train/'
	matrix_sizes=[long(size) for size in open(DATA_DIR+'shape_info.txt','r').read().splitlines()]
	# final reduced matrix
	visual_words_reduced=np.zeros((matrix_sizes[8],dim_red))
	num_files=range(1,9)
else:
	DATA_DIR='../Models/VW_Val/'
	matrix_sizes=[long(size) for size in open(DATA_DIR+'shape_info.txt','r').read().splitlines()]
	# final reduced matrix
	visual_words_reduced=np.zeros((matrix_sizes[0],dim_red))
	num_files=range(1,2)

# loading precomputed pca
pca=load_obj('../Models/PCAlayer_128.pkl')

done_till_now=0

# load matrices separately and reduce them
for i in num_files:
	print "Loading visual_words_" + str(i)
	visual_words=np.load(DATA_DIR+'visual_words_'+str(i)+'.npy')
	visual_words_reduced[done_till_now:done_till_now+matrix_sizes[i-1],:]=pca.transform(visual_words)
	done_till_now+=matrix_sizes[i-1]

print "Saving the complete reduced matrix"
np.save(DATA_DIR+'visual_words_reduced.npy',visual_words_reduced)