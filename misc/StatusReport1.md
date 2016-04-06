<h4>Status Report #1</h4>

<h5>1. Project description</h5>
<p>By request from the sustainability officer, a group of 6 students (including myself) are using Raspberry Pi computers to collect temperature data from the Bliss residence hall, and compiling the data into a single database for later analysis.</p>

<h5>2. Project goals (overall)</h5>
<p>To collect at least a month of data, and represent this data graphically on a website.</p>

<h5>3. Your project implementation plans.</h5>
<ul><li>Deploy about 8 raspberry pis (RPI) around Bliss</li>
<li>Have them collect data via cronjob (scheduled task) into sqlite3 database</li>
<li>Have Linux Apache MySQL PHP (LAMP) service pull data from RPIs</li>
<li>Graphically represent data from LAMP server via JavaScript</li></ul>

<h5>4. How you broke up the project into components – describe each component</h5>
<ul><li>Jabari- Logistics and Documentation</li>
<li>Heidi - Python data collection script and cronjob</li>
<li>Brendan - Networking, LAMP server</li>
<li>Victoria (other group Liason)- Use flask to convert data from sqlite3 to JSON objects</li>

<li>To be determined - GUI and graphical representation of data</li></ul>

<h5>5. For each component above, describe how much work you have done, and what remains to be done. Include hardware and software used.</h5>
<p>Heidi - Python temperature data logger is completed and working.  I was able to add a cronjob within the python script and create a table that stores the temperature every 10 minutes.  Integration with Brendan's code worked successfully.</p>

<h5>6. Summarize your project's “good” and “bad” aspects, “easy” and “tough” aspects, from the group's point of view</h5>
<h6>Good: </h6>
<p>Decision making is relatively smooth. We now have the physical RPIs, and have the software to collect the data.</p>

<h6>Bad: </h6>
<p>We failed to meet our deploy by April 1 deploy deadline. We also chose to leave all of the networking in the hands of Brendan. This is arguably an academic disservice to the rest of the group in that we will not have learned anything about networking because we let the expert do it instead of us learning on our own. This however, was done out of efficiency and the interest in time. We also chose a networking option that has many "quick and dirty" fixes. This impacts the scalability and portability of our project. Without Brendan, our project is essential in its infancy. We did not evenly distribute the back end responsibilities well.</p>

<h5>7. Describe your goals for the next 3-4 weeks</h5>
<p>Get the networking setup so that we can deploy the Pis as soon as possible [<b>Edit: </b>As of April 6, the networking is working. Our next step is to copy the sd cards.] Begin to develop our GUI and representation of the data.</p>

<h5>8. List group members, and each member's contributions.</h5>
<ul><li>Heidi - Python script and cronjob are written and working. (Will perform bug check [<b>Edit: </b> As of April 6, the bug was fixed])</li>
<li>Victoria - Flask is complete, the sqlite3 entries are returning JSON objects as desired</li>
<li>Brendan - LAMP server still in progress [<b>Edit: </b>As of April 6, the server is working with the test pi.] Static IP address on subnet have been successfully reserved.</li>
<li>Jabari - Organized meet dates, communication link to sustainability officer, reserved rooms to collect temperature data and is currently creating documentation</li></ul>

