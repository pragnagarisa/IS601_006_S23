<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Venkata Sai Pragna Garisa (vg473)</td></tr>
<tr><td> <em>Generated: </em> 3/20/2023 7:10:08 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/vg473" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226391475-b9a23c78-3011-45f7-a447-f3e73a566069.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Calculate_cost function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226392278-74fd59c3-43e1-4b2e-b350-569398fddc05.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output adding total cost of a burger<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; line-height: normal; font-family:<br>&quot;Helvetica Neue&quot;;"><font size="3">calculate_cost function calculates the total cost of burger, inprogress_burger list have<br>all the user added data and the cost of bun, patty and toppings<br>are added to total_cost and return total_cost</font></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian:<br>normal; font-stretch: normal; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><font size="3"><br></font></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric:<br>normal; font-variant-east-asian: normal; font-stretch: normal; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><font size="3">total = input(<br>f'Your total is {"${:,.2f}".format(expected)} please enter the exact value.\n')</font></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric:<br>normal; font-variant-east-asian: normal; font-stretch: normal; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><font size="3"><span class="Apple-converted-space">&nbsp; &nbsp;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span>self.handle_pay(expected, total)</font></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal;<br>font-variant-east-asian: normal; font-stretch: normal; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><font size="3">total is converted in<br>the currency format</font></p><p class="p2" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal;<br>font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><br></p><p class="p1" style="margin-bottom:<br>0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica<br>Neue&quot;;"><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226396175-ef0b7894-b98c-4fb2-bf1d-36c5740941b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>OutOfStockException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226397995-8ba88223-8e1e-48e1-8772-a55fe098bb00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output handling Outofstock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226399722-54f5135d-8393-4021-83e7-5252db7a8366.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>NeedsCleaningException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226400038-743a2bb4-652f-4338-95fd-15378cee5b8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output handling NeedsCleaningException (positive)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226400981-6a1d3562-6287-4870-8743-315662ef25ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output handling NeedsCleaningException (Negative)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226401677-5af74565-f674-4b86-b1d2-95914505443e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226402525-7f657dd4-a118-44e1-97ac-e28acc049205.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output handling InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226403362-99eadc91-87c0-441b-b8d5-ea1dbc1f0e33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ExceededRemainingChoicesException:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226404295-88284abf-38b6-4186-8e74-ddd39628290c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output handling ExceededRemainingChoicesException:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226405153-4ca698fc-9091-4d69-9c05-b919e1155db3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidPaymentException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226405502-34669e4a-af31-4feb-94b2-19ddfdfbd08c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output handling InvalidPaymentException:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;"><b>OutOfStockException:</b><span class="Apple-converted-space"><b>&nbsp;</b> </span>At any stage, if an item goes out<br>of stock, it will be handled with OutOfStockException.Inside OutofStockException, We print the message<br>mentioning at which stage and what item (passed in as exception argument 'ie')<br>went out of stock.</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal;<br>font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><br></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian:<br>normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><b>NeedsCleaningException:</b>NeedsCleaningException is raised at<br>stage patty, when remaining_uses = USES_UNTIL_CLEANING user needs to type the word CLEAN<br>, them clean_machine function is called and cleans the machine and prints machine<br>clean, if user input is not cleaned it clean_machine function isn't called and<br>prints message machine not cleaned yet</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal;<br>font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><br></p><p class="p1" style="margin-bottom: 0px; font-variant-numeric:<br>normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><b>InvalidChoiceException:</b>At any<br>stage, if an item name is invalid, it will be handled with InvalidChoiceException.Inside<br>InvalidChoiceException, We print the message mentioning at which stage and what item (passed<br>in as exception argument 'ce') name is invalid.</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal;<br>font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><br></p><p class="p1" style="margin-bottom:<br>0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica<br>Neue&quot;;"><b>ExceededRemainingChoicesException: </b>At any stage, selecting choices are exceeding , it will be handled<br>with ExceededRemainingChoicesException. Inside ExceededRemainingChoicesException, We print the message mentioning at which stage choices<br>are exceeding (passed in as exception argument 'ee')</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal;<br>font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><br></p><p class="p1" style="margin-bottom:<br>0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica<br>Neue&quot;;"><span class="Apple-converted-space">&nbsp;</span><b>InvalidPaymentException:&nbsp;</b>If user enter data is not matching with valid calculation at handle_pay<br>function<span class="Apple-converted-space">&nbsp; </span>InvalidPaymentException exception is raised.We print the Invalid payment message (passed is<br>an exception argument 'pe')</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal;<br>font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;"><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226431163-c131c7e6-58f0-46f1-b616-3c1eec2ab3d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_bun_first : bun must be the first selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226433841-71ca13c7-3e38-4dc8-9110-d4fca9d71723.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_patty_Outofstock <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226435144-951c78aa-6eb9-43fc-87f9-86325717a2b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_toppings_Outofstock <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226436272-1bc15cff-5854-4d25-88c3-d1752354f867.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_patty_Exceedingchoice<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226437089-088dbe0e-d0ed-42d5-904c-9057d88ae1ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_toppings_Exceedingchoice<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226483085-d775200a-d529-48ac-8f2a-300674f8f4dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cost calculation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226441457-52eba4ae-070d-469f-a0b9-2864de24dfc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Total_sales<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226441930-bd58a0fa-664a-4354-8d12-64d0e1e7ac51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Total_sales_output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226442693-17dadeb2-b6f5-4a32-9769-6d03dc72361f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>total burgers increment after each sale<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226443470-3ff2a3b4-b415-4bd4-ba8a-beeddf345e48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>total burgers increment after each sale - output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;"><b>Test 1 - bun must be the first selection (can&#39;t add<br>patties/toppings without a bun choice) :&nbsp;</b></span>In test_bun_function InvalidstageException is raised when &#39;bun&#39; is<br>not selected so, the test cases passed<br><div><span style="font-size: 13px;"><b>Test 2 - can only<br>add patties if they&#39;re in stock:&nbsp;</b></span><span style="font-size: 13px;">In&nbsp;test_patty_Outofstock function OutofstockException is raised when<br>patty item went out of stock and still user trying to select it,<br>in test case patty beef quantity is 1 , when we try to<br>select 2 beef&#39;s OutofstockException is raised, hence the test case passed</span></div><div><span style="font-size: 13px;"><b>Test<br>3 - can only add toppings if they&#39;re in stock: I</b></span><span style="font-size: 13px;">n&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;test_toppings_Outofstock function OutofstockException is raised when toppings item went out of stock<br>and still user trying to select it, in test case topping lettuce quantity<br>is 10, when we try to select lettuce OutofstockException is raised, hence the<br>test case passed</span></div><div><span style="font-size: 13px;"><b>Test 4 - Can add up to 3 patties<br>of any combination :</b> In test_patty_Exceedingchoice function&nbsp;</span><span style="font-family: &quot;Helvetica Neue&quot;; font-size: 13px;">ExceededRemainingChoicesException is<br>raised when more than 3 patties are selected, in test case 4 patty<br>items are selected where exception is triggered, so the test case passed.</span><span style="font-size:<br>13px;"><br></span></div><div><span style="font-size: 13px;"><b>Test 5 - Can add up to 3 toppings of any<br>combination :</b>&nbsp;</span><span style="font-size: 13px;">In test_topping_Exceedingchoice function&nbsp;</span><span style="font-family: &quot;Helvetica Neue&quot;; font-size: 13px;">ExceededRemainingChoicesException is raised<br>when more than 3 toppings are selected, in test case 4 toppings are<br>selected where exception is triggered, so the test case passed.</span><span style="font-family: &quot;Helvetica Neue&quot;;<br>font-size: 13px;"><br></span></div><div><div><span style="font-size: 13px;"><b>Test 6 - cost must be calculated :</b> Cost of<br>the burger is calculated and converted in currency format.</span><br></div></div><div><span style="font-size: 13px;"><b>Test 7 -<br>Total Sales (sum of costs) :&nbsp;</b></span><span style="font-family: &quot;Helvetica Neue&quot;; font-size: 13px;">test_total_sales function calculates<br>the total burger sales, in test case machine.total_sales holds the sum of the<br>three burger sales value.</span></div><div><span style="font-size: 13px;"><b>Test 8 - Total burgers should properly increment<br>for each purchase : </b>In test_total_burgerscount function, initially total_burgers is &#39;0&#39; and after<br>three sales total_burger incremented to &#39;3&#39;, hence the test case passed</span><span style="font-family: &quot;Helvetica<br>Neue&quot;; font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/15">https://github.com/pragnagarisa/IS601_006_S23/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ul><li>Through this assignment i got clear idea about both exceptions and pytests</li><li>How exceptions<br>are raised and handled</li><li>pytest to test how exceptions are handled</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226463471-3cb9ac37-b341-4ff9-925a-026b7f85cb87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of successful program execution <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226464386-ac2e981b-e671-4800-a2e6-501c221b2b07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of successful program execution <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/226483688-5d25727d-ac1e-427d-8089-a0fdb689054f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/vg473" target="_blank">Grading</a></td></tr></table>