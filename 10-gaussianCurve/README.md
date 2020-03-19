Welcome @Challenger's to the 10th #code4bytes challenge!
Because 10 is such a special number, we decided on making this a special one.
```
We set up a api that returns 100 values sampled from a gaussian distribution.
Your task is the find the μ (mean) and σ (standard deviation (square root of variance)) of this distribution.
A good statistician knows that calculating those metrics using only 100 samples won't accurately represent the true distribution, so collect enough data.
Each distribution created by the api is stored using a 4-16 long alphanumeric key, this key will be used to validate your submission so don't lose it!
Everytime you call the api, a new set of 100 values returns from the same distribution of the same key.

You call the api like this: 
curl -X GET http://codingweb.eu-central-1.elasticbeanstalk.com/yourstring
curl -X GET http://codingweb.eu-central-1.elasticbeanstalk.com/petergriffin
curl -X GET http://codingweb.eu-central-1.elasticbeanstalk.com/123456789
```
Try to come up with an original string as each distribution is limited to 2 requests per second, so watch out for 429 responses!


Example:
curl -X GET http://codingweb.eu-central-1.elasticbeanstalk.com/golang
 
Solution:
μ: 20.608640196774772
σ: 22.210112678759003

Submit the results to your own string, not the results of /golang!

- 1st place: 5000 bytes!
- 2nd place: 4000 bytes!
- 3rd place: 3500 bytes!
- Runner up: 2500 bytes!

Extra challenge:
- If you write your solution in a language that is not Python, you get 1000 bytes extra!
- If you do everything manually (curl by hand, plug it into your graphing calculator, and calculate it that way) you get 5000 bytes extra!

Extra info:
- Please ask your questions in #coding-general and NOT in DM's!
- If you don't know what any of this is, don't complain! Wikipedia can help you out!
