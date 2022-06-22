import numpy as np

def p_vector(n):
    """
    creates a probability vector 'p_vector' of size 'n'
    """
    v = np.random.randint(0,100,n)
    v_prob = np.ones(n)
    
    for index,i in enumerate(v):
        v_prob[index] = i/ np.sum(v)       
    return v_prob

example1 = p_vector(5)
print('this is the p_vector:', example1)
print('this is its row sum:', sum(example1))



def t_matrix(n):
    """
    creates a transition matrix 't_mat' of size 'n x n'
    where each row is summed to 1
    """
    i=0
    t_mat = []
    
    while i < n:
        t_mat.append(p_vector(n))
        i+=1
        
    return np.array(t_mat)

example2 = t_matrix(5)
print('this is the t_matrix:', example2)
print('and these are the row sums:')
for i in range(5):
    print(sum(example2[i]))



def nth_state(n,t_mat,p_vec):
    """
    computes the 'n'th state of probability vector 'p_vec' using 
    transition matrix 't_mat'
    """
    t_mat_power = np.linalg.matrix_power(t_mat, n) 
    result = t_mat_power.dot(p_vec)
  
    return result    

example3 = nth_state(20, example2, example1)
print('this is the nth state of p_vec on t_mat after n iterations:', example3)



def eigen_matrix(t_mat, N):
    """
    computes eigvenvector of 't_mat' to the power of 'N'
    """

    t_mat_transp = np.linalg.matrix_power(t_mat, N).T
    eigenvals, eigenvects = np.linalg.eig(t_mat_transp)
    return eigenvects

example4 = eigen_matrix(example2, 30)
print('this is the eigen matrix:', example4)



# This is as far as I got.
# I didn't have time to finish this task :(