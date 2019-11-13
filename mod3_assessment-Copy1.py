#!/usr/bin/env python
# coding: utf-8

# # Module 3 Assessment

# Welcome to your Mod 3 Assessment. You will be tested for your understanding of concepts and ability to solve problems that have been covered in class and in the curriculum.
# 
# Use any libraries you want to solve the problems in the assessment.
# 
# You will have up to **two hours** to complete this assessment.
# 
# The sections of the assessment are:
# - Combinatorics, Probability and Discrete Distributions
# - Statistical Distributions
# - Statistical Tests
# - Bayesian Statistics
# 
# 

# In[1]:


# import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

# import any additional libraries needed.


# ## Part 1: Combinatorics, Probability & Discrete Distributions
# 
# ### a. Set Theory
# 
# Given the following event probabilities:
# 
# $P(A) = 0.7$
# 
# $P(B) = 0.5$
# 
# $P(B|A) = 0.4$
# 
# Calculate the following probabilities and assign to the variables `ans1` and `ans2` in the next cell:
# 
# 1. $P(A and B)$
# 
# 2. $P(A|B)$
# 
# Hint: draw a diagram!
# 

# In[2]:


#your answer here
ans1 = None
ans2 = None


# ### b. Card Combinatorics
# 
# You have a standard deck of 52 cards.
# 
# 1. What is the probability of drawing a king or a queen? (`ans1`)
# 2. How many possible 5-card combinations can be formed with this deck of 52 cards? (`ans2`)
# 

# In[3]:


#your answer here
ans3 = None
ans4 = None


# ### c. Discrete Probability Distributions
# 
# In a game with the same deck of 52 cards, you draw a card $n$ times with replacement. You win a point by drawing a face card (king, queen or jack). 
# 
# The function ```probability_of_scoring``` is provided below.  In this function $k$ is the number of points won in the game, $n$ is the number of draws, and $p$ is the probability of winning a point.  The function returns the corresponding probability.

# In[4]:


def probability_of_scoring_k(n, p, k):
    """
    n = number of draws
    p = probability of winning a point
    k = number of points scored
    
    Use np.factorial()
    
    """
    # defining a helper function for factorial
    
    def fact(n):
        return np.math.factorial(n)
    
    
    return (fact(n)/(fact(k)*fact(n-k)))*(p**(k))*((1-p)**(n-k))


# 1. Using this function, what is the probability of winning 8 points out of 22 draws?
# 

# In[5]:


#your answer here
ans5 = None


# 2a. Use the function `probability_of_scoring` to calculate the probability of drawing $k$ points out of 22 draws.<br> _Hint_: Your final result should be in the form of a list or array.

# In[6]:


#your answer here
k_values = None
probs = None


# 2b. Plot the results of 2a. to create the probability mass function.
# 

# In[7]:


# Your code here


# 3. Based on the probability mass function, what type of distribution does the `probability_of_scoring` have? Save your answer as a string to the variable `dist_type`.

# In[2]:


# Your answer written here
dist_type = None


# ## Part 2: Statistical Distributions

# ### a. Descriptive Statistics
# 
# We have a sample of $10,000$ checks from a TexMex restaurant that has saved all their check receipts since openning.<br> We have the sample in the file ```check_data```.

# 1.  Compute the descriptive statistics of check totals and set it equal to the `desc_check_total` variable.

# In[9]:


data = pd.read_csv('data/check_data.csv')
# Your answer here
desc_check_total = None


# 2. What do the measures of central tendency (mean and median) indicate about the distribution of the check totals?

# In[10]:


# Your written response here:
"""

"""


# ### b. Continuous Distributions
# 
# 1. Create a histogram to visually depict the distribution of check totals.

# In[11]:


# Your code here


#  

# 
# For the following questions, you may use a [z-table](https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf).
# 
# 2. Calculate the 95% confidence interval around the mean check total as a **tuple** and set it to the variable `conf`. In a separate cell, interpret this interval correctly. 

# In[12]:


# Your code here
mean = 0
zscore = None
std = None
conf = (None, None)
print("The 95% confidence interval is {} with a mean of {}".format(conf,round(mean,2)))


# In[13]:


# Your written interpretation of the confidence interval:
"""

"""


