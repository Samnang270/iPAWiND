api_id = 30215079  # get this from my.telegram.org
api_hash = "529efffdc4de7009d7b7514b54aa0dd7" # get this from my.telegram.org
bot_token = "8834455555:AAGfoQUgVv2r9aCuN6plxCXRsn7iMNEMDaM"  # get it from @botfather
server_address = "https://ipawind-apps.samnangem00.workers.dev" # your url shortner api

PASSWORD = "1"
api_key = ""
api_urls = []

admin = [7069590773] # add your telegram user ID
reseller = []

web_path = "/var/www/html"
template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>items</key>
    <array>
      <dict>
        <key>assets</key>
        <array>
          <dict>
            <key>kind</key>
            <string>software-package</string>
            <key>url</key>
            <string><![CDATA[{url}]]></string>
          </dict>
          <dict>
            <key>kind</key>
            <string>full-size-image</string>
            <key>url</key>
            <string><![CDATA[{redirect_url}]]></string>
          </dict>
          <dict>
            <key>kind</key>
            <string>display-image</string>
            <key>url</key>
            <string><![CDATA[{redirect_url}]]></string>
          </dict>
        </array>
        <key>metadata</key>
        <dict>
          <key>bundle-identifier</key>
          <string><![CDATA[{package_name}]]></string>
          <key>bundle-version</key>
          <string>1.0.0</string>
          <key>kind</key>
          <string>software</string>
          <key>title</key>
          <string>{appname}</string>
        </dict>
      </dict>
    </array>
  </dict>
</plist>"""


accounts = [
]

reseller_accounts = {
}


excluded_accounts = (

)
