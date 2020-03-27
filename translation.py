class Translation(object):
    START_TEXT = """Hi `{}` . Thank You for using me.
/help to know how to use me
TL;DR, Please send a direct (video) link, and I will try to upload on Telegram.
© @MFB_DlBot
Subscribe @thwarikh if you 💔 using this bot.."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = """No Exclusive plans Available; more deatails contact @thwarikh"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "Trying to Downloading  ..."
    UPLOAD_START = "Trying to Uploading ..."
    RCHD_BOT_API_LIMIT = "Size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Share and Support."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nUploaded in {} seconds. \n@MFB_DlBot"
    NOT_AUTH_USER_TEXT = "You are Free User i Cna't procces it Now. \nPlease /upgrade your subscription."
    NOT_AUTH_USER_FILE_NAME = "Free user's can't upload file with @ in custom filename. You have to /upgrade in order to use custom filename with @ . Hope you understand what I am trying to say. Thanks for using @MFB_DlBot"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact @thwarikh"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = """✪༺ ──•◈•── ──•◈•──༻✪
🗂ᴄʜᴀɴɴᴇʟ : @MyFilmBox
🖼ᴄʜᴀɴɴᴇʟ : @MFBStreamz
📱ᴄʜᴀɴɴᴇʟ : @MFBlow
🆕ᴄʜᴀɴɴᴇʟ : @MFBhevc
📺ᴄʜᴀɴɴᴇʟ : @MFBTv"""
    NO_CUSTOM_THUMB_NAIL_FOUND = "No custom thumbnail found."
    NO_VOID_FORMAT_FOUND = "Something is wrong with the URL,\n<b>YouTubeDL</b> said: {}\nPlease check before trying again.\n If you think this could be a bug please report on @thwarikh"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
Name        :   {}
Plan name   :   {}
Expires on  :   {}"""
    HELP_USER = """Hi there , to know your plan details hit /me .
Instructions :-

To upload a media to Telegram send a valid http link, you can also set a thumbnail and new name.
Get external download link by replying with /getlink .
Convert media file to video by replying with /converttovideo .
Convert media file to audio by replying with /converttoaudio .
Rename files by replying with /rename ,you can also set thumbnail.
Generate custom thumbnail by replying with /generatecustomthumbnail .
Trim large videos hit /trim for more.
Take screenshots of Telegram media by replying with /generatescss .
Extract compressed Telegram media using /unzip .
Get a Telegram sticker as a Telegram downloadable media.

Type / for all commands"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get external download link."
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename ."
    AFTER_GET_DL_LINK = "Direct link generated.\n👉🏼 <a href='{}'>link</a>\n@MFB_DlBot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim start time[HH:MM:SS] end time[HH:MM:SS] \nExample:  Video /trim 01:50:10 01:52:30 \nPhoto /trim 01:50:10"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim Start Time (HH:MM:SS) End Time (HH:MM:SS) to cut a small photo / video, from the above media.\nExample:  Video /trim 01:50:10 01:52:30 \nPhoto /trim 01:50:10 "
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake contact @thwarikh ."
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to @Thwarikh"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    GET_LINK_ERRS_OCCURED = "Sorry the following Errors occurred: \n{}\nPlease check everything again twice, and if the issue persists, report this to @Thwarikh"
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 15 minutes.
/upgrade or Try {} seconds later."""
    G_DRIVE_GIVE_URL_TO_LOGIN = "Please login using {}. Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_IN_VALID_FORMAT = "Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_COMPLETE = "Logged In."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FED_UP_WITH_CRAP = "This bot is no longer leeching links for free users. @MFB_DLBot is open source, and you can deploy your own telegram upload by clicking on the links, available in GitHub README. or, Better /upgrade the subscription to continue using this bot."