# 3. Using a z-test and an $\alpha = 0.05$, is my $23 dollar check significantly **greater** than the mean in our sample? 
# - Set the `ztest_results` variable to the results of the ztest function.
# - Set your decision to the `significant` variable. 
# - Then, in a separate cell, elaborate on how you know this.

# In[14]:


# Your code here
ztest_results = None
significant = None # Set this to True or False


# In[15]:


# Your written response here:
"""

"""


# 4. Say we don't know how our population of checks is distributed. How does **sampling** and the **Central Limit Theorem** allow us to **make inferences on the population mean**, i.e. estimate $\mu, \sigma$ of the population mean?

# In[16]:


# Your written response here:
"""

"""


# ## Part 3: Statistical Testing

# ### a. Hypotheses and Errors
# 
# This TexMex restaurant recently added queso to its menu.<br>The restaurant owners hope that customers ordering queso will end up spending a significantly different amount than non-queso-orders.<br> Let the average amount on queso customers' checks be $X_{Q}$.
# 
# 1. Set up the null and alternative hypotheses for this test.

# $H_{0}:$ `hypothesis here`
# 
# $H_{A}:$ `hypothesis here`

# 2. In this context, what does it mean to make `Type I` and `Type II` errors?

# In[17]:


# Your written response here:
"""

"""


# With $\alpha = 0.05$, we want to determine if checks which included queso are significantly more **or** less than those that did not include queso. Below are histograms of the distribution of check totals split by orders that included queso and those that did not.  You may assume they have equal variances.

# In[18]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

np.random.seed(43)
no_queso = np.random.choice(data.check_total, 1000)
ax1.set_title('Sample of Non-Queso Check Totals')
ax1.set_xlabel('Amount')
ax1.set_ylabel('Frequency')
ax1.hist(no_queso, bins=20)

queso = pickle.load(open("data/queso.pkl", "rb"))
ax2.set_title('Sample of Queso Check Totals')
ax2.set_xlabel('Amount')
ax2.set_ylabel('Frequency')
ax2.hist(queso, bins=20)
# # # plt.show()


# 3. Run a statistical test on the two samples to determine if you should reject or fail to reject the null hypothesis above. 
# - Set the `queso_results` variable to the return of the ttest function.

# In[19]:


# Your code here
queso_results = None


# 4.  According to the results of the statistical test above
# - Set the `reject` variable to your decision 
# - In a separate cell, explain why you made that decision regarding your null hypothesis.

# In[1]:


reject = None # Set this to True or False


# In[1]:


# Your written response regarding the null hypothesis:
"""

"""


# 5. What are the conditions required to perform the test you chose?

# In[21]:


# Your written response here:
"""

"""


# ## Part 4: Bayesian Statistics
# ### a. Bayes' Theorem

# #### Scenario
# Thomas wants to get a new puppy 🐕 🐶 🐩 
# 
# 
# <img src="https://media.giphy.com/media/rD8R00QOKwfxC/giphy.gif" />
# 
# He can choose to get his new puppy either from the **pet store** or the **pound**.<br> 
# The probability of him going to the _pet store_ is $0.2$. 
# 
# He can choose to get either a **big**, **medium** or **small** puppy.
# 
# If he goes to the _pet store_:
# - the probability of him getting a small puppy is $0.6$ 
# - the probability of him getting a medium puppy is $0.3$
# - the probability of him getting a large puppy is $0.1$
# 
# If he goes to the _pound_: 
# - the probability of him getting a small puppy is $0.1$
# - the probability of him getting a medium puppy is $0.35$
# - the probability of him getting a large puppy is $0.55$
# 
# 
# #### Questions
# 1. What is the probability of Thomas getting a small puppy? (`ans1`)
# 2. Given that he got a large puppy, what is the probability that Thomas went to the pet store? (`ans2`)
# 3. Given that Thomas got a small puppy, is it more likely that he went to the pet store or to the pound? (`ans3`)
# 4. In question 2, what is the prior(`ans4_prior`), posterior(`ans4_posterior`) and likelihood(`ans4_likelihood`)?

# In[22]:


ans6 = None
ans7 = None
ans8 = "answer here"
ans9_prior = "answer here"
ans9_posterior = "answer here"
ans9_likelihood = "answer here"

