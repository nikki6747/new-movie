class script(object):
    START_TXT = """<b>π·π΄π»πΎ {},
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π</b>"""
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """<b>β― πΌπ π½π°πΌπ΄: {}</b>
<b>β― UPDATES: @M2LINKS</b>"""
    SOURCE_TXT = """<b>π ε½‘ [ @M2LINKS ] ε½‘ π</b>"""
    MANUELFILTER_TXT = """Help: <b>FILTERS Β»</b>

Β» <b>Filter is A Feature Where Users can Set Automated Reply to a Specific Word</b>

<b>Important Notes:</b>
1.<i> I Have To Be Admin </i>
2.<i> Only admins can add Filters in Chat</i>
3.<i> Buttons have a limit of 64 Characters</i>

<b>Commands and Usage:</b>
β’ <i> /filter - Add a Filter</i>
β’ <i> /filters - List of All Filters</i>
β’ <i> /del - Delete a Filter</i>
β’ <i> /delall - Delete All Filters</i> """
    BUTTON_TXT = """Help: <b>BUTTONS Β»</b>

Β» Supports both url and alert inline buttons.

<b>NOTE:</b>
1. <i>Telegram will not allows you to send buttons without any content, so content is mandatory.</i>
2. <i>Supports buttons with any telegram media type</i>
3. <i>Buttons should be properly parsed as markdown format</i>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/M2links)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>AUTO FILTER Β»</b>

πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. <i>Only Admins Can Add Connection</i>
2. <i>Send <code>/connect</code> To Connect Me to Your PM</i>

<b>Commands and Usage:</b>
β’<i> /connect  - Connect a Chat to your PM</i>
β’<i> /disconnect  - Disconnect from a Chat</i>
β’<i> /connections - List Of All Connections</i>"""
    EXTRAMOD_TXT = """Help: <b>Extra Features of Me Β»</b>

<b>Commands and Usage:</b>
β’<i> /id - Get ID Of A User</i>
β’<i> /info  - Get Info About a User</i>
β’<i> /imdb  - Get Movie/Series Info from IMDb</i>"""
    ADMIN_TXT = """Help: <b>ADMIN MODS Β»</b>

<b>NOTE:</b>
This Works Only For Admins!

<b>Commands and Usage:</b>
β’<i> /stats - Get Status of DataBase</i>
β’<i> /delete - Delete A File</i>
β’<i> /users - List of My Users </i>
β’<i> /chats - Get List Of My Chats </i>
β’<i> /leave  - Leave from a chat</i>
β’<i> /disable  - Disable a Chat</i>
β’<i> /ban  - Ban a User</i>
β’<i> /unban  - Unban a User</i>
β’<i> /channel - List of All Connected Channels</i>
β’<i> /broadcast - Broadcast a Message to All Users</i>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: {}
β ππΎππ°π» πππ΄ππ: {}
β ππΎππ°π» π²π·π°ππ: {}
β πππ΄π³ πππΎππ°πΆπ΄: {} πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: {} πΌππ±"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
