mkdir -p ~/.streamlit/

echo "
[general]
email = \"${HEROKU_EMAIL_ADDRESS}\"
" > ~/.streamlit/credentials.toml

echo "
[server]
headless = true
enableCORS = false
port = $PORT

[theme]
primaryColor = "#E694FF"
backgroundColor = "#0c0538"
secondaryBackgroundColor = "#bac4d6"
textColor = "#C6CDD4"


" >> ~/.streamlit/config.toml


