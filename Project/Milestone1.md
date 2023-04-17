<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Venkata Sai Pragna Garisa (vg473)</td></tr>
<tr><td> <em>Generated: </em> 4/17/2023 3:41:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/vg473" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256429-949baa75-7cb2-4d6d-8573-cc28d6ecb654.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256513-f29feac7-9c97-4fa7-ac44-c97ba5adba73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256555-ebba7cca-8d0e-4418-b5e4-b3bb12ce5add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256601-efd29998-2152-40bc-8ab4-ecae0d0c79fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256674-c83155d5-a8d9-4957-b6c2-bcfd36190a48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username is not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256730-bad735ae-de87-4990-918a-6ba11b698257.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232258572-b30b4e21-3ee1-4460-9abe-70bc5b4870b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid User data in database (test_7, last one)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1.For form production and validation, we employ WTforms.</div><div>2. Both in the frontend and<br>the backend, data is checked using WTform validators. For example, the username must<br>be between 2 and 30 characters long and cannot already be in use<br>by another user.</div><div>3. The password and confirm password should both be identical and<br>eight characters long. This is verified using wtform validators and stored in the<br>database using the bcrypt hashing technique.</div><div>4. The users table stores the hashed password,<br>username, and email.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232259368-2d356680-d3a0-4dca-8749-f188d0f863b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232259754-a15dd37b-7126-4c37-9608-c966ce38235b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><font size="2">1.We will utilize the username or email field instead of the confirm<br>password field on the login form, which is handled using wt forms.</font></div><div><font size="2">2.<br>In the front end, if a username or email field has a "@,"<br>it will use an email validator; otherwise, it will verify the username format,<br>see if the length is between 2 and 30 or not, and see<br>if a password has been provided or not.&nbsp;</font></div><div><font size="2">We retrieve data from the<br>users table in the backend using the user's email and username. If we<br>receive anything, we compare the password and then determine whether the user has<br>roles assigned.</font></div><div><font size="2">3. First, we verify that the password was entered at the<br>front end, and then we retrieve the password from database based on username/email</font></div><div><font<br>size="2">&amp; then check if the passwords match, if they match then we delete</font></div><div><font<br>size="2">the password from that point in the program.</font></div><div><font size="2"><span style="color: rgb(31, 35, 40);<br>font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;,<br>&quot;Segoe UI Emoji&quot;; background-color: rgb(246, 248, 250);">4. we fetch username, email, password</span><br style="box-sizing:<br>border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica,<br>Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; background-color: rgb(246, 248, 250);"><span style="color:<br>rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif,<br>&quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; background-color: rgb(246, 248, 250);">from users table passing<br>username/email, and then check if passwords match, and then</span><br style="box-sizing: border-box; color: rgb(31,<br>35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple<br>Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; background-color: rgb(246, 248, 250);"><span style="color: rgb(31, 35, 40);<br>font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;,<br>&quot;Segoe UI Emoji&quot;; background-color: rgb(246, 248, 250);">check if the user is assigned is<br>any roles from userroles tables &amp;</span><br style="box-sizing: border-box; color: rgb(31, 35, 40); font-family:<br>-apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe<br>UI Emoji&quot;; background-color: rgb(246, 248, 250);"><span style="color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;,<br>&quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;<br>background-color: rgb(246, 248, 250);">fetch it.</span></font><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232346014-e866a22a-3a8a-4fd2-a881-b5681091bf8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232346367-2d1a2237-59af-4242-9a2c-c219b1d37a0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><font color="#1f2328" face="-apple-system, system-ui, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px; background-color: rgb(246, 248, 250);">We&#39;ll define a variable<br>for login_manager outside of the app factory since we&#39;re using one, and then<br>inside the factory we&#39;ll utilize its init_app() method to link the app.</span></font><br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232346367-2d1a2237-59af-4242-9a2c-c219b1d37a0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232485594-c67b456a-d0d4-4b4f-82ac-a04ae8d7834e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232556932-31cb4351-741a-4876-94bd-ba2e7fee1464.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232557565-7d72252e-f25c-4be2-abee-4cf4a0567f0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the UserRoles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><span style="box-sizing: border-box;">Since we’re using an app factory we’ll defined<br>a<br style="box-sizing: border-box;">variable for login_manager outside of the factory, t</span><span style="box-sizing: border-box;">hen inside<br<br>style="box-sizing: border-box;">the factory we use its init_app() method to associate the app,&nbsp;</span></p><div dir="auto"<br>style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;,<br>Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246,<br>248, 250);">For<br style="box-sizing: border-box;">the login protected pages, we decorate the views with @login_required<br>function,&nbsp;If the user<br style="box-sizing: border-box;">is not logged in, it calls the&nbsp;</div><div dir="auto" style="box-sizing:<br>border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica,<br>Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246, 248,<br>250);"><a href="https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.unauthorized" title="flask_login.LoginManager.unauthorized" rel="nofollow" style="box-sizing: border-box; background-color: transparent; text-decoration-line: none;">&lt;span class="pre"<br style="box-sizing: border-box;">style="hyphens:<br>none;"&gt;LoginManager.unauthorized</a>&nbsp;function.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Here, we use the @admin_permission_require function from the roles.permissions package, similar to the<br>login protected page. We raise a 403 exception and display a 403 html<br>page with the message &quot;Permission denied&quot; if the user is not an administrator.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232558803-1bcf7522-f9c8-41ca-9833-0c0502c8a496.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots to show examples of your site&#39;s styles/theme<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232559264-ba9705a2-c15d-428f-b92d-cbb26d3a99cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232559668-6fd1a954-251b-4450-a3b7-2827755afa31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232559952-9bddf7bc-2ffe-4a8c-a02c-1db0a6059dac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>We utilize Bootstrap styling.&nbsp;</div><div><br></div><div>Navbars need to be wrapped.navbar featuring.navbar-expand-lg and bg-light are used<br>for responsive collapse at big break points and color, respectively.for the project's name,<br>use navbar-brand.navbar-nav provides full-height, lightweight navigation with dropdown support.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232346367-2d1a2237-59af-4242-9a2c-c219b1d37a0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error -1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232562348-83211b44-47e4-4daf-ae5d-7d07c50a7c8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error - 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232256429-949baa75-7cb2-4d6d-8573-cc28d6ecb654.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error - 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica,<br>Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246, 248,<br>250);">we use flask error handler functions for 403 &amp; 404 errors, and at</span>&lt;br<br>style=&quot;box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;,<br>Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246,<br>248, 250);&quot;&gt;<span style="color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;,<br>Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246,<br>248, 250);">most places we see what code is doing in backend and write<br>a</span><br style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto<br>Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color:<br>rgb(246, 248, 250);"><span style="color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto<br>Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color:<br>rgb(246, 248, 250);">flash message for that, if any field is missing or else<br>other.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232564221-9084806b-b5e6-4d96-a2ea-2bced374b9de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">when </span><span style="outline: 0px; box-sizing:<br>border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">the</span><span style="font-family: Arial, Helvetica, sans-serif;<br>font-size: 18px; white-space: pre-wrap;"> profile page is opened, if it is not a<br>POST </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space:<br>pre-wrap;">request,</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> then <br> email, </span>&lt;span<br>style=&quot;outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;&quot;&gt;the</span><span style="font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> username </span><span style="outline: 0px; box-sizing: border-box;<br>font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">is taken</span><span style="font-family: Arial, Helvetica, sans-serif;<br>font-size: 18px; white-space: pre-wrap;"> from </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica,<br>sans-serif; font-size: 18px; white-space: pre-wrap;">the username</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space:<br>pre-wrap;"> table </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px;<br>white-space: pre-wrap;">that passes the username,</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"><br>then </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space:<br>pre-wrap;">is</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> <br> </span><span style="outline: 0px;<br>box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">is presented to</span><span style="font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> the profile form.</span><br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232565603-e6cc94d2-dc3a-4d5f-9c7d-493f2741c9d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232565883-51d7ba3e-7cb7-49d0-997e-20d37e9884d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232567335-323f29da-1f35-4d3b-a469-b567b78085b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232567582-5ed74a59-a9a8-471a-9527-4524c73ecd7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232568209-471b049b-4271-4f79-a753-3dfc581ce83c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232568877-86033ab7-5c93-45aa-93b4-e64c0d06e69c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before edit (pragna_garisa - user name)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/232571065-c83ef999-6734-4e8a-8135-8ec44d4d955e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit (pragna_garisa24 - user name)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/19">https://github.com/pragnagarisa/IS601_006_S23/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">The code first checks <br>if it is </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size:<br>18px; white-space: pre-wrap;">a</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> POST request,<br>if it is, <br> then  checks if </span><span style="outline: 0px; box-sizing: border-box;<br>font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">the current passwords, passwords</span><span style="font-family: Arial,<br>Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> and </span><span style="outline: 0px; box-sizing: border-box; font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">confirmation</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px;<br>white-space: pre-wrap;"> are </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size:<br>18px; white-space: pre-wrap;">given and</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> then<br></span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">valid</span>&lt;span<br>style=&quot;font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;&quot;&gt; <br> password </span><span style="outline: 0px;<br>box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">of</span><span style="font-family: Arial, Helvetica,<br>sans-serif; font-size: 18px; white-space: pre-wrap;"> users table,  current password and pwd </span>&lt;span<br>style=&quot;outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;&quot;&gt;of</span><span style="font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> DB are <br> compared to </span>&lt;span<br>style=&quot;outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;&quot;&gt;checking</span><span style="font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> if they are the same or<br>not, if they are <br> </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica,<br>sans-serif; font-size: 18px; white-space: pre-wrap;">is</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"><br>not </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space:<br>pre-wrap;">the same,</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> we  raise<br></span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">the<br>wrong</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> password  if they<br>are </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space:<br>pre-wrap;">the</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> same <br>  the<br>new password is </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size:<br>18px; white-space: pre-wrap;">then</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> hashed and<br>updated in the database. </p><br><p> Then the username <br> and </span><span style="outline:<br>0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">the</span><span style="font-family: Arial,<br>Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> email </span><span style="outline: 0px; box-sizing: border-box; font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">is</span><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px;<br>white-space: pre-wrap;"> updated in the database and </span><span style="outline: 0px; box-sizing: border-box; font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">the instant</span><span style="font-family: Arial, Helvetica, sans-serif; font-size:<br>18px; white-space: pre-wrap;"> message &quot;saved profile&quot; <br> is displayed.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p><b style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">Learn</b>&lt;span<br>style=&quot;font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;&quot;&gt; how  flask_login works and<br>how </span><b style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space:<br>pre-wrap;">to use</b><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> loginmanager  for<br></span><b style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">sessions</b>&lt;span<br>style=&quot;font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;&quot;&gt; and <br> </span><b style="outline: 0px;<br>box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;">everyone, see the</b><span style="font-family:<br>Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> flask_login documentation. and also how error<br>handlers work for known </span><b style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;<br>font-size: 18px; white-space: pre-wrap;">errors</b><span style="font-family: Arial, Helvetica, sans-serif; font-size: 18px; white-space: pre-wrap;"> <br><br>errors like 403 and 404.</span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/sample">https://is601-vg473-prod.herokuapp.com/sample</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/vg473" target="_blank">Grading</a></td></tr></table>