mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"${HEROKU_EMAIL_ADDRESS}\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\

[theme]

primaryColor = "#E694FF"
backgroundColor = "#0c0538"
secondaryBackgroundColor = "#bac4d6"
textColor = "#C6CDD4"
font="sans"


" > ~/.streamlit/config.toml


