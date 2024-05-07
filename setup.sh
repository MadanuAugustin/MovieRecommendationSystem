# refer streamlit documentation for the below commands

mkdir -p ~/.streamlit/


echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml