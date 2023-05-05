<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Venkata Sai Pragna Garisa (vg473)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 11:14:22 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/vg473" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220223872-077cdb7e-0c9f-409c-9950-653a2b3c395f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>add_task() takes in name, description, due as arguments. When any of these argument<br>has an empty string or due is in incorrect format. I&#39;m raising an<br>exception with approriate message that is caught and error message is shown to<br>the user. When the data is entered correctly, the add_task() will convert due<br>string to datetime format and update template task with provided arguments, and then<br>add it to the list and save it to tracker.json file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220224163-e4cfb179-ebf7-4eb7-bfa4-60e51affa06b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful execution of adding a new task and saving it.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220224460-b96b6494-50f1-46ed-a574-3436e36cdfbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case where the error message shows that description is missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220224597-7d59f328-b988-47d7-b987-11afbf661240.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case where the due date string is given in an incorrect format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;"><div style="">add_task() takes in name, description, due as arguments. When any<br>of these argument has an empty string or due is in incorrect format.<br>I'm raising an exception with approriate message that is caught and error message<br>is shown to the user. When the data is entered correctly, the add_task()<br>will convert due string to datetime format and update template task with provided<br>arguments, and then add it to the list and save it to tracker.json<br>file</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220226966-4f54c01c-7d7d-487e-9aaa-bfb56ec1d942.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>process_update() checks whether the given is in tasks or not. if it is<br>in tasks range, it reads update_task() function variables; else printing an error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>process_update() checks whether the given is in tasks or not. if it is<br>in tasks range, it reads update_task() function variables; else printing an error message<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220232831-1c974787-961f-43c5-8678-3b0e51a7ee96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update_task() code that updates an existing task if new values are valid and<br>doesn&#39;t match old values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220229800-1aa8e709-9c07-4064-9041-641b187f2558.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success case where the task is updated with the new values<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220234132-d366f639-1a02-4b68-b752-a815a9594d79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case where the new values match existing task values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;"><div style="">update_task() get the value for the process_update(),</div><div style="">  <br> - if index value is less than zero or greater than or<br>equal to len(tasks) it prints invalid index</div><div style="">    - if<br>index value is valid, it checks given name,description,due are valid and compare them<br>with the old values, </div><div style="">      &nbsp; if<br>new values aren't matching old values, prints a message that the task is<br>updated and saves updated task to tasks</div><div style="">     <br>&nbsp; if new values are same as old, it prints a message task<br>not updated.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220236038-bc4661ec-0634-4d5c-8cfb-736fea6c0395.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for mark_done() that is used to mark a task as done<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220235975-73f5fd53-e841-442f-a7c5-4921f421eb1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success case where a unmark case is mark done<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220236141-ddc0061a-6421-4016-bd2b-a387d1c1072e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case where we attempt to mark a task that is already marked<br>as done<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;"><div style="">mark_done() does following things,</div><div style="">&nbsp; - if index is out<br>of range, then a message invalid index is shown</div><div style="">&nbsp; - if index<br>is valid and task is not done, done and lastActivity are updated with<br>current timestamp and task completed message is printed</div><div style="">&nbsp; - if index is<br>valid and task done value is not False, task completed message is printed</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220236953-c6cae904-5a29-4656-8b97-715b23ec2f80.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for view_task() to pick and display the right task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220237030-2af01ce3-5e45-411a-853b-d6b5e24d1ef3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success case where the index is valid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220237099-fc679b69-737f-4048-8f64-117adf98b027.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case where the index is out of bound<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220237459-c1da7b6a-7306-4285-af74-fc725635e58f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_task() results show 5 added tasks<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220238381-18b45a2c-0d32-4778-a736-df899bb5ed42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for delete_task() that takes in index value to find and remove it<br>from tasks list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220238315-00366612-de63-4831-9e16-5067c185a624.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success case where index is valid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220238457-d99dfdc4-7927-41bf-aa21-a450a60b4e9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure case where index is out of range<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;">delete_task() delete the task from tasks based on index value if<br>index values is valid and in case the index value is out of<br>range, it will print an error message</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220240052-884d716a-1c8e-4409-b914-74c13b46330a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for get_incomplete_tasks() to print all incomplete tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220239592-95878295-094d-4db6-a8e4-9bc6abe70608.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220240337-c5ac5f1d-f6e6-4ea7-b7e7-71ebdc8b2b51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;"><div style="">get_incomplete_tasks() loops over all the tasks and find incomplete task<br>and adds them to _tasks list. </div><div style="">Once the loop is done, list_tasks()<br>is called to print all incomplete tasks if _tasks has any tasks if<br>not it prints no incomplete tasks message</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220241167-8b312448-5033-4510-8009-17ca769bc96d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for get_overdue_tasks() to display overdue tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220241252-007e99d5-472c-4cb5-a5f4-e59d5aec5cc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220241402-f11f1f7d-281a-403d-9826-120805b2d1bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;"><div style="">get_overdue_tasks() loops over all tasks to see if any task<br>due timestamps are in past and add them to _tasks.<br>If _tasks has more<br>than one task in it, we call list_tasks() or else print no overdue<br>tasks message</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220243271-ab4dc73b-018a-4e74-9341-0f74121bd09e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for get_time_remaining() that display remaining or overdue time in a formatted message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220243222-f9daade0-fc5c-4a39-80c9-49258aacd4e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Both success (remaining time) and failure (over due by) cases are in the<br>screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 18px;"><div style="">get_time_remaining() does following things,</div><div style=""><ul><li>if index is invalid, prints an<br>error message</li><li>if index is valid, we find the task and change the due<br>string to datetime format - task_due_datetime.<br>task_due_datetime is then compared with current timestamp to<br>get the difference<br>I have used two functions, diff_in_secs() which gives me the seconds<br>difference between two datetimes and<br>format_time_diff() which converts those seconds into days, hours, minutes,<br>seconds with abs().</li><li>at the end, if due is before current time, we print<br>it as remaining time and if due is after current time we print<br>it as over due by</li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220244658-93ffeb2c-0909-4628-934b-762ae7216034.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showcases add, list, done, incomplete events<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/220244881-1bca3197-aece-408f-9cac-13a7e5a3c428.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>tracker.json file shows 3 different tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>Initially, I had hard time with converting the date formats in hours, minutes<br>and seconds for which I was able research a bit on the web<br>and I finally was able to come up with a solution that I<br>think solved the problem.<div>I also found that handling edge cases and exception cases<br>needed to be done carefully .</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/4">https://github.com/pragnagarisa/IS601_006_S23/pull/4</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/vg473" target="_blank">Grading</a></td></tr></table>