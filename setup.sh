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

[theme]\n\
primaryColor = "#E694FF"\n\
backgroundColor = "#0c0538"\n\
secondaryBackgroundColor = "#bac4d6"\n\
textColor = "#C6CDD4"\n\


" > ~/.streamlit/config.toml


