<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Venkata Sai Pragna Garisa (vg473)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 5:01:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vg473" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233855501-0202e6c9-1480-470c-b11d-13ca08f3b3ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of admin create item page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233855683-6339087d-35ce-47e3-a62f-e6a7259fd310.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of populated Products table clearly showing the columns<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>The values are input on the add page, they are delivered to the<br>item function in shop.py. It checks to verify if an id has been<br>passed before deciding whether the action is to modify or add. Considering that<br>no id is provided, this is a create action. As a result, an<br>INSERT statement is executed, passing the values to the Products table, and if<br>successful, a flash is displayed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/21">https://github.com/pragnagarisa/IS601_006_S23/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/admin/items">https://is601-vg473-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233856810-fa121491-64b1-4dd7-97f8-244b18217e68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233856920-394bf659-cbe3-46e7-bf62-4e5df98e41d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233857018-a71e3675-84d5-4b83-98b1-6640e2e0bef2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filters and a different sorting applied(sorted<br>low to high)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233857096-5544042e-4a2c-43fb-9e0f-78af42259b32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filters and a different sorting applied(sorted<br>high to low)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233857325-1c7b1db7-e81d-432a-ab86-98f74ccbec8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div>The Products table, whose visibility is set to 1, provides the initial data<br>for the shop page. The page also offers name searches, category choices, and<br>"High to Low" or "Low to High" sorting of prices. when we carry<br>out a search using one or more of the aforementioned methods. Then, based<br>on the input, we adjust the where condition of the query in the<br>shop list of the shop.py function.</div><div>then display the results once more.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/21">https://github.com/pragnagarisa/IS601_006_S23/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/shop?name=&category=Food&price=DESC">https://is601-vg473-prod.herokuapp.com/shop?name=&category=Food&price=DESC</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233858038-09edf1e3-6756-43d7-b6ea-d04879ce820e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of the Admin List page/results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233858076-f2ca4b2d-1a5a-4ac9-b0f7-812ee426e82e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot of the Admin List page/results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);">Without applying any filters, we choose every field from the<br>Products database and<br style="box-sizing: border-box;">feed it to the HTML page.</div><div dir="auto" style="box-sizing: border-box;<br>color: rgb(31, 35, 40); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial,<br>sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; background-color: rgb(246, 248, 250);">Since<br>no conditions are stated anywhere, every product<br style="box-sizing: border-box;">will be shown regardless of<br>visibility status.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/21">https://github.com/pragnagarisa/IS601_006_S23/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/admin/items">https://is601-vg473-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866269-d206839b-aa21-48fb-ad9a-fc4730a41e8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866322-06195fb7-3dac-42c5-a66e-ba06db396bff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866572-a38beb06-0428-4fe8-a474-1c9e3c9592e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866623-2cd1fca8-3a32-462a-9c9e-49444ffd2f43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of before Editing a Product via the Admin Edit Product Page:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866719-8d9c0110-8f12-448a-9ef4-81213067e6de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of After Editing a Product via the Admin Edit Product Page:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>In shop.html, each product contains a check to determine if the user is<br>signed in and if they are an administrator. If both conditions are met,<br>a button to modify the item is shown, which directs the user to<br>the page with the item's specifications.</div><div>If the user is an admin, the edit<br>button is shown on the item details page.</div><div>The edit button is the default<br>on the admin items page because only administrators can access it.</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/21">https://github.com/pragnagarisa/IS601_006_S23/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/admin/item?id=2">https://is601-vg473-prod.herokuapp.com/admin/item?id=2</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866891-62ba1515-94d8-4c53-839f-8866fe3cd7dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233866959-c7760b86-dda9-469d-b71c-7ed22aaf824e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product Details Page:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>I created the itemdetails.html and item details routines just for this.</div><div>When the product<br>name is clicked, the item details function receives the product id and uses<br>it to extract all the data from the Products database and show it<br>on the item details page.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/21">https://github.com/pragnagarisa/IS601_006_S23/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/itemdetails?id=2">https://is601-vg473-prod.herokuapp.com/itemdetails?id=2</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/233869840-fff62458-0d34-40a6-8abd-9cb3578df261.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234102432-b65db417-d34f-4751-b8bd-59123612aef9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234103310-c38e8342-a30b-4b9e-854b-266df79f37b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <div>The combined unique key for one cart per user is made up of<br>the product id and user id.</div><div><br></div><div>When a user is added to the cart,<br>an insert query is run to add the data to the cart, and<br>the user receives the items from the store. and execute update and delete<br>queries when a user wants to change the quantity of something or get<br>rid of a product.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>The product id is supplied as a hidden field to the cart function<br>in shop.py when the ADD button is clicked. As long as the quantity<br>is greater than 0, we then enter the product id, user id, desired<br>quantity, and unit pricing (fetching it from the products table).<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/22">https://github.com/pragnagarisa/IS601_006_S23/pull/22</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234104922-74d34a33-44ca-4877-ab83-22f2da1a53a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div>If a product id is not supplied when we click the cart, the<br>method detects that this is not an add or update function and tries<br>to see if one is being passed instead. The next step is to<br>navigate to the SELECT block where it retrieves the user and product identifiers,<br>name, and requested quantity. It then calculates the subtotal by dividing the desired<br>quantity by the unit price and sends these values to cart.html.</div><div>The subtotal value<br>for each row is added to a variable named ns.total, and the total<br>is then displayed at the bottom. Each item is rendered as a row<br>in a table in the HTML output for the purpose of computing the<br>total.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/22">https://github.com/pragnagarisa/IS601_006_S23/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/cart">https://is601-vg473-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234106324-447ef8d7-5230-4ef9-a928-456794f6527d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before screenshot of Cart Quantity update:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234106878-0b9cf091-3f1d-4091-939f-b0a92774a1d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After screenshot of Cart Quantity update:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234109127-e06a55bb-dfe6-4cdf-b2a1-92f637740484.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before  screenshot of setting Cart Quantity to 0:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234109394-afb421b3-de6b-4139-a088-e49a1bc3b0ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After screenshot of setting Cart Quantity to 0:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234112407-1074b920-85df-4e9a-8b4f-b1bb333f5799.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Negative quantity is handled:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>- A hidden product id is given to the cart function when we<br>click the update button next to the amount field and update button in<br>the cart.</div><div>- The code retrieves the name and price from the products table<br>if the quantity is more than 0, then updates the quantity and price<br>in the cart table while providing the product id and user id.</div><div>- When<br>we enter 0 in the amount box, the code advances to the DELETE<br>block where we delete the product from the cart database while giving the<br>product id and user id because the number is less than 0.</div><div>- To<br>accommodate negative amounts in the input field's minimum value in HTML, we set<br>it to 0.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/22">https://github.com/pragnagarisa/IS601_006_S23/pull/22</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234113097-29ff3d0a-0954-41b1-8275-fa5993a7dc2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before screenshot of deleting a single item from the Cart:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234113500-e82c5de3-b205-4e7c-99eb-ce8463f59d03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After screenshot of deleting a single item from the Cart:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234113500-e82c5de3-b205-4e7c-99eb-ce8463f59d03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before screenshot of clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/234114768-b5caf5dc-cb95-445c-93e5-c5420ac42134.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After screenshot of clearing the cart:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>A hidden field amount of -1 will be provided next to the delete<br>button when a single item is removed from a cart. If the hidden<br>field amount is less than zero, the cart function will perform the delete<br>query while delivering the product id.</div><div>If the value of the variable delete all<br>in the cart method is True, we delete the records in the Cart<br>table while supplying the user id when clearing the entire cart.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/pragnagarisa/IS601_006_S23/pull/22">https://github.com/pragnagarisa/IS601_006_S23/pull/22</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p><font size="3"><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">One  place where I got<br>stuck </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">was in<br>making</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> tables, <br> the cart table </span>&lt;span<br>style=&quot;outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;&quot;&gt;depends</span><span style="font-family: Arial, Helvetica,<br>sans-serif; white-space: pre-wrap;"> on </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;<br>white-space: pre-wrap;">the</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> product table and the query<br></span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">being created</span><span style="font-family:<br>Arial, Helvetica, sans-serif; white-space: pre-wrap;"> <br> </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial,<br>Helvetica, sans-serif; white-space: pre-wrap;">The</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> cart table is<br>before the  product table </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica,<br>sans-serif; white-space: pre-wrap;">is created,</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> so </span><span style="outline:<br>0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">mine is</span><span style="font-family: Arial, Helvetica,<br>sans-serif; white-space: pre-wrap;"> <br> </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;<br>white-space: pre-wrap;">The products</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> table was </span><span style="outline:<br>0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">created,</span><span style="font-family: Arial, Helvetica, sans-serif;<br>white-space: pre-wrap;"> but the </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;<br>white-space: pre-wrap;">products could</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> not </span><span style="outline: 0px;<br>box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">be inserted</span><span style="font-family: Arial, Helvetica, sans-serif;<br>white-space: pre-wrap;"> <br> cart and </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica,<br>sans-serif; white-space: pre-wrap;">then I found</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> that </span>&lt;span<br>style=&quot;outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;&quot;&gt;the</span><span style="font-family: Arial, Helvetica,<br>sans-serif; white-space: pre-wrap;"> cart table </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica,<br>sans-serif; white-space: pre-wrap;">is not</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> created and <br><br></span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">Then I notice<br>that I</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> run inti_db.py again and the<br>cart table was </span><span style="outline: 0px; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif; white-space:<br>pre-wrap;">there</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> <br> </span><span style="outline: 0px; box-sizing: border-box;<br>font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;">created</span><span style="font-family: Arial, Helvetica, sans-serif; white-space: pre-wrap;"> <br><br><br></span></font><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vg473-prod.herokuapp.com/">https://is601-vg473-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vg473" target="_blank">Grading</a></td></tr></table>