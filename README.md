<h1 align=center>Lauchbot</h1>
<p align="center">A Discord Bot programmed by <a href="https://github.com/Lauchschwert">Me</a> and <a href="https://github.com/anditv21">@anditv21</a></p>
<p align="center"><img src="https://cdn.discordapp.com/avatars/934460478510493788/4b86154cdc5f241fcf3f51f4da6abf87.webp?size=256"></p>
<details>
<summary>Commands</summary>
<ul>
   <li>Added avatar command which shows the avatar of a mentioned user</li>
   <li>Added command which nukes a discord Channel</li>
   <li>Added command which sends mine and anditv's github</li>
   <li>Added command which sends my Twitch - Channel</li>
   <li>Added command which sends my Youtube - Channel</li>
  <li>Added command for my website</li>
   <li>Added help command which shows all commands</li>
   <li>Added clear command which deletes a specified amount of messages</li>
   <li>Added download command which allows you to download YouTube videos</li>
   <li>Added Miesmuschel command</li>
   <li>Added reverse command which reverses a string</li>
   <li>Added userinfo command which displays informations about a user</li>
   <li>Added fact command which gives you a random useless fact</li>
   <li>Added fact command which gives you a random useless fact BUT in the german language</li>
   <li>Added RPC command which changes the bots activity</li>
   <li>Added Kick command</li>
   <li>Added Ban command</li>
</ul>
<h1>More coming soon!</h1>
</details>

<details>
<summary>Setup</summary>
<ol>
   <li>Create a file named token.txt in the same directory as the main.py file</li>
   <li>Go to <a href="https://discord.com/developers/applications">https://discord.com/developers/applications</a></li>
   <li>Click "New Application"</li>
   <li>Click "Bot" in the navigation bar</li>
   <li>Click "Add bot"</li>
   <li>Click "Yes, do it!"</li>
   <br>
   <img src="https://i.ibb.co/27mLWRJ/image-2022-05-31-164248276.png">
   <br>
   <li>Click "Reset Token"</li>
   <li>Click "Yes, do it!"</li>
   <li>Enter your 2FA Code if you have to.</li>
   <li>Copy and paste your Token into token.txt</li>
   <br>
   <img src="https://i.ibb.co/9vvNyw4/image-2022-05-31-172427950.png">
  <li>Open CMD (Command Prompt) and cd to your Bot directory</li>
  <br>
  <img src="https://i.ibb.co/x2GMCMY/image-2022-05-31-171506522.png">
  <br>

  As you can see, the bot is located on my desktop.
    So I have to type "cd Dekstop\Lauchbot-main" and press enter
    <br>
  <li>Run pip install -r requirements.txt</li>
  <li>Last but not least: Run python main.py
</ol>
</details>

<details>
<summary>Linux Rootserver-setup</summary>
 <ol>
    <li>Open your FTP application you use for your server and connect to your rootserver.</li>
    <li>Go to your root location in your server and drag the Lauchbot folder with all the files (except Readme.md, .gitignore and temp_main) into it</li>
    <li>Connect to your server via your SSH Client</li>
    <li>Go to your root directory (or type: "cd root")</li>
    <li>You need to install python to your server. To install python type: "wget https://bootstrap.pypa.io/get-pip.py" and after that command use: "python3 ./get-pip.py"</li>
    <li>Now you need to install pm2, so your bot autostarts even after your linux Server restarts. To install pm2 follow this <a href="https://pm2.io/docs/runtime/guide/installation/">guide</a></li>
    <li>After you installed python and pm2, go to the folder-directory you named your bot (in my case Lauchbot): "cd YourFolderName"</li>
    <li>Then type: "pip3 install -r requirements.txt"</li>
    <li>After the packages are installed type: "pm2 start main.py"</li>
    <li>If you did everything right you'll notice that your bot started, Congrats!</li>
    <li>You can also test the autostart just by restarting your linux server.</li>
 </ol>
</details>