Remove-Item .venv -Recurse -Force -Confirm:$false -ErrorAction SilentlyContinue

python -m venv .venv
.\.venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r .\requirements.txt
