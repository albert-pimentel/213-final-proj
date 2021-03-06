<h2> HIT Design (3): </h2>
The HIT will display two profiles. Profile 1 will remain constant and can be thought of as the
person trying to be matched. Profile 2 will change. A Worker will be required to rate on a scale
of 1 to 10 how good of a match Profile 2 is to Profile 1 based on various characteristics such as
ethnicity, sexual orientation, body type, etc. One HIT will consist of ten different profiles rated
for Profile 1.

<h2> Publish Hit/Collect Results (1): </h2>
Once published, we expect the results to come in very rapidly given the simplicity of the task.

<h2> Quality Control (2): </h2>
We will use two methods of quality control. The first is to have three different Workers
complete each profile rating in order to obtain a majority vote. To avoid people randomly
clicking a rating, we will throw out any result that pairs a person with the incorrect gender given
their sexual orientation. For example, it is common sense that a gay man would not match well
with a woman. Any result that rates such a matching highly will be discarded. We will include in
the HIT instructions that for situations such as this, the Worker should select a rating of 1.

<h2> Final Aggregation (1): </h2>
Once we have discarded the bad data, we will collect our final set of matchings in a csv file. This cleaned data set is our gold standard. That is, we assume that the most capable entity
for matchmaking is other humans. We will use this data as a test to see how well our algorithm
is able to match people.

<h2> Building the Algorithm (4): </h2>
We will use the K-Means algorithm to create our model. K-Means partitions data entries into
clusters, whose entries are similar to each other. This means that in either case, we are simply
using similarity to match people. This will allow us to match a person with k other individuals
who are a likely match.

<h2> Training the Algorithm (2): </h2>
We utilize the OkCupid data set to train our model. It consists of about 60,000 profiles that
describe characteristics such as sex, diet, level of education, etc. The algorithm will group the
most similar profiles together which will be how matches are determined.

<h2> Testing the Algorithm (1): </h2>
Utilizing the gold standard data that we crowdsourced from earlier, we will see how well our
algorithm does matching people together. The goal is that it would suggest the same matches
that a human would.

<h2> Creating an Interface (1): </h2>
We will build a platform that implements our algorithm and allows real users to find their k best
matches. The testing group will be other students in NETS 213.

<h2> Publish Interface (1): </h2>
Students from NETS 213 will use our project to find their best matches. We will collect feedback
to see how real time users felt about their matches so that we can make further improvements.
