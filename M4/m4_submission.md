<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Venkata Sai Pragna Garisa (vg473)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 3:56:56 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/vg473" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221622554-c2b6221b-ccc5-4a84-9b00-c820f1b7cbd0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>addition() : addition method have two variables num1 and num2, if condition checks<br>num1 value, whether it is &#39;ans&#39; or not, if num1==&#39;ans&#39;, it returns ans<br>and num2 as variables  if num1 is not &#39;ans&#39; ,it takes run<br>time values as num1 and num2   num1 = self._as_number(num1) ,_as_number function<br>checks  and read as int or float , later  num1 +<br>num2 value stores in ans and then returns the value ans  ans<br>which is defined in class will update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221623339-8e2b85b5-c5d7-4482-a733-5fdca59692fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of addition function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221624129-3840a26a-b09a-4feb-b0ad-ad75f7c059f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>subtraction : subtraction method have two variables num1 and num2. If condition checks<br>num1 value, whether it is &#39;ans&#39; or not, if num1==&#39;ans&#39;,it returns ans and<br>num2 as variables  ,if num1 is not &#39;ans&#39; ,it takes run time<br>values as num1 and num2  .num1 = self._as_number(num1) ,_as_number function checks <br>and read as int or float , later  num1 - num2 value<br>stores in ans and then returns the value ans  .ans which is<br>defined in class will update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221624807-58d32976-f6c5-4956-8578-aab53f4aa249.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of subtraction function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221627888-c6abb68d-ca1e-4c45-914f-730a267e5cf4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>multiplication : multiplication method have two variables num1 and num2.   If<br>condition checks num1 value, whether it is &#39;ans&#39; or not, if num1==&#39;ans&#39;,it returns<br>ans and num2 as variables   if num1 is not &#39;ans&#39; ,it<br>takes run time values as num1 and num2     num1<br>= self._as_number(num1) ,_as_number function checks  and read as int or float ,<br>later  num1 * num2 value stores in ans and then returns the<br>value ans  ans which is defined in class will update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221628332-6f2a2840-3641-4583-9a85-5477aa0f645b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of multiplication function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221628878-c2f6f38f-57f5-4c6f-875b-38ccc0e57537.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>division : division method have two variables num1 and num2.  If condition<br>checks num1 value, whether it is &#39;ans&#39; or not, if num1==&#39;ans&#39;,it  <br> returns ans and num2 as variables   if num1 is not<br>&#39;ans&#39; ,it takes run time values as num1 and num2   <br>num1 = self._as_number(num1) ,_as_number function checks  and read as int or float<br>, later  another if condition checkes whether num2 is 0 or not,<br>if zero it will print can&#39;t divide by zero if not it divides<br>num1 and num2   num1 / num2 value stores in ans and<br>then returns the value ans    ans which is defined in<br>class will update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221629527-b1a94b7c-dc69-4920-ae33-81c5ea643996.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of division function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221633618-8152c37e-4402-4d60-807b-35acd9997e3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>tes_number_add_number(): This method contains a test case , MyCalc is assigned to calc<br>.we are passing two values to addition method and comparing to the given<br>number .The assert keyword lets you test if a condition in your code<br>returns True, if not, the program will raise an AssertionError.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221634524-ecc12e9c-55cf-4af0-9151-5899aa94c154.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_ans_add_number(): This method contains three test cases .series of data is passing ,in<br>first test we pass values and result of first test case is passed<br>as input to other series and second number we are passing and comparing<br>with r passing value .for loop checks all the three returns pass or<br>failure cases test cases by calling method addition and<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221636292-973e3d31-4109-4e40-956e-9c3e7743eb91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_number_sub_number() : This method contains a test case , MyCalc is assigned to<br>calc .we are passing two values to subtraction method and comparing to the<br>given number .The assert keyword lets you test if a condition in your<br>code returns True, if not, the program will raise an AssertionError.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221637466-f0d50491-569d-481c-aaeb-286777e4db8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_ans_sub_number(): This method contains three test cases #series of data is passing ,in<br>first test we pass values and result of first test case is passed<br>as input to other series and second number we are passing and comparing<br>with r passing value .for loop checks all the three test cases by<br>calling method subtraction and returns pass or failure cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221639171-df687768-dabd-4975-bb91-056873c7a034.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_number_mult_number(): This method contains a test case , MyCalc is assigned to calc.we<br>are passing two values to multiplication method and comparing to the given number<br>.The assert keyword lets you test if a condition in your code returns<br>True, if not, the program will raise an AssertionError.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221652858-89df6319-e92b-4fea-8870-2af318285057.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_ans_multi_number(): This method contains three test cases .series of data is passing ,in<br>first test we pass values and result of first test case is passed<br>as input to other series and second number we are passing and comparing<br>with r passing value .For loop checks all the three test cases by<br>calling method multiplication and returns pass or failure cases.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221653951-1476b785-9732-4c0a-b394-923c033a8214.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_number_div_number(): This method contains a test case , MyCalc is assigned to calc<br>.we are passing two values to divison method and comparing to the given<br>number .The assert keyword lets you test if a condition in your code<br>returns True, if not, the program will raise an AssertionError.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/221654335-d076f041-b357-4fc2-b1b7-2adce19c50df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_ans_div_number(): This method contains three test cases ,series of data is passing ,in<br>first test we pass values and result of first test case is passed<br>as input to other series and second number we are passing and comparing<br>with r passing value .For loop checks all the three test cases by<br>calling method division and returns pass or failure cases<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>In this assignment, i have learned about classes and methods , defining a<br>class, assigning variables, and using those variables in class.<div>Also, Pytest :&nbsp;&nbsp;</div><div><ul><li>&nbsp; &nbsp;How to<br>write test cases</li><li>&nbsp; &nbsp;How to define method in pytest</li><li>&nbsp; &nbsp;use of ASSERT keyword</li></ul></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ul><li>Test cases are used to check whether give code is working as expected<br>or not</li><li>Test cases are very easy to write because of its easy and<br>simple syntax</li><li>It detects bugs easily</li><li>Can run a specific test or a subset of<br>tests</li><li style="border: 0px; margin: 0px; padding: 0px;">Tests are run parallel</li><li style="border: 0px; margin:<br>0px; padding: 0px;">It can skip tests and automatically detect the tests.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/vg473" target="_blank">Grading</a></td></tr></table>