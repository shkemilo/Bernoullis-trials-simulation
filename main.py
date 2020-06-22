from random import random
from math import comb
import matplotlib.pyplot as plt

def populateExperiments(n, p):
  temp = []
  for i in range(n):
    temp.append(simulateExperiment(p))
  return temp
    
def simulateExperiment(p):
  if random() <= p:
      return 1
  return 0

def successProbability(n, k, p):
	return comb(n, k) * pow(p, k) * pow(1 - p, n - k)

def numberOfSuccesses(experiment):
	count = 0
	for i in experiment:
		if(i == 1):
			count += 1

	return count

print("Enter Number of Sets of Experiments: ")
N = int(input())

print("Enter Number of Experiments: ")
n = int(input())

print("Enter Probability of Expermient Success: ")
p = float(input())
if (p < 0 or p > 1):
	print("Probability must element of [0, 1]")
	exit()

experiments = [];
for i in range(N):
	experiments.append(populateExperiments(n, p))

print("Results of experiments: ")
for i in range(N):
	print(experiments[i])

successes = [0 for x in range(n + 1)]
for i in range(N):
	ind = numberOfSuccesses(experiments[i])
	successes[ind] = round(successes[ind] + 1.0 / N, 4)

print("Output: ")
print(successes)

theorethicalSuccesses = []
for k in range(n + 1):
	theorethicalSuccesses.append(round(successProbability(n, k, p), 4))

print("Theoretically correct output: ")
print(theorethicalSuccesses)

print("Generate histograms?(y/n)")
choice = input()
if(choice != "y"):
	exit()

fig, (ax1, ax2) = plt.subplots(2)
fig.subplots_adjust(hspace = .5)
fig.suptitle("Bernoulli trials p = " + str(p) + " n = " + str(n), fontsize = 12)

ax1.set(xlabel = "Number of successes", ylabel = "Probability")
ax1.hist(range(n + 1), weights = successes, bins = n + 1, label = "Output (N = " + str(N) + ")", ec = "black")
ax1.legend()

ax2.set(xlabel = "Number of successes", ylabel = "Probability")
ax2.hist(range(n + 1), weights = theorethicalSuccesses, bins = n + 1, label = "Theorethical Output", ec = "black", color = "red")
ax2.legend()

plt.savefig("results.pdf")
plt.savefig("results.png")
plt.show()